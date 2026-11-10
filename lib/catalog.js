// Siamak Kalhor's AI product catalog, which Ryan sells. Source: "AI Product Catalog" PDF,
// product information verified on each product's website on November 9, 2026.
// The AI advisor recommends from this list only. Edit here when a product, price or link changes.

export const CATALOG_AS_OF = 'November 9, 2026';

export const PRODUCTS = [
  // AI VISIBILITY
  {
    name: 'S.C.A.L.E.',
    category: 'AI visibility software',
    url: 'https://scale.siamakconsulting.com',
    summary:
      'Self-serve scanner that reads a website the way ChatGPT, Gemini and Claude do, scores it on five stages (Scan, Clarify, Amplify, Leverage, Evaluate) with 22 named checks in about ten seconds, and returns a fix list ranked by impact. With an account it rescans monthly, tracks momentum and checks whether ChatGPT and Perplexity actually name the business.',
    forWho:
      'Small and mid-size business owners, marketers and in-house teams, agencies managing several client sites, any business that wants to be recommended by AI assistants.',
    pricing:
      'Free: $0, 1 website, one scan every 30 days, lessons for top fixes, monthly AI check. Growth: $29/month, 1 website, rescan any time, every fix with lessons, AI check every scan. Scale: $99/month, up to 5 websites. Billed monthly through Stripe, cancel any time. A done-with-you AI Authority Audit is a fixed $1,500.',
    tryIt: 'The scan is free with no account.',
  },
  {
    name: 'S.C.A.L.E. Academy',
    category: 'Online course with AI tutor',
    url: 'https://siamakconsulting.com/academy',
    summary:
      'Six-week online course taught by Siamak Kalhor on how ChatGPT, Gemini, Claude and Perplexity pick which businesses to recommend (the five-stage S.C.A.L.E. Framework). Six lessons of 25 to 35 minutes, an AI tutor by text or voice that coaches you on your own business in your language, weekly hands-on exercises with the free S.C.A.L.E. app, and a shareable certificate.',
    forWho:
      'Business owners who want to do it themselves, marketers and marketing teams, agency staff who need to learn LLMO, consultants adding AI visibility to their services.',
    pricing: 'Week 1 free with just an email. Full course $197 one-time, lifetime access to all six weeks, the AI tutor and the certificate.',
    tryIt: 'Week 1 is free.',
  },
  // AI AGENTS & VOICE
  {
    name: 'Agent Studio',
    category: 'No-code AI agent builder',
    url: 'https://agents.siamakconsulting.com',
    summary:
      'No-code builder for an AI business agent: name it, give it a voice, connect store, site, inbox and CRM. It watches orders, leads and reviews, follows up, reports on money, and runs social media (weekly post plans, captions, hashtags, reel and TikTok scripts, comment reply drafts), with everything approved by the owner before it goes out. Industry packs for online stores, medical, dental, law, home services, real estate, mortgage, financial advisors, restaurants, salons and B2B; HIPAA-aware agents for doctors and State Bar-aware intake for attorneys.',
    forWho: 'Online stores, medical and dental practices, law firms, home services and contractors, other small businesses.',
    pricing:
      'Build it yourself: free agent preview plus 3 free content plans; full blueprint $99. Live agent: $249/month (currently waitlist). Done for you: $3,500 plus $1,000/month. Regulated industries (doctors, dentists, lawyers, financial advisors): from $5,000 plus $1,500/month. Some connections are live today; others switch on as each launches.',
    tryIt: 'Free preview in about 2 minutes.',
  },
  {
    name: 'Your Legal Brain',
    category: 'AI client intake for law firms',
    url: 'https://yourlegalbrain.com',
    summary:
      "24/7 AI voice intake for law firms in English, Spanish, Farsi and Armenian. A potential client presses one button on the firm's website and talks; the assistant says it is an AI, gathers the facts, asks practice-area follow-ups (personal injury, criminal defense, family, immigration, employment, landlord-tenant, estate, business and more), flags urgent matters and possible deadlines, lists opposing parties for conflict checks, and delivers a structured intake with transcript to the firm within about a minute for an attorney to review.",
    forWho:
      'Personal injury, criminal defense and immigration firms; family, employment and landlord-tenant practices; firms serving Spanish, Farsi or Armenian speakers; any firm that misses after-hours calls.',
    pricing: 'Pricing on request (not published).',
    tryIt: 'Live demo on the site. Firms can be live in about ten minutes by choosing practice areas and pasting one line of code.',
  },
  {
    name: 'Lending Desk',
    category: 'AI lending desk for non-bank lenders',
    url: 'https://lendingdesk.app',
    summary:
      "AI lending desk that answers borrowers and brokers 24/7 by chat and voice in English, Spanish, Persian, German and Chinese, asks three to five questions per loan program, checks the deal against the lender's states, loan limits and leverage (LTV, LTC, loan-to-ARV), scores every lead and routes it to the right account executive with a complete file. Shows live market rates (never a quote). Partner brokers can embed it with one line of code.",
    forWho:
      'Non-bank and private lenders; hard money, fix-and-flip, bridge, construction and DSCR lenders; mortgage broker networks; commercial real estate lenders.',
    pricing:
      "Pricing on request, depends on volume and setup. Each desk is configured for the lender's states, programs and account executives, branded, and launched on the lender's own domain in about four weeks.",
    tryIt: 'Try it live on the site, or book a demo.',
  },
  {
    name: 'Orchamind',
    category: 'AI operations for contractors',
    url: 'https://orchamind.com',
    summary:
      'Voice-run AI office manager for contractors: log hours, assign crew and update jobs hands-free; writes itemized estimates from a photo of the plans and Good, Better, Best proposals; dispatch, scheduling and GPS time clock; flags jobs trending over budget or behind schedule and sends a plain-English morning briefing. Built and proven with Howard Construction Inc.',
    forWho:
      'General contractors; electricians, plumbers, HVAC and roofers; painting, landscaping, solar, flooring, concrete and other field-service businesses; small and mid-size contractors priced out of ServiceTitan or Buildertrend.',
    pricing:
      'First month free, then $500/month per company. No card to start, no per-seat fees, cancel anytime. Professional website add-on: $750 one-time, done for you, with a free site audit.',
    tryIt: 'First month free, no card needed. Live demo on the site.',
  },
  {
    name: 'ResBizAI',
    category: 'AI restaurant management',
    url: 'https://resbizai.com',
    summary:
      'One voice-run system for restaurant staff, inventory, menus and money: shifts, call-outs and payroll export from a phone; recipe-linked inventory that depletes as dishes sell, with low-stock alerts and one-tap supplier orders; photograph a vendor invoice and it reads every line; exact food cost and margin per dish; daily P&L and a 30-second nightly count that shows variance.',
    forWho:
      'Independent restaurants and wine country bistros; fine dining, fast casual, bars and taprooms; catering, hotel restaurants and food halls; multi-location restaurant groups.',
    pricing: '30-day free trial, then $500/month per restaurant. Cancel anytime.',
    tryIt: 'First month free. Live demo on the site.',
  },
  // INDUSTRY SOFTWARE
  {
    name: 'Textile Wizard',
    category: 'ERP for fabric and textile businesses',
    url: 'https://textilewizard.com',
    summary:
      'Operating system for fabric distributors: tracks every roll and dye lot (yards on hand vs. available, oversold alerts), turns packing lists into invoices without retyping, accounts receivable with 30/60/90 aging and one-click statements, AI that reads PDF purchase orders, mill invoices and remittances and drafts entries for approval, and an optional wholesale-only catalog with a Request Price button. Works in a browser or on a phone.',
    forWho: 'Fabric distributors and wholesalers, converters, importers and mills, apparel manufacturers, Fashion District style fabric houses.',
    pricing: '$500/month for the whole company. Thirty days free, no card to start. Unlimited users, no per-seat pricing, no module upsell, no implementation fee.',
    tryIt: 'Thirty days free with no card.',
  },
  {
    name: 'Weftwise',
    category: 'AI catalog tools for fabric stores',
    url: 'https://weftwise.vercel.app',
    summary:
      'Three tools in one script tag for online fabric stores: an AI Fabric Expert on every product page that answers shopper questions using only the listing (never invents fiber, stock or price); a Yardage Calculator for 18 garment and home projects that sets the cart quantity; and Catalog Studio, which turns a supplier note and photo into a finished listing with SEO fields, FAQ and schema.',
    forWho: 'Online fabric stores, fabric retailers on Shopify or WooCommerce, quilting, sewing and craft shops, stores with large messy supplier catalogs.',
    pricing:
      'Pricing on request. Founding stores are being onboarded now and get a store key, a setup call and their first 100 fabrics enriched at no charge.',
    tryIt: 'Try the live Fabric Expert on the site.',
  },
  {
    name: 'K2 Investment Parcel Finder',
    category: 'California land feasibility AI',
    url: 'https://land.siamakconsulting.com',
    summary:
      'Type a California address and get a land feasibility report in under two minutes with a downloadable branded PDF: parcel record, zoning and density (allowed uses, minimum lot size, dwellings by right, ADU potential, buildable envelope), deal-killer checks (FEMA flood, CAL FIRE hazard severity, Williamson Act, terrain) as green, amber or red flags, assessed value and sales history, and a written AI investor analysis with a verdict. California only.',
    forWho: 'Real estate investors and land buyers, developers and builders screening sites, real estate agents and brokers, lenders and advisors doing early due diligence.',
    pricing: 'Pricing on request (not published).',
    tryIt: 'Try it on the site.',
  },
  {
    name: 'InstaChecker',
    category: 'Telegram bot for Instagram account monitoring',
    url: 'https://t.me/omidmehrbot',
    summary:
      "Telegram bot that watches Instagram accounts around the clock and sends an instant alert in Telegram and Discord the moment a banned or disabled account is restored. Paste or forward usernames and links; links in a forwarded client message are auto-tagged to that client; private watch lists and per-client reports.",
    forWho: 'Social media marketing agencies, account managers handling many client Instagram accounts, creators and brands recovering a banned account.',
    pricing: 'Pricing on request (not published).',
    tryIt: 'Open @omidmehrbot in Telegram.',
  },
  // FREE APPS & DESIGN
  {
    name: 'AisleBird',
    category: 'Free smart grocery list app',
    url: 'https://aislebird.com',
    summary:
      'Grocery list that sorts itself in the order you walk your specific store, with a department hint on every item. Add items by voice, typing, pasting a recipe or from history; real-time shared lists; works offline with no app to download. The site lists 11 store chains and 300+ locations (Whole Foods, Trader Joe\'s, Costco, Target and more).',
    forWho: 'Busy families and household shoppers, home cooks who shop from recipes, anyone who wants a faster store trip.',
    pricing: 'Free forever, all features, no credit card. Pro coming soon at $3.99/month for power users.',
    tryIt: 'Free on the site, no app download.',
  },
  {
    name: 'Napa Wino',
    category: 'Free AI Napa Valley sommelier and guide',
    url: 'https://napawino.com',
    summary:
      'Free AI Napa sommelier: describe your perfect day and it plans a tasting route across 50+ wineries and 16 AVAs with stops in order and lunch included. Also GPS town guides (Napa, Yountville, St. Helena, Calistoga, no app), trip planning guides, editor picks, harvest report, events and Napa real estate listings. Zero paid placements in the wine and dining guide.',
    forWho: 'Napa Valley visitors and first-timers, wine lovers planning a trip, people considering buying property in Napa, licensed agents with Napa listings.',
    pricing: 'Free for visitors. Licensed agents can list real estate free during launch. No other business pricing is published.',
    tryIt: 'Plan a Napa day free on the site.',
  },
  {
    name: 'Pattern Studio',
    category: 'AI sewing pattern maker',
    url: 'https://studio.siamakconsulting.com',
    summary:
      'Browser-based AI sewing pattern maker by Blue Moon Fabrics: choose one of 24 garment types (bikinis, leggings, sports bras, leotards, dresses, corsets, rash guards and more), enter measurements, pick the fabric, and get a cut-ready pattern with seam allowance, grain lines and notches, an AI Style Picker, fabric yield and auto-nesting, a designer sketch in the chosen fabric, size grading and print-ready or DXF export.',
    forWho: 'Independent fashion designers, home sewists and seamstresses, cosplayers and costume makers, swimwear, activewear and dancewear makers.',
    pricing:
      'Free: first 10 pattern generations with sketches, yield planning and print-at-home. Studio: $19.99/month (size grading, DXF/SVG export, unlimited patterns). Pro: $24.99/month (adds AI photorealistic model photos).',
    tryIt: 'Start free on the site, nothing to install.',
  },
  {
    name: 'Custom Pattern Studio',
    category: 'Client build: AI pattern maker inside an online store',
    url: 'https://bluemoonfabrics.com/pages/custom-pattern-studio',
    summary:
      "AI made-to-measure pattern maker Siamak built into Blue Moon Fabrics' online store: a designer describes a garment and the AI generates a sewing pattern previewed on a fabric chosen from the store. It shows what Siamak can build for a client: a custom AI feature embedded in an existing store that turns browsing into buying.",
    forWho: 'Fabric and craft retailers who want a similar tool, e-commerce brands that want a custom AI feature in their store, investors evaluating Siamak\'s build track record.',
    pricing: 'Pricing on request. Custom AI builds are quoted per project.',
    tryIt: 'See it live on the Blue Moon Fabrics site.',
  },
];

export const CATALOG_TEXT = PRODUCTS.map(
  (p, i) =>
    `${i + 1}. ${p.name} (${p.category}) - ${p.url}
   What it does: ${p.summary}
   Who it's for: ${p.forWho}
   Pricing: ${p.pricing}
   Try it: ${p.tryIt}`,
).join('\n');
