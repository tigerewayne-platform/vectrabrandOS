# Vectra Shop

**No surprises. Just tech.** This is the brand system for vectrashop.co.za, the consumer storefront of The Vectra Group. Everything that carries the Vectra Shop name follows it from 22 November 2026: the website, product pages, Google Shopping listings, ads, emails, WhatsApp replies and packaging inserts.

When this system and a one-off idea disagree, the system wins. To change it, change this file first, then the work.

## 1. Position: radical honesty

**The idea:** most tech stores sell the same products at similar prices. We stand out by being the store that never surprises you. You see real stock, a real delivery date and a straight answer, including "you don't need the expensive one".

**Tagline:** No surprises. Just tech.

**Who we sell to:** South African homes, home offices and small businesses who want the right kit without learning the spec sheet first. We write for them, not for enthusiasts who already know what a CAS latency is.

**What we promise:**
- Stock you can see: Cape Town and Johannesburg counts on every product, and an arrival date when it's out.
- A date, not a range: "Arrives Thursday 27 Nov", never "3 to 5 working days".
- The price you pay is the price you see, incl. VAT, with delivery shown before checkout.
- Straight advice, even when it means a smaller sale.

**What we are not:** the cheapest on every SKU, or the store for people chasing frame rates. We let others fight on price and hype.

### Things we won't do
These are published on the site. Breaking one is a bigger problem than losing a sale.
1. No "in stock" unless it is on a shelf in Cape Town or Johannesburg today.
2. No fake "was" prices. A was-price means we sold it at that price in the last 30 days.
3. No countdown timers or "only 2 left" unless the number is real.
4. No hidden fees at checkout.
5. No upsell we wouldn't buy ourselves.

### Signature: the stock line
Every product card and page carries one line in the same format: `4 in Cape Town · Ships Tuesday` or `Back in Johannesburg around 14 Dec`. It's the one thing people should remember us by. Never hide it, never round it into "available".

> Proposed, not live: a delivery-date guarantee (miss the date and we refund the delivery fee), a signed note in every box, and a buying advisor whose job is to recommend the cheapest product that does the job. These depend on who dispatches orders and are decided separately.

## 2. Voice

**Plain, specific, honest. Calm, never hyped.** Write like the person at the counter who knows the stock and has nothing to prove. If a sentence would sound strange said out loud to a customer, rewrite it.

Four rules:
1. **Facts over adjectives.** A number, a date or a place beats any describing word.
2. **Say the limitation.** Every product description names one thing it won't do. That sentence is what makes the rest believable.
3. **Plain words first.** Lead with what it does for the buyer, then the spec. "Keeps your Wi-Fi on for about 6 hours" before "12V 7Ah".
4. **No pressure.** We inform, we don't push. If someone should wait for stock or buy the cheaper option, we say so.

| Do | Don't |
| --- | --- |
| "2 left in Cape Town. Ships tomorrow." | "Hurry! Limited stock!!!" |
| "Runs a router and fibre box for about 6 hours." | "Ultimate power solution for your needs." |
| "R1 099 incl. VAT" | "Only R1 099!" |
| "Out of stock in Johannesburg. Back around 14 Dec." | "Coming soon" with no date |
| "Most people don't need 32GB. 16GB runs Office and Chrome fine." | "Upgrade to 32GB for blazing performance!" |
| "Won't power a fridge. For that you need the 2kVA." | (no limitation mentioned) |
| "We got your order. It leaves Cape Town on Tuesday." | "Your order is being processed." |

**Where the voice shows most:** out-of-stock pages, error messages, order emails and refund replies. These are where other stores sound like a machine; we sound like a person who owns the problem.

Banned in all Vectra copy: unlock, elevate, seamless, game-changing, robust, cutting-edge, best-in-class, ultimate, "in today's world", "Hurry", exclamation marks in headlines, all-caps sentences, emoji in product titles.

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

- **Geist** for everything, the same family as the wordmark. Headings at 700 with -0.02em tracking, body at 400, prices at 800.
- **JetBrains Mono** for SKUs and spec values in tables.
- Prices always use tabular figures so they line up in grids.

## 5. Product content rules

These apply to every product on the site, whether loaded from the Syntech feed or added by hand.

- **Title format:** `Brand Model Key-spec Type`, e.g. "UGREEN 55W Fast Charging Power Bank". No promo words in titles, no ALL CAPS, max 70 characters so it fits Google Shopping.
- **Price display:** `R1 099` with a space as thousands separator, no cents unless non-zero, always followed by "incl. VAT" on product pages. Was-price only when the item genuinely sold at that price in the last 30 days.
- **Stock display (the stock line):** one line per warehouse on every card and product page, with the real count: "12 in Cape Town", "3 in Johannesburg". Above 50 show "50+". Empty with an ETA: "Back in Johannesburg around 14 Dec". Empty with no ETA: "None in Cape Town". Green at 6 or more, amber at 1 to 5 or with an ETA, red when none.
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

- **Wordmark:** lowercase "vectra" in Geist Bold followed by the descriptor ("shop" or "group") in Geist Light, same size, on one baseline. The descriptor is copper for **vectra shop** (the retail brand) and slate for **vectra group** (the company), so the two are told apart at a glance while reading as one family. Copper in the Group logo appears only in the V.
- **Lockups:** **horizontal** (mark, "vectra" and the descriptor on one line) is the default everywhere: website header, emails, documents, invoices. The `inline` files are the same lockup, kept under that name so older links still work. **Stacked** (mark centred above the words) is for square spaces such as packaging and profile tiles. Files are in `brand/assets/logo/lockup/`.
- **Versions:** `colour` on white or bench, `reverse` on graphite, `mono-graphite` for one-colour print and invoices, `mono-white` on photos. The mark alone also has an `on-copper` version.
- **Clear space:** keep at least the height of the descriptor's letters, doubled, clear on every side. The SVG files already include it.
- **Minimum size:** mark alone 16px (favicon), horizontal lockup 110px wide on screen, 30mm in print.
- **Never:** recolour the blades, swap their order, add gradients or shadows, capitalise or re-set the wordmark, make the Group descriptor copper, or put the colour version on copper or a busy photo.
- **Favicons and app icons** are in `brand/assets/logo/favicon/`. Social profile images and banners (LinkedIn, Facebook, X) for Shop and Group are in `brand/assets/social/`. Profile images are safe for circle crops.

## 8. How we keep it

- This system lives at its own link and in the theme's `theme.json`. Colours and type in the theme come only from these tokens.
- Any new colour, font or component is added here first.
- Logo files are generated by `scripts/build_logos.py` with the type converted to outlines, so they never depend on an installed font. Change the script, never hand-edit an exported file.
