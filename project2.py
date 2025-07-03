

grocery_list = []
print('--- Grocery List Tracker ---')
while True:
    print('What will you like to do?')
    print('Press 1 Add item to your grocery list')
    print('Press 2 View item in your grocery list')
    print('Press 3 Check item in your grocery list')
    print('Press 4 Remove item in your grocery list')
    print('Press 5 Clear all item in your grocery list')
    print('Press 6 Sort item in your grocery list')
    print('Press 7 Exit')
    choice = int(input('Enter your choice'))

    if choice == 1:
        name = input('Enter grocery name').lower()
        grocery_list.append(name)
        print('Item Added to List successfully')

    elif choice == 2:
        if grocery_list:
            for x in grocery_list:
                print(x)
        else:
            print('List is empty')

    elif choice == 3:
        check_item = input('Enter the item you want to check')
        if check_item in grocery_list:
            print('Item is in the list')
        else:
            print('Item not in list')

    elif choice == 4:
        name = input('Enter name you want to remove').lower()
        if name in grocery_list:
            grocery_list.remove(name)
            print('Item successfully removed')
        else:
            print('Item not found')

    elif choice == 5:
        grocery_list.clear()
        print('Items successfully cleared')

    elif choice == 6:
        grocery_list.sort()
        print(grocery_list)

    elif choice == 7:
        print('Exiting from program')
        break

    else:
        print('Invalid input')
