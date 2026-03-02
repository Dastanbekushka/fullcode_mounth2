from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet
import datetime


def create_receipt_pdf(balance, amount, operasia):
    filename = f"receipt_{operasia}.pdf"
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [
        Paragraph("<b>BANK RECEIPT</b>", styles["Title"]),
        Spacer(1, 12),
        Paragraph(f"Operation: {operasia}", styles["Normal"]),
        Paragraph(f"Amount: {amount}", styles["Normal"]),
        Paragraph(f"Current Balance: {balance}", styles["Normal"]),
        Paragraph(f"Date: {now}", styles["Normal"]),
    ]

    doc.build(content)

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Вы ввели недостаточное средство!")
            return

        self.balance += amount
        self.history.append({
            "type": "deposit",
            "date": datetime.datetime.now(),
            "amount": amount
        })
        create_receipt_pdf(self.balance, amount, "deposit")

    def withdraw(self, amount):
        if amount <= 0:
            print("Вы ввели недостаточное средство!")
            return
        elif amount > self.balance:
            print("Недостаточно средств!")
            return

        self.balance -= amount
        self.history.append({
            "type": "withdraw",
            "date": datetime.datetime.now(),
            "amount": amount
        })
        create_receipt_pdf(self.balance, amount, "withdraw")

    def get_history(self):
        result = ''
        for i in self.history:
            result += f"{i['type']}: {i['date']}, amount:{i['amount']}\n"
        return result

    def __str__(self):
        return f"name: {self.name}, balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.balance += interest
        self.history.append({
            "type": "deposit",
            "date": datetime.datetime.now(),
            "amount": interest
        })
        create_receipt_pdf(self.balance, interest, "interest")

    def __str__(self):
        return f"name: {self.name}, balance: {self.balance} interest rate: {self.interest_rate}"

user1 = Account("Dastan", 10000)
user1.deposit(100)
user1.withdraw(50)
print(user1.get_history())
print(user1)
user2 = SavingsAccount("Ilim", 10000, 2)
user2.deposit(100)
user2.withdraw(50)
print(user2.get_history())
user2.add_interest()
print(user2)

account = [user1,user2]
for i in account:
    print(i)
