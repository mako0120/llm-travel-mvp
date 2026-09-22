# Luxury Travel Production Queue

This module is the durable production queue for the luxury-travel social workflow.

## Ownership
- Claude: discovers/researches candidates and inserts approved candidates.
- Database: every inserted candidate is a production target. No score threshold is used.
- ChatGPT: claims the oldest pending item, re-checks current official facts/prices/photos, creates the Canva design, QA-checks all 5 pages, then marks it completed.
- Canva: final artifact store.
- GitHub: schema, automation code, migration history and recovery trail.

## Queue rule
`status = pending ORDER BY created_at ASC`.

Statuses: `pending -> processing -> completed`, or `failed` with retry metadata.

## Reliability
`claim_oldest_pending_travel()` uses `FOR UPDATE SKIP LOCKED` so parallel workers do not claim the same candidate.

A candidate is not marked completed until the Canva design has passed QA and its design ID is stored.

## Data principles
- Registration means approved for production.
- Scores are not required and never gate production.
- Prices are timestamped checks with conditions; never guessed.
- Official source URLs are retained for re-verification.
- Canva copy/layout is intentionally not stored here; ChatGPT owns composition at production time.
