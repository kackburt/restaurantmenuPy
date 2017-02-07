
print("Welcome to your restaurant menu - add dishes to your daily menu list.")

# Taskmanager
yes = ['yes', 'y']
save = ['save', 's', 'exit', 'e', 'x']
menu = {}

currency = raw_input("Enter a currency for your menu: ")

while True:
    dish = raw_input("Enter a dish for the menu: ")
    price = float(raw_input("Enter a price for '%s' " % dish))
    menu[dish] = price
    newdish = raw_input("Do you want to add another dish (y)es or (s)ave and (e)xit. ")

    if newdish.lower() in yes:
        continue

    elif newdish.lower() in save:
        with open("menu.txt", "w+") as menu_file:
            for dish in menu:
                menu_file.write("%s, %s, %s\n" % (dish, menu[dish], currency))
                break

print("Your menu includes now: ") + str(menu)

