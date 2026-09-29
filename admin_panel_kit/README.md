# 🚀 Universal Digital Menu Admin Panel Kit

A standalone, plug-and-play admin panel template for digital menus, restaurants, and local e-commerce stores. Powered by **Supabase** (permanently free tier, real-time database, and secure authentication).

---

## 📁 Kit Contents

| File | Purpose |
|---|---|
| [`admin_template.html`](file:///d:/ai/yumwok/admin_panel_kit/admin_template.html) | Mobile-first admin panel (Dashboard, Product Availability toggles, Order history). |
| [`supabase_template_config.js`](file:///d:/ai/yumwok/admin_panel_kit/supabase_template_config.js) | Supabase configuration file (URL + Anon Key). |
| [`database_schema.sql`](file:///d:/ai/yumwok/admin_panel_kit/database_schema.sql) | 1-click database SQL script (Tables, Row Level Security, Realtime broadcast). |
| [`customer_integration_snippet.js`](file:///d:/ai/yumwok/admin_panel_kit/customer_integration_snippet.js) | Copy-paste JavaScript snippet to connect any customer-facing menu website to this admin panel. |

---

## ⚡ 5-Minute Setup for a New Business

### Step 1: Create Supabase Project
1. Go to [supabase.com](https://supabase.com) and create a free project.
2. In the left sidebar, open **SQL Editor** → **New Query**.
3. Copy all code from [`database_schema.sql`](file:///d:/ai/yumwok/admin_panel_kit/database_schema.sql), paste, and click **Run**.

### Step 2: Create Admin Account
1. In Supabase, go to **Authentication** → **Users**.
2. Click **Add User** → **Create User**.
3. Enter the business owner's email & password, and make sure **Auto Confirm User** is checked.

### Step 3: Configure API Credentials
1. In Supabase, go to **Project Settings** → **API**.
2. Copy the **Project URL** and **anon public** API key.
3. Paste them into [`supabase_template_config.js`](file:///d:/ai/yumwok/admin_panel_kit/supabase_template_config.js).

### Step 4: Customize Products for the Business
Open [`admin_template.html`](file:///d:/ai/yumwok/admin_panel_kit/admin_template.html) and edit the products list near the bottom of the `<script>` tag:

```javascript
const ADMIN_PRODUCTS = [
    { id: 'burger_classic', name: 'Classic Beef Burger', category: 'Burgers' },
    { id: 'pizza_margherita', name: 'Margherita Pizza', category: 'Pizzas' },
    { id: 'fries_regular', name: 'French Fries', category: 'Sides' }
];

const CATEGORIES = ['Burgers', 'Pizzas', 'Sides'];
```

### Step 5: Connect the Customer Website
Follow the instructions inside [`customer_integration_snippet.js`](file:///d:/ai/yumwok/admin_panel_kit/customer_integration_snippet.js):
1. Add Supabase SDK to the customer website's `<head>`.
2. Call `initProductAvailability()` when the menu loads.
3. Call `recordOrderToSupabase(orderData)` when the customer submits their order.

---

## 🌟 Key Features
- **Mobile First Design**: Optimized for store owners using their smartphones.
- **Add to Home Screen**: Installable as a Progressive Web App (PWA) on iPhone & Android.
- **Real-Time Sync**: Disabling an item updates the customer site immediately with zero delay.
- **Live Sales Tracking**: Today's orders count and total sales revenue update in real-time as orders are placed.
- **Zero Server Costs**: Runs 100% on Supabase's free tier.
