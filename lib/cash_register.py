#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, new_item, price, quantity = 1):
    self.total += price * quantity
    for i in range(quantity):
      self.items.append(new_item)
      self.last_transaction = [new_item, price, quantity]

  def apply_discount(self):
    self.total -= int(self.total * self.discount / 100)
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${self.total}.")

  def items_list_without_multiples(self):
    unique_list = list(set(self.items))
    print(unique_list)
    return unique_list
  
  def items_list_with_multiples(self):
    return self.items
  
  def void_last_transaction(self):
    transaction = self.last_transaction
    self.total -= transaction[1] * transaction[2]
    print(f"{transaction[2]} {transaction[0]}(s) has been removed from the shopping list")