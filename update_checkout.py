import re

files = [r"d:\ai\yumwok\the_pizza_master_app.html", r"d:\ai\yumwok\index.html"]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove Customer Name and Phone Number fields from checkout form
    # Pattern to match the name and phone fields block
    old_fields = r'''                        <div>
                            <label class="block text-slate-800 font-bold mb-1">
                                Customer Name <span class="text-\[#2E9578\]">\*</span>
                            </label>
                            <input 
                                type="text" 
                                id="custName" 
                                placeholder="Your Name" 
                                class="[^"]*"
                            >
                        </div>

                        <div>
                            <label class="block text-slate-800 font-bold mb-1">
                                Phone Number <span class="text-\[#2E9578\]">\*</span>
                            </label>
                            <input 
                                type="tel" 
                                id="custPhone" 
                                placeholder="e\.g\. 0321-XXXXXXX" 
                                class="[^"]*"
                            >
                        </div>'''
    
    content = re.sub(old_fields, '', content)

    # 2. Update payment dropdown option text
    content = content.replace(
        '<option value="JazzCash / Online Transfer">JazzCash / Online Transfer</option>',
        '<option value="JazzCash / Easypaisa / Online Transfer">JazzCash / Easypaisa / Online Transfer</option>'
    )

    # 3. Update online payment card with both JazzCash & Easypaisa accounts and Shakir Hussain title
    old_payment_card = r'''                        <!-- PAYMENT ACCOUNTS DETAILS CARD WITH 1-CLICK COPY BUTTONS -->
                        <div id="onlinePaymentCard" class="hidden bg-\[#edf8f5\] border border-\[#a8dcce\] rounded-2xl p-3\.5 space-y-3 shadow-sm">
                            <div class="flex items-center justify-between border-b border-\[#a8dcce\]/60 pb-2">
                                <div class="flex items-center gap-2">
                                    <span class="w-7 h-7 rounded-lg bg-\[#2E9578\] text-white flex items-center justify-center font-black text-xs">
                                        <i class="fa-solid fa-money-bill-transfer"></i>
                                    </span>
                                    <div>
                                        <h5 class="text-xs font-black text-slate-900">Direct JazzCash / Online Transfer</h5>
                                        <span class="text-\[10px\] text-slate-600">Account Title: <strong class="text-slate-900 font-bold">Shakir Hussain</strong></span>
                                    </div>
                                </div>
                                <span class="text-\[9px\] font-black uppercase tracking-wider bg-white text-\[#2E9578\] border border-\[#a8dcce\] px-2 py-0\.5 rounded">
                                    Active
                                </span>
                            </div>

                            <!-- Account 1 -->
                            <div class="bg-white p-2\.5 rounded-xl border border-\[#a8dcce\] flex items-center justify-between gap-2">
                                <div class="min-w-0 flex-1">
                                    <span class="text-\[10px\] text-slate-500 block font-medium">JazzCash Account • Shakir Hussain</span>
                                    <span class="text-xs font-black text-\[#2E9578\] tracking-wider font-mono block">0316-5265885</span>
                                </div>
                                <button 
                                    type="button"
                                    onclick="copyToClipboard\('03165265885', 'accBtn1'\)" 
                                    id="accBtn1"
                                    class="[^"]*"
                                >
                                    <i class="fa-regular fa-copy"></i>
                                    <span>Copy</span>
                                </button>
                            </div>

                            <p class="text-\[10px\] text-slate-500 italic text-center">
                                \* Transfer payment & share screenshot on WhatsApp \(0321-0083737\) after order submission\.
                            </p>
                        </div>'''

    new_payment_card = '''                        <!-- PAYMENT ACCOUNTS DETAILS CARD WITH 1-CLICK COPY BUTTONS -->
                        <div id="onlinePaymentCard" class="hidden bg-[#edf8f5] border border-[#a8dcce] rounded-2xl p-3.5 space-y-3 shadow-sm">
                            <div class="flex items-center justify-between border-b border-[#a8dcce]/60 pb-2">
                                <div class="flex items-center gap-2">
                                    <span class="w-7 h-7 rounded-lg bg-[#2E9578] text-white flex items-center justify-center font-black text-xs">
                                        <i class="fa-solid fa-money-bill-transfer"></i>
                                    </span>
                                    <div>
                                        <h5 class="text-xs font-black text-slate-900">JazzCash &amp; Easypaisa Accounts</h5>
                                        <span class="text-[10px] text-slate-600">Account Title: <strong class="text-slate-900 font-bold">Shakir Hussain</strong></span>
                                    </div>
                                </div>
                                <span class="text-[9px] font-black uppercase tracking-wider bg-white text-[#2E9578] border border-[#a8dcce] px-2 py-0.5 rounded">
                                    Active
                                </span>
                            </div>

                            <!-- JazzCash Account -->
                            <div class="bg-white p-2.5 rounded-xl border border-[#a8dcce] flex items-center justify-between gap-2">
                                <div class="min-w-0 flex-1">
                                    <div class="flex items-center gap-1.5">
                                        <span class="text-[10px] font-bold text-amber-700 bg-amber-50 border border-amber-200 px-1.5 py-0.2 rounded">JazzCash</span>
                                        <span class="text-[10px] text-slate-500 font-medium">Title: <strong class="text-slate-800">Shakir Hussain</strong></span>
                                    </div>
                                    <span class="text-xs font-black text-[#2E9578] tracking-wider font-mono block mt-0.5">0316-5265885</span>
                                </div>
                                <button 
                                    type="button"
                                    onclick="copyToClipboard('03165265885', 'accBtn1')" 
                                    id="accBtn1"
                                    class="bg-[#2E9578] hover:bg-[#247861] text-white text-xs font-black px-3 py-1.5 rounded-lg flex items-center gap-1.5 active:scale-95 transition shadow-sm shrink-0"
                                >
                                    <i class="fa-regular fa-copy"></i>
                                    <span>Copy</span>
                                </button>
                            </div>

                            <!-- Easypaisa Account -->
                            <div class="bg-white p-2.5 rounded-xl border border-[#a8dcce] flex items-center justify-between gap-2">
                                <div class="min-w-0 flex-1">
                                    <div class="flex items-center gap-1.5">
                                        <span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 border border-emerald-200 px-1.5 py-0.2 rounded">Easypaisa</span>
                                        <span class="text-[10px] text-slate-500 font-medium">Title: <strong class="text-slate-800">Shakir Hussain</strong></span>
                                    </div>
                                    <span class="text-xs font-black text-[#2E9578] tracking-wider font-mono block mt-0.5">0316-5265885</span>
                                </div>
                                <button 
                                    type="button"
                                    onclick="copyToClipboard('03165265885', 'accBtn2')" 
                                    id="accBtn2"
                                    class="bg-[#2E9578] hover:bg-[#247861] text-white text-xs font-black px-3 py-1.5 rounded-lg flex items-center gap-1.5 active:scale-95 transition shadow-sm shrink-0"
                                >
                                    <i class="fa-regular fa-copy"></i>
                                    <span>Copy</span>
                                </button>
                            </div>

                            <p class="text-[10px] text-slate-500 italic text-center">
                                * Transfer payment &amp; share screenshot on WhatsApp (0321-0083737) after order submission.
                            </p>
                        </div>'''

    content = re.sub(old_payment_card, new_payment_card, content)

    # 4. Update submitOrderToWhatsApp JS function
    old_submit_start = r'''            const custName = document\.getElementById\('custName'\)\.value\.trim\(\);
            const custPhone = document\.getElementById\('custPhone'\)\.value\.trim\(\);
            const address = document\.getElementById\('custAddress'\)\.value\.trim\(\);
            const notes = document\.getElementById\('custNotes'\)\.value\.trim\(\);
            const payment = document\.getElementById\('custPayment'\)\.value;

            if \(!custName\) \{
                showToast\("Please enter your name!"\);
                document\.getElementById\('custName'\)\.focus\(\);
                return;
            \}

            if \(!custPhone\) \{
                showToast\("Please enter your phone number!"\);
                document\.getElementById\('custPhone'\)\.focus\(\);
                return;
            \}'''

    new_submit_start = '''            const address = (document.getElementById('custAddress') ? document.getElementById('custAddress').value.trim() : '');
            const notes = (document.getElementById('custNotes') ? document.getElementById('custNotes').value.trim() : '');
            const payment = document.getElementById('custPayment').value;'''

    content = re.sub(old_submit_start, new_submit_start, content)

    # 5. Remove Customer line from WhatsApp message template
    content = content.replace(
        'message += `*CUSTOMER:* ${custName} (${custPhone})\\n`;\n',
        ''
    )

    # 6. Remove Customer line from receiptPreviewBox
    content = content.replace(
        '<div><strong>Customer:</strong> ${custName} (${custPhone})</div>\n',
        ''
    )

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated checkout fields and payment details in {fpath}")

print("All files updated successfully!")
