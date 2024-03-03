class Category:
		
	def __init__(self, name):
		self.name = name
		self.ledger = []
	
	def deposit(self, amount, description=False):
		if description != False:
			self.ledger.append({"amount": amount, "description": description})
		else:
			self.ledger.append({"amount": amount, "description": ""})
	
	def withdraw(self, amount, description=False):
		if description != False:
			if self.get_balance() >= amount:
				self.ledger.append({"amount": -amount, "description": description})
				return True
			else:
				return False
		else:
			if self.get_balance() >= amount:
				self.ledger.append({"amount": -amount, "description": ""})
				return True
			else:
				return False
	
	def get_balance(self):
		funds = 0
		for x in self.ledger:
			funds += x["amount"]
		return funds
	
	def transfer(self, amount, budget_category):
		if self.get_balance() >= amount:
			self.withdraw(amount, "Transfer to " + budget_category.name)
			budget_category.deposit(amount, "Transfer from " + self.name)
			return True
		else:
			return False
	
	def check_funds(self, amount):
		if self.get_balance() >= amount:
			return True
		else:
			return False
			
	def __str__(self):
		title = self.name.center(30, "*") + "\n"
		items = ""
		total = 0
		for x in self.ledger:
			items += x["description"][:23] + (str("{:.2f}".format((x["amount"])))[:7] + "\n").rjust(31 - len(x["description"][:23]))
			total += x["amount"]
		return f"{title}{items}Total: {total}"

def create_spend_chart(categories):
	
	a = [] #List of categories 
	b = [] #The spent in each category
	c = [] #The percentage spent in each category
	
	for x in categories:
		a.append(x.name)
		spent = 0
		for y in (x.ledger):
			if y["amount"] < 0 and x.name == a[len(a) - 1]:
				spent += y["amount"]
		b.append(spent)
				
	for z in b:
		p = round(z / sum(b), 2) * 100
		c.append(p)	
	
	s = "Percentage spent by category\n"
	r = reversed(range(0, 110, 10))
	
	for x in r:
		s += str(x).rjust(3) + "| "
		for y in c:
			if y >= x:
				s += "o  "
			else:
				s += "   "
		s += "\n"
	s += " ".rjust(4) + 10 * "-" + "\n"
	m = []
	
	for x in a:
		m.append(len(x))
	
	n = int(max(m))
	i = 0
	
	while i < n:
		s += " ".rjust(5)
		for x in a:
			if i < len(x):
				s += x[i] + 2 * " "
			else:
				s += 3 * " "
		i += 1
		if i <= n - 1:
			s += "\n"
		
	return s
