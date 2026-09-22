-- Luxury Travel production queue
create extension if not exists pgcrypto;

create table if not exists public.travel_content_queue (
  id uuid primary key default gen_random_uuid(),
  title text not null,
  canonical_name text,
  category text,
  region text,
  prefecture text,
  address text,
  official_url text,
  booking_url text,
  official_social_url text,
  operator_name text,
  summary text,
  unique_experience text,
  highlights jsonb not null default '[]'::jsonb,
  target_travelers jsonb not null default '[]'::jsonb,
  recommended_season text,
  why_now text,
  access_info text,
  research_sources jsonb not null default '[]'::jsonb,
  photo_source_urls jsonb not null default '[]'::jsonb,
  source_system text not null default 'claude',
  source_external_id text,
  source_created_at timestamptz,
  status text not null default 'pending' check (status in ('pending','processing','completed','failed')),
  processing_started_at timestamptz,
  completed_at timestamptz,
  failed_at timestamptz,
  failure_reason text,
  retry_count integer not null default 0,
  canva_design_id text,
  canva_design_url text,
  canva_folder_id text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index if not exists travel_content_queue_source_unique
on public.travel_content_queue(source_system, source_external_id)
where source_external_id is not null;

create index if not exists travel_content_queue_pending_oldest
on public.travel_content_queue(status, created_at asc);

create table if not exists public.travel_price_checks (
  id uuid primary key default gen_random_uuid(),
  queue_id uuid not null references public.travel_content_queue(id) on delete cascade,
  checked_at timestamptz not null,
  amount numeric,
  currency text not null default 'JPY',
  price_unit text,
  guest_count integer,
  stay_or_use_date date,
  room_or_plan text,
  meal_condition text,
  tax_condition text,
  service_charge_condition text,
  other_conditions text,
  source_url text not null,
  created_at timestamptz not null default now()
);

create table if not exists public.travel_production_events (
  id bigint generated always as identity primary key,
  queue_id uuid not null references public.travel_content_queue(id) on delete cascade,
  event_type text not null,
  detail jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create or replace function public.claim_oldest_pending_travel()
returns setof public.travel_content_queue
language plpgsql
security definer
as $$
declare picked uuid;
begin
  select id into picked
  from public.travel_content_queue
  where status = 'pending'
  order by created_at asc, id asc
  for update skip locked
  limit 1;

  if picked is null then return; end if;

  update public.travel_content_queue
  set status='processing', processing_started_at=now(), updated_at=now()
  where id=picked;

  return query select * from public.travel_content_queue where id=picked;
end;
$$;
