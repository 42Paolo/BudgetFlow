from multiprocessing import Value


def menu() -> int:
	print('--- SPESE LOGIN ---')
	print()
	print('1 - INSERISCI SPESE')
	print('2 - GUARDA SPESE')
	print('3 - EXIT')
	while(True):
		try:
			choice = int(input('>'))
			if not (1 >= choice <= 3):
				raise ValueError
			return choice
		except ValueError:
			print('Opzione non valida')

def exec_opt(choice: int):
	if choice == 1:
		
	elif choice == 2:

	elif choice == 3:
		break

def main():
	


if __name__ == "__main__":
	main()