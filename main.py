from ast import Return
from multiprocessing import Value
import os

def instructions() -> None:
	print("Instructions:")
	print("- Enter your expense in the format: <amount> <category>")
	print("  Example: 50 Food")
	print("- Type 'exit' to quit the program\n")

def banner() -> None:
	print("=== EXPENSE TRACKER ===\n")
	instructions()

def new_file() -> None:
	pass

def file_rename() -> str:
	name_file = "expenses_file"
	flag = 0
	ext = ".txt"
	while(True):	
		try:
			banner()
			answer = input(f"Save records in {name_file}{ext}? (Y/n)")
			if(answer.strip() == "" or answer.strip().lower() == "y"):
				return name_file+ext
			elif(answer.strip().lower() == "n"):
				name_file = input("New file name: ")
				if name_file.strip() == "":
					raise ValueError	
				return name_file+ext
		except ValueError:
			print("[!] New file name empty")		


	with open("{name_file}{ext}", "a") as f:
		f.write(f"\n${amount} --> {reason}\n")
	
def save_data(file_name:str ,amount: int, reason: str):
	with open(file_name, "a") as f:
		f.write(f"\n${amount} --> {reason}\n")
			
def check_data(amount, reason) -> bool:
	if not (isinstance(amount,  int) or isinstance(reason, str)):
		return False
	return True

def menu_p() -> None:
	print("\n=== MENU ===")
	print("1. Aggiungi spesa")
	print("2. Mostra spese")
	print("3. Esci")

def menu() -> None:
	while(True):
		menu_p()
		choice = input('>')
	


def main():
	file_name = file_rename()
	os.system('clear')
	banner()
	input(f'Press ENTER to continue...\n')
	os.system('clear')
	menu_p()
	while (True):
		input_expense = input('> ')
		if input_expense.strip().lower() == 'exit':
			break
		try:
			amount, reason = input_expense.split()
			if not check_data(amount, reason):
				raise ValueError()
			save_data(file_name, str(amount), reason)
		except ValueError:
			print("Error: Variables are wrong")

if __name__ == "__main__":
	main()