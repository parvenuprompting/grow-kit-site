#!/usr/bin/env python3
"""build_nav.py — één bron van waarheid voor het zijmenu van de Grow Kit-site.

Hoe het werkt:
  1. Hieronder staat PAGINA'S: de complete menulijst (volgorde = menuvolgorde).
  2. Dit script injecteert die nav in ELKE index.html op de site, met per
     pagina de juiste relatieve paden en automatisch de actieve markering
     (aria-current="page") op basis van waar het bestand ligt.
  3. Idempotent: opnieuw draaien is veilig; oude nav's worden eerst weggehaald.

Nieuwe pagina toevoegen:
  - Maak map/index.html aan (bv. 'nieuws/index.html').
  - Zet de map in de lijst hieronder (of laat weg: dan staat hij niet in het menu).
  - Draai: python3 build_nav.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# (pad-vanuit-siteroot-met-slash, label, icoon).  "" = homepage.
MENU = [
    ("", "Index", "⌂"),
    ("hoe-het-werkt/", "Hoe het werkt", "⚙"),
    ("familie/", "De agent-familie", "❖"),
    ("cyberseed/", "CyberSeed AI 🌱", "🧬"),
    ("watch-bpd/", "Watch-BPD ⌚", "♡"),
    ("fabriek/", "De fabriek", "⬢"),
    ("familie/kenji-moppen/", "Kenji-moppen", "♟"),
    
    ("dagboek/", "Dagboek", "❡"),
]

NAV_RE = re.compile(r'<nav class="side-nav"[^>]*>.*?</nav>', re.S)


def relatief(pad: str, diepte: int) -> str:
    if pad == "":
        return "./" if diepte == 0 else "../" * diepte
    return "../" * diepte + pad


def actief(item_pad: str, pagina_pad: str) -> bool:
    """aria-current automatisch: item is actief als de pagina precies op het
    item-pad ligt, of eronder valt (bv. fabriek/agenda/ markeert fabriek/)."""
    if item_pad == "":
        return pagina_pad == ""
    return pagina_pad.startswith(item_pad)


def nav_html(diepte: int, pagina_pad: str) -> str:
    regels = ['<nav class="side-nav" id="side-nav" aria-label="Hoofdmenu">']
    brand = relatief("", diepte)
    logo = relatief("assets/logo.png", diepte)
    regels.append(
        f'<a class="brand" href="{brand}"><img src="{logo}" alt="Grow Kit">'
        '<span class="brand-tekst">Grow <em>Kit</em></span></a>'
    )
    for pad, label, icoon in MENU:
        cur = ' aria-current="page"' if actief(pad, pagina_pad) else ""
        regels.append(
            f'<a class="item"{cur} href="{relatief(pad, diepte)}">'
            f'<span class="icoon">{icoon}</span><span class="label">{label}</span></a>'
        )
    regels.append("</nav>")
    return "\n".join(regels)


def main() -> None:
    gewijzigd = []
    for bestand in sorted(ROOT.rglob("index.html")):
        rel = bestand.relative_to(ROOT).as_posix()
        pagina_pad = "" if rel == "index.html" else rel.rsplit("/", 1)[0] + "/"
        diepte = 0 if pagina_pad == "" else pagina_pad.count("/")
        src = bestand.read_text(encoding="utf-8")
        nieuwe = nav_html(diepte, pagina_pad)
        if NAV_RE.search(src):
            src2 = NAV_RE.sub(lambda m: nieuwe, src, count=1)
            # extra oude nav's (mocht er ooit een dubbele in zitten) opruimen
            src2 = NAV_RE.sub("", src2, count=99) if src2.count(nieuwe) > 1 else src2
        else:
            # geen nav gevonden: direct na <body> invoegen
            src2 = re.sub(r"(<body[^>]*>)\n?", r"\1\n" + nieuwe + "\n", src, count=1)
        if src2 != src:
            bestand.write_text(src2, encoding="utf-8")
            gewijzigd.append(f"{rel} (actief: {pagina_pad or 'Index'})")
    if gewijzigd:
        print("Bijgewerkt:")
        for g in gewijzigd:
            print("  -", g)
    else:
        print("Alle pagina's waren al actueel.")


if __name__ == "__main__":
    main()
