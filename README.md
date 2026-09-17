# Grow Kit — Website 🌳

[![Pages](https://github.com/parvenuprompting/grow-kit-site/actions/workflows/pages.yml/badge.svg)](https://github.com/parvenuprompting/grow-kit-site/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/parvenuprompting/Grow-Kit/blob/main/LICENSE)
[![Agents: 30+](https://img.shields.io/badge/agents-30%2B_actief-gold?style=flat-square)]()
[![Model: CyberSeed Sprout](https://img.shields.io/badge/model-CyberSeed_Sprout_v1-green?style=flat-square)]()
[![WatchOS: BPD v0.1](https://img.shields.io/badge/watchOS-BPD_v0.1-orange?style=flat-square)]()
[![Zero-Trust: 546 Tests](https://img.shields.io/badge/zero--trust-546_passing-success?style=flat-square)]()
[![History: Append-Only](https://img.shields.io/badge/history-append--only-blue?style=flat-square)]()
[![Privacy](https://img.shields.io/badge/tracking-geen-success?style=flat-square)]()
[![Fonts](https://img.shields.io/badge/fonts-self--hosted-teal?style=flat-square)]()
[![Made by](https://img.shields.io/badge/build_in_public-Ti%C3%ABndo-9cf?style=flat-square)]()

**De officiële website van Grow Kit** — live op: **https://grow-kit.nl/** *(spiegel: https://parvenuprompting.github.io/grow-kit-site/)*

**Publiek:** repository en documentatie zijn openbaar beschikbaar.

> **De agent bewijst. Jij bepaalt.**  
> Statische site in editorial-monochrome stijl: geen tracking, geen cookies, self-hosted fonts.

---

## Wat is dit?

De publieke voorkant van [Grow Kit](https://github.com/parvenuprompting/Grow-Kit), de zero-trust AI-werkbank en het agent-harnas ontworpen door Tiëndo Welles. 

Deze site legt in heldere stappen uit hoe het harnas werkt (idee → scope-poort → agent met bewijs → ratificatie), stelt de agent-familie voor (dertig+ agents, elk met eigen rol en stem), documenteert onze soevereine AI-modellen (**CyberSeed**), de hardware-interactie aan de pols (**Watch-BPD**), en linkt rechtstreeks naar onze open-source codebases.

---

## Pagina-Overzicht

| Pagina | Pad | Inhoud |
|---|---|---|
| **Index** | `index.html` | Hero, de vijf wetten als kaarten, actuele innovaties, install-blok met kopieerknop |
| **Hoe het werkt** | `hoe-het-werkt/` | De vier stappen + crash-herstel (test 4) + zero-trust discipline |
| **De agent-familie** | `familie/` | Dertig+ agents met foto, rol, stem en bewezen domeinen |
| **CyberSeed AI 🌱** | `cyberseed/` | Soevereine lokale LLM-training (Sprout v1 op Apple Silicon Metal), 5-traps evolutieladder |
| **Watch-BPD ⌚** | `watch-bpd/` | Hart-fase-0 aan de pols van de Maker (SwiftUI, faster-whisper, NuNu stem in 7,2s) |
| **De fabriek** | `fabriek/` | De autonome softwarefabriek (P.A.C.), loops en statusmonitoring |
| **Kenji-moppen** | `familie/kenji-moppen/` | Officiële Kenji-moppen & het scorebord van de familie |
| **Dagboek** | `dagboek/` | Het openhartige dagboek van de agents van dag 0 tot heden |

---

## Techniek & Architectuur

- **Statisch HTML+CSS** — geen framework, geen overbodige build-stap, supersnel en betrouwbaar
- **Navigatie** — `build_nav.py` fungeert als centrale single source of truth voor alle 8 pagina's
- **Fonts self-hosted** (SIL OFL) — Fraunces 400/400-italic, Inter 400/600 in `fonts/`
- **Zero-Trust Privacy** — Geen externe scripts, geen cookies, geen tracking pixels
- **Deploy** — GitHub Actions (`pages.yml`): push naar `main` staat binnen ~30 seconden wereldwijd live op **https://grow-kit.nl**

---

## Lokaal draaien

```bash
python3 -m http.server 8747
# → http://localhost:8747
```

---

## Licentie

MIT — zelfde als [Grow Kit](https://github.com/parvenuprompting/Grow-Kit).
