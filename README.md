# Grow Kit — Website 🌳

[![Pages](https://github.com/parvenuprompting/grow-kit-site/actions/workflows/pages.yml/badge.svg)](https://github.com/parvenuprompting/grow-kit-site/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/parvenuprompting/Grow-Kit/blob/main/LICENSE)
[![Privacy](https://img.shields.io/badge/tracking-geen-success?style=flat-square)]()
[![Fonts](https://img.shields.io/badge/fonts-self--hosted-teal?style=flat-square)]()
[![Made by](https://img.shields.io/badge/build_in_public-Ti%C3%ABndo-9cf?style=flat-square)]()

**De website van Grow Kit** — live op: **https://parvenuprompting.github.io/grow-kit-site/**

> **De agent bewijst. Jij bepaalt.**
> Statische site in editorial-monochrome stijl: geen tracking, geen cookies, self-hosted fonts.

## Wat is dit?

De publieke voorkant van [Grow Kit](https://github.com/parvenuprompting/Grow-Kit), de zero-trust AI-werkbank. Deze site legt in vier stappen uit hoe het harnas werkt (idee → scope-poort → agent met bewijs → ratificatie), stelt de agent-familie voor (zeven agents, elk met eigen rol en stem), en linkt rechtstreeks naar de repo.

## Pagina's

| Pagina | Inhoud |
|---|---|
| `index.html` | Hero, de drie wetten als kaarten, install-blok met kopieerknop |
| `hoe-het-werkt/` | De vier stappen + crash-herstel (test 4) |
| `familie/` | De zeven agents met rol en stem |

## Techniek

- **Statisch HTML+CSS** — geen framework, geen build-stap, geen JavaScript behalve de kopieerknop
- **Fonts self-hosted** (SIL OFL): Fraunces 400/400-italic, Inter 400/600 — `fonts/`
- **Geen tracking, geen cookies, geen externe requests**
- **Deploy**: GitHub Actions (`pages.yml`) — elke push naar `main` staat de site binnen ±30 seconden bij

## Lokaal draaien

```bash
python3 -m http.server 8747
# → http://localhost:8747
```

## Licentie

MIT — zelfde als [Grow Kit](https://github.com/parvenuprompting/Grow-Kit).
