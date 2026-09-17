#!/usr/bin/env python3
"""build_nav.py — één bron van waarheid voor het zijmenu en mobiele menu van de Grow Kit-site."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

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

# Pattern matching old nav structure
NAV_BLOCK_RE = re.compile(
    r'(?:<header class="mobile-header".*?</header>\s*)?'
    r'(?:<div class="side-nav-overlay"[^>]*></div>\s*)?'
    r'<nav class="side-nav"[^>]*>.*?</nav>',
    re.S
)

def relatief(pad: str, diepte: int) -> str:
    if pad == "":
        return "./" if diepte == 0 else "../" * diepte
    return "../" * diepte + pad

def actief(item_pad: str, pagina_pad: str) -> bool:
    if item_pad == "":
        return pagina_pad == ""
    return pagina_pad.startswith(item_pad)

def nav_html(diepte: int, pagina_pad: str) -> str:
    brand = relatief("", diepte)
    logo = relatief("assets/logo.png", diepte)
    
    regels = []
    
    # 1. Vaste mobiele topbalk (alleen zichtbaar op mobiel via CSS)
    regels.append(f'''<header class="mobile-header">
  <a class="brand" href="{brand}"><img src="{logo}" alt="Grow Kit"><span>Grow <em>Kit</em></span></a>
  <button type="button" class="hamburger-btn" id="mobileMenuBtn" aria-label="Menu openen">
    <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
      <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
    </svg>
  </button>
</header>
<div class="side-nav-overlay" id="sideNavOverlay"></div>''')

    # 2. Side-nav container
    regels.append('<nav class="side-nav" id="side-nav" aria-label="Hoofdmenu">')
    regels.append(f'''  <div class="drawer-top">
    <a class="brand" href="{brand}"><img src="{logo}" alt="Grow Kit"><span>Grow <em>Kit</em></span></a>
    <button type="button" class="side-nav-close" id="sideNavCloseBtn" aria-label="Menu sluiten">✕</button>
  </div>''')

    for pad, label, icoon in MENU:
        cur = ' aria-current="page"' if actief(pad, pagina_pad) else ""
        regels.append(
            f'  <a class="item"{cur} href="{relatief(pad, diepte)}">'
            f'<span class="icoon">{icoon}</span><span class="label">{label}</span></a>'
        )
    # Externe link naar Parvenu Lab
    regels.append(
        '  <div style="margin-top:18px;padding-top:14px;border-top:1px solid var(--line);">'
        '    <a class="item" href="https://parvenulab.nl/" target="_blank" rel="noopener">'
        '      <span class="icoon">🏛️</span><span class="label">Parvenu Lab ↗</span></a>'
        '  </div>'
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
        
        # Zorg ook dat side-nav.js wordt ingeladen vóór </body>
        js_rel = relatief("css/side-nav.js", diepte)
        js_tag = f'<script src="{js_rel}"></script>'
        if js_tag not in src:
            src = src.replace("</body>", f"{js_tag}\n</body>")
            
        if NAV_BLOCK_RE.search(src):
            src2 = NAV_BLOCK_RE.sub(lambda m: nieuwe, src, count=1)
        else:
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
