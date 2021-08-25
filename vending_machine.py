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
				
