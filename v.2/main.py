from db import create_tab, add_expense, see_expenses

def main():
	print('DB EXPENSES RECORD')
	create_tab()
	add_expense(50, "prova")
	see_expenses()




if __name__ == "__main__":
	main()