import json
from pathlib import Path
from llm_client import ask_llm

transactions = []

def save_transactions():
    file_path = Path(__file__).resolve().parent / "transactions.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)

def load_transactions():
    file_path = Path(__file__).resolve().parent / "transactions.json"

    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            transactions[:] = json.load(file)


def add_transaction():
    while True:
        transaction_type = input("income/expense: ").strip().lower()

        if transaction_type in ["income", "expense"]:
            break

        print("Invalid type. Please enter income or expense.")

    category = input("category: ").strip()
    title = input("title: ").strip()

    while True:
        try:
            amount = float(input("amount: "))

            if amount > 0:
                break

            print("Amount must be greater than zero.")

        except ValueError:
            print("Invalid amount. Please enter a number.")

    date = input("date: ").strip()
    print("------------------\n")

    transaction = {
        "type": transaction_type,
        "category": category,
        "title": title,
        "amount": amount,
        "date": date
    }

    transactions.append(transaction)
    save_transactions()

from datetime import datetime

def validate_transaction(transaction):
    if not isinstance(transaction, dict):
        return False

    required_fields = ["type", "category", "title", "amount", "date"]

    for field in required_fields:
        if field not in transaction:
            return False

    if transaction["type"] not in ["income", "expense"]:
        return False

    if not isinstance(transaction["category"], str) or not transaction["category"].strip():
        return False

    if not isinstance(transaction["title"], str) or not transaction["title"].strip():
        return False

    amount = transaction["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
        return False

    if not isinstance(transaction["date"], str):
        return False

    try:
        datetime.strptime(transaction["date"], "%Y-%m-%d")
    except ValueError:
        return False

    return True

def add_transaction_with_ai():
    message = input("Describe your transaction: ")

    try:
        tool_name, arguments = ask_llm(message)
    except Exception as error:
        print(f"Could not process the transaction: {error}\n")
        return

    if tool_name == "add_transaction":
        if validate_transaction(arguments):
            transactions.append(arguments)
            save_transactions()
            print("The transaction saved successfully.\n")
        else:
            print("Invalid transaction data!\n")
    else:
        print("The AI returned an unexpected tool.")
        return


def show_summary():
    total_income = 0
    total_expense = 0

    for transaction in transactions:
        if transaction["type"] == "expense":
            total_expense += transaction["amount"]
        elif transaction["type"] == "income":
            total_income += transaction["amount"]

    balance = total_income - total_expense    

    print("\ntotal income: " , total_income)    
    print("total expense: " , total_expense)    
    print("balance: " , balance , "\n")  

def show_transactions():
    if not transactions:
        print("No transactions found.")
        return
    for transaction in transactions:
        print("\ntype: " , transaction["type"])
        print("category: " , transaction["category"])
        print("title: " , transaction["title"])
        print("amount: " , transaction["amount"])
        print("date: " , transaction["date"])
        print("---------------")
        


load_transactions()

while True:
    choice = input("Welcome to my expense tracker:)\nplease select one option:\n1.show transactions list\n2.add a transaction\n3.Add a transaction using AI\n4.show summary\n5.exit\n")

    match choice:
        case "1":
            show_transactions()
        case "2":
            add_transaction()
        case "3":
            add_transaction_with_ai()
        case "4":
            show_summary()
        case "5": 
            break
        case _:
            print("Invalid choice")




    
