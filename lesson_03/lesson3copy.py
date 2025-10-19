class User:

	def __init__(self, name):
		print("я создался")
		self.username = name

	def sayName(self):
		print("меня зовут ", self.username)

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")

alex.sayName()