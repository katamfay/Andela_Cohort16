
"""A BankAccount class with methods and properties"""

class My_Bank_Account:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance
	def deposit(self, amount):
		self.balance += amount
		return self.balance

		"""Inheritance showing how class Least_Amount inherits from
		 class My_Bank_Account """

class Least_Amount(My_Bank_Account):
	def __init__(self, Least_Amount):
		My_Bank_Account.__init__(self)
		self.Least_Amount = Least_Amount


	def withdraw(self, amount):
	    if self.balance - amount < self.Least_Amount:
	        print "Sorry, Not enough Balance"
	    else:
	        My_Bank_Account.withdraw(self, amount)

        """A class showing polymorphism"""


class Savings_Account(My_Bank_Account):
	def __init__(self, Savings_Account):
		My_Bank_Account.__init__(self)
		self.Savings_Account = Savings_Account





	        	