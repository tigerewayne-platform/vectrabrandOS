# Vectra Brand OS

The brand operating system for Vectra Shop (vectrashop.co.za). Everything carrying the Vectra Shop name follows it from 22 November 2026.

| Path | What it is |
| --- | --- |
| `brand/BRAND.md` | The brand book: position, voice, colour, type, product content rules, layout rules. Start here. |
| `brand/tokens.json` | The single source for colours (light and dark), type, spacing and radius. |
| `dist/tokens.css` | CSS custom properties (`--vs-*`) generated from the tokens. |
| `dist/theme.json.fragment.json` | Palette, fonts and spacing for the WordPress block theme's `theme.json`. |
| `brand/assets/logo/` | Split V mark, Shop and Group lockups (SVG and PNG), favicons and app icons. |
| `brand/assets/social/` | Profile image and banners for LinkedIn, Facebook and X, for Shop and Group. |
| `scripts/build_tokens.py` | Rebuilds `dist/` from `brand/tokens.json`. |
| `scripts/build_logos.py` | Rebuilds the logo SVGs with outlined type. |
| `CHANGELOG.md` | Every change to the brand, dated. |

## Rules for changing the brand

1. Change `brand/BRAND.md` or `brand/tokens.json` first, never the theme directly.
2. Run `python3 scripts/build_tokens.py` and commit `dist/` with the change.
3. Add a line to `CHANGELOG.md` saying what changed and why.
4. Changes go through a pull request so there is a record of who approved them.

The live, browsable version of this system is pinned in the owner's claude.ai sidebar as "Vectra Shop Brand System".
