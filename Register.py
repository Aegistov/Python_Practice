import requests
import json

def add_menu_item(menu, name, price):
	new_entry = {}
	new_entry["name"] = name
	new_entry["price"] = price
	menu.append(new_entry)
	print (menu)
	master_menu = open("menu.json", 'w')
	master_menu = json.dump(menu, master_menu)
	return master_menu

def rem_menu_item(menu, name):
	for item in menu:
		if item['name'] == name:
			menu.remove(item)
			master_menu = open("menu.json", 'w')
		master_menu = json.dump(menu, master_menu)

def order_input(menu):
	orders = []
	x = 1
	total = 0
	found = False
	while (True):
		if x < 2:
			order = input('What would you like to order? (Enter Q to finish your order)\n')
		else:
			order = input("Anything else for you today? (Enter Q to finish your order)\n")
		for item in menu:
			if order == item['name']:
				total += item['price']
				orders.append(item['name'])
				found = item
				print(orders)
		if found is False:
				print ("Menu item doesn't exist")
		if order.upper() == 'Q':
			store_order(orders, total)
			print(total)
			break
		x += 1

def store_order(order, total):
	sales_log = open("Today's orders.txt", 'a')
	for name in order:
		sales_log.write (name + "\n")
	sales_log.write ("total = " + format(total, '.2f') +  '\n\n')
	sales_log.close

def load_menu(menu):
	try:
		menu_request = requests.get("http://link to website here")
		daily_menu = menu_request.json()
	except:
		print("Could not connect with website. Loading Backup Menu.")
		try:
			daily_menu = open("menu.json", 'r')
		except:
			print("File does not exist.")
	return daily_menu


def main():
	menu = []
	load_menu(menu)
	add_menu_item(menu, 'Hamburger', 1.99)
	print(menu)
	add_menu_item(menu, 'Double Cheeseburger', 2.99)
	print(menu)
	#rem_menu_item(menu, 'Hamburger')
	print(menu)
	order_input(menu)
main()