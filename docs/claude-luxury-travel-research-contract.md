# Luxury Travel Research Queue Contract

Claude is the discovery and primary-research producer for the luxury travel queue.

## Boundary
Do: discover, verify, deduplicate, research, and register high-quality candidates.
Do not: design Canva pages, write page-by-page composition, choose Canva layouts, or mark production completed.

## Registration semantics
Every row inserted into `travel_content_queue` is approved for Canva production. There is no score threshold. Do not insert weak or speculative candidates.

Set `status` to `pending`. Preserve the discovery time in `source_created_at` when available. The production worker processes oldest pending records first.

## Required verification
Prefer official website, official booking page, operator, tourism authority, official social accounts, press room, and official releases. Supplement with reputable booking/review sources where useful.

Never invent URLs, prices, review counts, awards, opening status, or availability. Unknown values remain null/unknown.

## Required candidate data
Capture canonical name, category, region/address, official/booking/social URLs, operator, concise factual summary, unique experience, highlights, target travelers, recommended season, why-now rationale, access, research sources, and official photo-source pages when available.

Price observations belong in `travel_price_checks` and must include check time, amount/unit, guest count, date, room/plan, meals, tax/service conditions, other conditions, and source URL whenever each field is known.

## Deduplication
Check existing canonical names, official URLs, and source IDs before inserting. Update an existing candidate when it is the same facility/experience; do not create spelling-variant duplicates.

## Quality gate
Only register candidates with enough verified substance and official visual material to support a strong travel social post. Quality beats volume.
