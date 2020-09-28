#Create a program that let the user know the price of an item from a supermarket. The user must select one of the options provided to see the real price.
#1. List of items and prices
Items_List = ["1. Potato", "2. Egg", "3. Milk Cartom", "4. Cereal Box", "5. Gansitos", "6. 1L water bottle", "7. 1lb of Meat", "8. 5 Lemons", "9.Bag of chips", "10. 1L bottle orange juice", "11. 1 Pack of ham", "12. 1 loaf of bread", "13. Cheese", "14. Sausage", "15. bag of mints"]
Price_list = [1.22, 0.50, 5.0, 8.99, 3.50, 3.25, 2.50, 1.16, 2.50, 4.3, 7.76, 3.60, 2.45, 3.10, 4.30]
#2. Item price selector
while True:
    print()
    print(Items_List)
    Price_Select = int(input("Select an item (1 = Potato, 2 = egg, etc...) --> "))
    print()
    Fetch_Item_Price = Price_list[Price_Select-1]
    print()
    print("The price for this item is:", Fetch_Item_Price, "$")
    print()
    Continue_Program = int(input("Enter 1 to continue, Enter any other number to exit: "))
    if Continue_Program == 1:
        print("Continuing...")
        print()
    elif Continue_Program != 1:
        print()
        print("Goodbye")
        raise SystemExit
    else:
        print("Invalid option")