-- ============================================================
-- UNIVERSAL DIGITAL MENU ADMIN PANEL — SUPABASE SCHEMA
-- Reusable SQL Template for Any Restaurant / Store
-- ============================================================

-- 1. PRODUCT AVAILABILITY TABLE
create table if not exists public.product_availability (
  product_id text primary key,
  is_available boolean not null default true,
  updated_at timestamp with time zone default timezone('utc'::text, now()) not null
);

-- 2. WHATSAPP ORDERS TABLE
create table if not exists public.orders (
  id text primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  date text not null,
  time text,
  timestamp bigint,
  items jsonb not null default '[]'::jsonb,
  subtotal numeric default 0,
  delivery_fee numeric default 0,
  total numeric not null default 0,
  status text not null default 'pending',
  service_type text,
  delivery_area text,
  address text,
  payment text,
  notes text
);

-- 3. ENABLE ROW LEVEL SECURITY (RLS)
alter table public.product_availability enable row level security;
alter table public.orders enable row level security;

-- Product Availability Security Policies:
drop policy if exists "Public can view product availability" on public.product_availability;
create policy "Public can view product availability"
  on public.product_availability for select
  to anon, authenticated
  using (true);

drop policy if exists "Admin can manage availability" on public.product_availability;
create policy "Admin can manage availability"
  on public.product_availability for all
  to authenticated
  using (true)
  with check (true);

-- Orders Security Policies:
drop policy if exists "Public can insert orders" on public.orders;
create policy "Public can insert orders"
  on public.orders for insert
  to anon, authenticated
  with check (true);

drop policy if exists "Admin can view orders" on public.orders;
create policy "Admin can view orders"
  on public.orders for select
  to authenticated
  using (true);

drop policy if exists "Admin can update orders" on public.orders;
create policy "Admin can update orders"
  on public.orders for update
  to authenticated
  using (true);

-- 4. ENABLE REALTIME SYNC
alter publication supabase_realtime add table public.product_availability;
alter publication supabase_realtime add table public.orders;
