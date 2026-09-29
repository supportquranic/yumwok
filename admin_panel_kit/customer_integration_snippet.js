// ============================================================
// CUSTOMER WEBSITE INTEGRATION SNIPPET
// Add this to any customer-facing menu website to connect it
// to the Supabase Admin Panel.
// ============================================================

/*
<!-- STEP 1: Add these two scripts inside <head> of customer HTML: -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="supabase-config.js"></script>
*/

// STEP 2: State variable for unavailable products
let unavailableItems = new Set();

// STEP 3: Listen for Real-Time Product Availability
async function initProductAvailability() {
    if (typeof supabaseClient === 'undefined' || !supabaseClient) return;

    try {
        // Initial load
        const { data, error } = await supabaseClient
            .from('product_availability')
            .select('product_id, is_available');

        if (!error && data) {
            unavailableItems.clear();
            data.forEach(row => {
                if (row.is_available === false) {
                    unavailableItems.add(row.product_id);
                }
            });
            // Call your UI render function to grey out / mark unavailable
            if (typeof renderProducts === 'function') renderProducts();
        }

        // Real-time listener: instantly updates without page refresh
        supabaseClient
            .channel('public:product_availability')
            .on('postgres_changes', { event: '*', schema: 'public', table: 'product_availability' }, payload => {
                if (payload.new) {
                    if (payload.new.is_available === false) {
                        unavailableItems.add(payload.new.product_id);
                    } else {
                        unavailableItems.delete(payload.new.product_id);
                    }
                } else if (payload.eventType === 'DELETE' && payload.old) {
                    unavailableItems.delete(payload.old.product_id);
                }
                if (typeof renderProducts === 'function') renderProducts();
            })
            .subscribe();
    } catch (e) {
        console.warn('Availability init error:', e);
    }
}

// STEP 4: Record WhatsApp Order in Database when checkout button is clicked
function recordOrderToSupabase(orderData) {
    if (typeof supabaseClient === 'undefined' || !supabaseClient) return;

    try {
        const now = new Date();
        const dateStr = now.getFullYear() + '-' + String(now.getMonth()+1).padStart(2,'0') + '-' + String(now.getDate()).padStart(2,'0');
        const timeStr = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', hour12: true });
        const orderId = 'ORD-' + Date.now().toString(36).toUpperCase() + '-' + Math.random().toString(36).substring(2, 6).toUpperCase();

        supabaseClient.from('orders').insert([{
            id: orderId,
            items: orderData.items || [],               // Array of { name, qty, unitPrice, total, options }
            subtotal: orderData.subtotal || 0,
            delivery_fee: orderData.deliveryFee || 0,
            total: orderData.total || 0,
            service_type: orderData.serviceType || '',  // 'Home Delivery' or 'Take Away'
            delivery_area: orderData.deliveryArea || '',
            address: orderData.address || '',
            payment: orderData.payment || '',
            notes: orderData.notes || '',
            status: 'pending',
            timestamp: Date.now(),
            date: dateStr,
            time: timeStr
        }]).then(({ error }) => {
            if (error) console.warn('Order save error:', error);
        });
    } catch(e) {
        console.warn('Order recording failed:', e);
    }
}
