# Vectra Shop

Local stock, straight answers. This is the brand system for vectrashop.co.za, the consumer storefront of The Vectra Group. Everything that carries the Vectra Shop name follows it from 22 November 2026: the website, product pages, Google Shopping listings, ads, emails, WhatsApp replies and packaging inserts.

When this system and a one-off idea disagree, the system wins. To change it, change this file first, then the work.

## 1. Position (draft, to be confirmed by Wayne)

**Who we sell to:** South African home and small-office buyers who know roughly what they need and want it from local stock, at a fair price, without being upsold.

**What we promise:** you see exactly where the stock is (Cape Town or Johannesburg), what it costs incl. VAT, and when it arrives. No "in stock" that turns out to be a supplier back-order.

**What we are not:** the cheapest price on every SKU. Takealot and the specialist PC stores will win some price fights. We compete on certainty and clarity, and we price to protect margin.

> Open question: this position is a proposal. Until Wayne confirms it, treat section 1 as provisional and sections 2 to 6 as binding.

## 2. Voice

Write like a knowledgeable person behind the counter: direct, specific, a little dry. Short sentences. Rand amounts and real specs instead of adjectives.

| Do | Don't |
| --- | --- |
| "2 left in Cape Town. Ships tomorrow." | "Hurry! Limited stock!!!" |
| "Runs a router and fibre box for about 6 hours." | "Ultimate power solution for your needs." |
| "R1 099 incl. VAT" | "Only R1 099!" |
| "Out of stock in Johannesburg. Back around 14 Dec." | "Coming soon" with no date |

Banned in all Vectra copy: unlock, elevate, seamless, game-changing, robust, cutting-edge, "in today's world", exclamation marks in headlines, all-caps sentences, emoji in product titles.

Load-shedding, fibre, rand, CPT and JHB are our vocabulary. Use South African English (colour, organise, programme).

## 3. Colour

Graphite & Copper. Graphite is the frame and the ink; copper is the only loud colour and it always means "act here" or "this is on sale".

- `graphite-frame` with `frame-ink` for the header, hero panels and footer.
- `bench` page ground, `card` for anything holding a product, `tile` for category tiles and chips.
- `copper` for buy buttons, sale badges and active states only. Text on copper is `copper-ink` (graphite). **Never white text on copper**: it fails contrast at 3.4:1.
- `copper-text` when copper has to be text or a link on a light ground.
- `stock-in`, `stock-low`, `stock-out` are reserved for stock status and form errors. Never use green, amber or red as decoration, or shoppers stop trusting them.
- One copper element per card. If everything is copper, nothing is.

## 4. Type

- **Sora** (display) for headings and hero lines only. Tight tracking, heavy weights.
- **Manrope** (body) for everything else, including prices at weight 800.
- **JetBrains Mono** for SKUs and spec values in tables.
- Prices always use tabular figures so they line up in grids.

## 5. Product content rules

These apply to every product on the site, whether loaded from the Syntech feed or added by hand.

- **Title format:** `Brand Model Key-spec Type`, e.g. "UGREEN 55W Fast Charging Power Bank". No promo words in titles, no ALL CAPS, max 70 characters so it fits Google Shopping.
- **Price display:** `R1 099` with a space as thousands separator, no cents unless non-zero, always followed by "incl. VAT" on product pages. Was-price only when the item genuinely sold at that price in the last 30 days.
- **Stock display:** show CPT and JHB separately on every card and product page. 6 or more = "In stock", 1 to 5 = "2 left", 0 with an ETA = "Back around 14 Dec", 0 with no ETA = "Out of stock".
- **Descriptions:** never publish the distributor's copy unchanged on priority products. Rewrite the top 300 by revenue in Vectra voice: one line on who it is for, three to five spec bullets that matter, one honest limitation.
- **Images:** distributor packshots on pure white, hosted on our own server, never hot-linked. Minimum 1000px square. No added text or badges baked into images.
- **SKU:** prefix distributor SKUs with `VG-` (already in use). Never change a SKU once live.

## 6. Layout and components

- Borders, not shadows. Cards are `card` with a `hairline` border and `radius-md`.
- Buttons and chips are pills (`radius-pill`). Primary button: `copper` fill, `copper-ink` text. Secondary: `graphite` fill, white text.
- Product grid gap `space-3`; homepage section gap `space-8` on desktop, `space-5` on mobile.
- Every product card carries, in this order: image, brand label, name, price, VAT note, stock by warehouse, add to cart. Nothing else.
- No entry popups. A newsletter offer lives in a strip or an exit-intent prompt.
- Imagery for banners and category tiles: product on a graphite or tile ground, shot or rendered, no lifestyle stock photos of people.

## 7. Logo

The Split V: two blades meeting at a point. The left blade is graphite (or white on dark grounds), the right blade is always copper, the same "act here" colour as the buy button. It replaces the three-facet blue and silver mark from 22 November 2026.

- **Lockups:** the mark beside "VECTRA" in Sora 800, with a descriptor (SHOP or GROUP) in tracked Manrope 700. Three layouts: **inline** (mark, VECTRA and the descriptor on one line) for the website header, email headers and any bar under 60px tall; **horizontal** (descriptor under VECTRA) for documents, invoices and packaging; **stacked** where width is tight. Files are in `brand/assets/logo/lockup/`.
- **Versions:** `colour` on white or bench, `reverse` on graphite, `mono-graphite` for one-colour print and invoices, `mono-white` on photos. The mark alone also has an `on-copper` version.
- **Clear space:** keep at least the height of the descriptor's letters, doubled, clear on every side. The SVG files already include it.
- **Minimum size:** mark alone 16px (favicon), horizontal lockup 120px wide on screen, 30mm in print.
- **Never:** recolour the blades, swap their order, add gradients or shadows, italicise or re-set the wordmark, or put the colour version on copper or a busy photo.
- **Favicons and app icons** are in `brand/assets/logo/favicon/`. Social profile images and banners (LinkedIn, Facebook, X) for Shop and Group are in `brand/assets/social/`. Profile images are safe for circle crops.

## 8. How we keep it

- This system lives at its own link and in the theme's `theme.json`. Colours and type in the theme come only from these tokens.
- Any new colour, font or component is added here first.
- Logo files are generated by `scripts/build_logos.py` with the type converted to outlines, so they never depend on an installed font. Change the script, never hand-edit an exported file.
