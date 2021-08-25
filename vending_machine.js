vending_machine.js
==================

// Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vending Machine', {
	// refresh: function(frm) {
		

		
	// },
	setup: function(frm){
		(frm.fields_dict["item_table"].grid.get_field(
            "item_name"
        ).get_query = function () {
            return {
                filters: {    stock:['>', +0],
                            },
            };
        });
    

	}
    
});
frappe.ui.form.on('Vending Machine Item Table', {
    qauntity: function(frm, cdt,cdn){
    var row = locals[cdt][cdn]
        
        row.total = row.qauntity * row.rate
        refresh_field("item_table");
        
        var gnd_total = 0;
    
        for(var i = 0; i<frm.doc.item_table.length; i++){
            gnd_total += +frm.doc.item_table[i].total;
        }
    
    
        frm.set_value('grand_total', gnd_total);    
        refresh_field("grand_total");
    
    },
    
    });
