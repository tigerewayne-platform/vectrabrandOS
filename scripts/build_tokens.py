"""Build CSS variables and a WordPress theme.json fragment from brand/tokens.json.

Run: python3 scripts/build_tokens.py
Outputs go to dist/. Never edit dist/ by hand; edit brand/tokens.json and rebuild.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
t = json.loads((root / "brand" / "tokens.json").read_text())

themes = [th["id"] for th in t["color"]["themes"]]
light, dark = themes[0], themes[1]

def css_block(theme):
    lines = []
    for tok in t["color"]["tokens"]:
        v = tok["value"]
        val = v.get(theme, v[light]) if isinstance(v, dict) else v
        lines.append(f"  --vs-{tok['name']}: {val};")
    return "\n".join(lines)

shared = []
for fam in ("spacing", "radius"):
    for tok in t[fam]["tokens"]:
        shared.append(f"  --vs-{tok['name']}: {tok['value']};")
for k, v in t["type"]["families"].items():
    shared.append(f"  --vs-font-{k}: {v};")

css = f"""/* Vectra Shop brand tokens. Generated from brand/tokens.json. Do not edit. */
:root {{
{css_block(light)}
{chr(10).join(shared)}
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
{css_block(dark)}
  }}
}}
:root[data-theme="dark"] {{
{css_block(dark)}
}}
"""
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "tokens.css").write_text(css)

slug = lambda n: n.replace(".", "-")
theme_json = {
    "$schema": "https://schemas.wp.org/trunk/theme.json",
    "version": 3,
    "settings": {
        "color": {
            "defaultPalette": False,
            "custom": False,
            "palette": [
                {"slug": slug(tok["name"]), "name": tok["name"].replace("-", " ").title(),
                 "color": tok["value"][light] if isinstance(tok["value"], dict) else tok["value"]}
                for tok in t["color"]["tokens"]
            ],
        },
        "typography": {
            "fontFamilies": [
                {"slug": k, "name": k.title(), "fontFamily": v}
                for k, v in t["type"]["families"].items()
            ]
        },
        "spacing": {
            "spacingSizes": [
                {"slug": tok["name"], "name": tok["name"], "size": tok["value"]}
                for tok in t["spacing"]["tokens"]
            ]
        },
        "custom": {"radius": {tok["name"].replace("radius-", ""): tok["value"] for tok in t["radius"]["tokens"]}},
    },
}
(root / "dist" / "theme.json.fragment.json").write_text(json.dumps(theme_json, indent=2) + "\n")
print("Built dist/tokens.css and dist/theme.json.fragment.json")
