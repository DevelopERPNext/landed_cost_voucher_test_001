frappe.ui.form.on("Landed Cost Voucher", {
    onload: function(frm) {
        if (frm.doc.docstatus === 0) {
//        if (frm.doc.docstatus === 0 && frm.doc.stock_entry_type === 'Manufacture' && frm.doc.bom_check === 1) {
            frm.add_custom_button(__('Landed Cost Voucher Test'), function() {
                frappe.call({
                    method: "landed_cost_voucher_test_001.landed_cost_voucher_test_001.landed_cost_voucher_py.create_print_msg",
                    args: {
                        "doc": frm.doc.name,
                    },
                    callback: function(response) {
                        if (response.message) {
                            frappe.show_alert({
                                message: __(response.message),
                                indicator: 'green'
                            });
                            frm.reload_doc();
                            // frm.refresh();
                        }
                        frm.reload_doc();
                    }
                });
            }).addClass('btn-warning').css({
                'color': 'white',
                'font-weight': 'bold',
                'background-color': '#274472'
            });
        }
    },
});



// ==============================================





//frappe.ui.form.on('Landed Cost Voucher', {
//    validate: function(frm) {
//        frappe.call({
//            method: 'landed_cost_voucher_test_001.landed_cost_voucher_test_001.landed_cost_voucher_py.create_journal_entry_from_lcv',
//            args: {
//                lcv_name: frm.doc.name
//            },
//            callback: function(r) {
//                if(r.message) {
//                    frappe.msgprint(__('Journal Entry {0} created successfully.', [r.message]));
//                }
//            }
//        });
//    }
//});





// ==============================================
// ==============================================













