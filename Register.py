def add_menu_item(menu, name, price):
	menu[name] = price

def rem_menu_item(menu, name):
	if menu.get(name, "Doesn't exist"):
		del menu[name]

def order_input(menu):
	orders = {}
	x = 1
	total = 0
	while (True):
		if x < 2:
			order = input('What would you like to order? (Enter Q to finish your order)\n')
		else:
			order = input("Anything else for you today? (Enter Q to finish your order)\n")
		found = menu.get(order)
		if order.lower() == 'bazinga':
			print ("Sorry, all out of the Bazinga.")
			continue
		if order.upper() == 'Q':
			store_order(orders)
			print(total)
			break
		if found:
			total += menu[order]
			orders[order] = menu[order]
			print(orders)
		else:
			print ("Menu item doesn't exist")
		x += 1

def store_order(order):
	sales_log = open("Today's orders.txt", 'a')
	total = 0
	for item, price in order.items():
		total += price
		sales_log.write (item + ' ' + format(price, '.2f') + "\n")
	sales_log.write ("total = " + format(total, '.2f') +  '\n\n')
	sales_log.close

def load_menu(menu):
	file = open("menu.txt", 'r')
	name = []
	price = []
	for line in file:
		line = line.strip()
		if type(line) == str:
			name.append(line)
		elif type(line) == int:
			price.append(line)
		else:
			raise TypeError
	for item, value in zip(name, price):
		menu[item] = price
	print(menu)
	return menu


def main():
	menu = {}
	load_menu(menu)
	add_menu_item(menu, 'Hamburger', 1.99)
	print(menu)
	add_menu_item(menu, 'Double Cheeseburger', 2.99)
	print(menu)
	rem_menu_item(menu, 'Hamburger')
	print(menu)
	order_input(menu)
main()