// ============================================================
// YUM WOK — Supabase Configuration
// ============================================================
// SETUP REQUIRED: Replace placeholder values below with your
// actual Supabase project URL and anon public key.
//
// Steps to get these values:
// 1. Go to https://supabase.com and create a free project
// 2. Go to Project Settings -> API
// 3. Copy "Project URL" and "anon public" API Key
// 4. Paste them below replacing the YOUR_... placeholders
// ============================================================

const SUPABASE_URL = "https://sfbjvbxjonsdishqroyo.supabase.co";
const SUPABASE_ANON_KEY = "sb_publishable_suk5sTdNIWedRw2h41VN7g_h7CKG9Sv";

// Initialize Supabase client
let supabaseClient = null;
if (typeof supabase !== 'undefined' && typeof supabase.createClient === 'function') {
    try {
        supabaseClient = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
    } catch (e) {
        console.warn('Supabase initialization failed:', e.message);
    }
}
