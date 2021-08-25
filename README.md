# ERP-Task-1
Vending Machine Task
					CREATE A VENDING MACHINE.
DOCTYPE: VENDING MACGINE ITEMS [ ITEMV NAME, RATE, STOCK]
	VALIDATIONS:
		DOC NAME BASED ON ITEM NAME		-- DONE
		WITH AN EMPTY FIELD CAN'T SAVE DOC. 	-- DONE
DOCTYPE: VENDING MACHINE [ CURRENT DATE AND TIME,GRAND TOTAL,CHILD TABLE[ITEM(LINK TO ITEM DOC),QTY,TOTAL] -- DONE

	VALIDATIONS:
		SET NAMING SERIES	-- DONE
		SUBMITABILE DOC		-- DONE
		USER CANT SELECT SAME ITEM TWICE -- DONE
		IF GIVEN QUANTITY GREATER THAN TOTAL STOCK THROW ERROR -- DONE
		BASED ON PURCHASE SELECTED ITEM STOCK REDUCE IN THE ITEM DOC.
		IF ITEM STOCK QUANTITY IS 0 DONT DISPALY IN ITEM FIELD(CHILD TABLE)---DONE
		WITHOUT ANY ITEM AND ITEM QTY GREATERTHAN 0 CANT SUBMIT THE DOC. ---DONE
		

vending_machine.py:
====================

# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VendingMachine(Document):

	def before_save(self):
		self.grand_total =0
		for i in self.get('item_table'):
			i.total = i.rate * i.qauntity
			self.grand_total = self.grand_total + i.total

	def validate(self):
		ls = []
		for i in self.get('item_table'):
			if i.item_name in ls:
				frappe.throw('You can select same item only once')
			else:
				ls.append(i.item_name)
		
		for i in self.get('item_table'):
			doc = frappe.get_doc('Vending Machine Items',{'name':i.item_name})
			if doc.stock < i.qauntity:
				frappe.throw('Quantity limit exceeded')
			elif doc.stock >= i.qauntity:
				doc.stock  -= i.qauntity
				doc.save()
			# else:
			# 	frappe.throw('You should have to buy atleast one item')
		# for i in i.qauntity:
			if i.qauntity <= 0:
				frappe.throw("Quantity should not be zero or negative")

			
			
		# for i in self.get('grand_total'):
		# 	doc = frappe.get_doc('Vending Machine Items',{'name':i.grand_total})
		# 	for i.grand_total:
				


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
