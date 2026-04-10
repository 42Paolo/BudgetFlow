from queries import add_expense, get_expenses

while True:
    print("\n=== MENU ===")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Exit")

    choice = input("> ")

    if choice == "1":
        data = input("Format >50 FOOD: ")
        amount, category = data.replace(">", "").split()
        add_expense(int(amount), category)

    elif choice == "2":
        for row in get_expenses():
            print(row)

    elif choice == "3":
        break

    else:
        print("Invalid choice")