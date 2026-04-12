from db import create_tab, add_expense, see_expenses

def main():
	print('DB EXPENSES RECORD')
	try:
		create_tab()	
	except Exception as e:
		print(f"[Error] Failed create table: {e}")
		return
	try:
		add_expense(50, "prova")
	except Exception as e:
		print(f'[Error] Insert data into table: {e}')
	see_expenses()

if __name__ == "__main__":
	main()