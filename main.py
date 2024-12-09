#1.budzet
#2.dodavanje troskova
#3.brisanje troskova
#4.logovanje troskova
import json
import sys
from datetime import datetime

user=None
credit=None

with open("data/user.json") as file:
    user = json.load(file)

print(user["budget"]+user["credit"])

user_budget=user["budget"]+user["credit"]

#definirati max budzet, ako korisnik ima veci od max budzet ili manji od 0, ispisati gresku
max_budget=100000
min_budget=0

if user_budget>=max_budget:
    print("Dosegnuli ste limit budzeta")
elif user_budget<=min_budget:
    print("Nemate dovoljan budzet")
    sys.exit()

print(f"dobar dan, vas budzet i credit zajedno iznosi {user_budget}")

expense = 0
while expense <=0 or expense > user_budget:
    expense = int(input("Molim vas unesite iznos troska"))

#napraviti textualni file koji se zove "expense_log.txt"
#upisati svaki trosak u sledecem formatu
#"amount:cifra_expense, user:id, dateTime:9.12.2024 22:44, budzet: trenutni budzet, preostali budzet"

with open("logs/expense_log.txt","a") as file:
    remaining_budget=user_budget-expense
    message= (f"\nAmount: {expense}, "
              f"User:{user["id"]}, "
              f"Budget:{user_budget}, "
              f"Preostali budget:{remaining_budget},"
              f"DateTime: {datetime.now()}")

    file.write(message)