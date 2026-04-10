from ast import Return
from multiprocessing import Value
import os

def instructions() -> None:
    print("--- ISTRUZIONI ---")
    print("» Inserisci: <importo> <categoria>")
    print("  Esempio: 50 Cibo")
    print("» Scrivi 'exit' per uscire\n")

def banner() -> None:
    print("==========================")
    print("     EXPENSE TRACKER      ")
    print("==========================")
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
            answer = input(f"Salvare i record in {name_file}{ext}? (Y/n): ")
            if(answer.strip() == "" or answer.strip().lower() == "y"):
                return name_file+ext
            elif(answer.strip().lower() == "n"):
                name_file = input("Nuovo nome file: ")
                if name_file.strip() == "":
                    raise ValueError    
                return name_file+ext
        except ValueError:
            print("[!] Errore: Il nome del file è vuoto")        

def save_data(file_name:str ,amount: int, reason: str):
    with open(file_name, "a") as f:
        f.write(f"\n${amount} --> {reason}\n")
            
def check_data(amount, reason) -> bool:
    if not (isinstance(amount,  int) or isinstance(reason, str)):
        return False
    return True

def menu_p() -> None:
    print("\n--- MENU SELEZIONE ---")
    print("1. Aggiungi spesa")
    print("2. Mostra spese")
    print("3. Esci")
    print("----------------------")

def menu() -> int:
    while(True):
        try:
            menu_p()
            choice = int(input('Scelta > '))
            if not (1 <= choice <=3):
                raise ValueError
            return choice
        except ValueError:
            print("[!] Opzione non valida")
            os.system('clear' if os.name == 'posix' else 'cls')

def insert_data(file_name: str) -> None:    
    os.system('clear' if os.name == 'posix' else 'cls')
    print("--- INSERIMENTO SPESE ---")
    print()
    instructions()
    while (True):
        input_expense = input('> ')
        if input_expense.strip().lower() == 'exit':
            break
        try:
            amount, reason = input_expense.split()
            if not check_data(amount, reason):
                raise ValueError()
            save_data(file_name, str(amount), reason)
            print("[*] Dato salvato correttamente")
        except ValueError:
            print("[!] Errore: Formato non corretto")

def p_data(file_name):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("--- STORICO SPESE ---")
    try:
        with open(file_name, "r") as f:
            content = f.read()
            if not content.strip():
                print("Nessuna spesa registrata.")
            else:
                print(content)
    except FileNotFoundError:
        print("[!] File non trovato.")
    input(f"\nPremere INVIO per tornare al menu...")

def main():
    file_name = file_rename()
    while(True):
        os.system('clear' if os.name == 'posix' else 'cls')
        banner()
        input(f'Premere INVIO per continuare...\n')
        os.system('clear' if os.name == 'posix' else 'cls')
        choice = menu()
        if choice == 1:
            insert_data(file_name)
        elif choice == 2:
            p_data(file_name)
        elif choice == 3:
            print("Chiusura in corso...")
            break
    
if __name__ == "__main__":
    main()