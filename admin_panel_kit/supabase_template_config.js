// ============================================================
// UNIVERSAL ADMIN PANEL — Supabase Configuration Template
// ============================================================
// Replace the values below with the Supabase project credentials
// for the new client / business.
//
// Where to find these in Supabase:
// 1. Create a free project at https://supabase.com
// 2. Go to Project Settings -> API
// 3. Copy "Project URL" and "anon public" API Key
// ============================================================

const SUPABASE_URL = "https://YOUR_PROJECT_ID.supabase.co";
const SUPABASE_ANON_KEY = "YOUR_ANON_KEY";

// Initialize Supabase client
let supabaseClient = null;
if (typeof supabase !== 'undefined' && typeof supabase.createClient === 'function') {
    try {
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } catch (e) {
        console.warn('Supabase initialization failed:', e.message);
    }
}
