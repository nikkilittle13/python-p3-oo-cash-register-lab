#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity=1):
    item_total = price * quantity
    self.total += item_total
    self.items += [title] * quantity
    self.last_transaction = item_total

  def apply_discount(self):
    discount_in_dollars = self.total * self.discount / 100
    self.total -= discount_in_dollars

    if discount_in_dollars == 0:
      print("There is no discount to apply.")
    
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    pass