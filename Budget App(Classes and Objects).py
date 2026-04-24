class Category:

    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({
            'amount': amount,
            'description': description
            })

    def withdraw(self, amount, description=""):
        if self.get_balance() >= amount:
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True  
        return False

    def get_balance(self):
        balance = 0
        for purchase in self.ledger:
            balance += purchase["amount"]
        return balance

    def transfer(self, amount, purchase_category):
        self.withdraw(amount, f"Transfer to {purchase_category.name}")
        purchase_category.deposit(amount, f"Transfer from {self.name}")
        if amount <= self.get_balance():
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        title = f"{self.name:*^30}"
        items = ""
        
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}" 
            amt = amt[:7]  
            items += f"{desc:<23}{amt:>7}\n" 
        
        total = f"Total: {self.get_balance():.2f}" 
        return f"{title}\n{items}{total}"



def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    spending = []
    total_spent = 0

    for cat in categories:
        cat_spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spending.append(cat_spent)
        total_spent += cat_spent

    percentages = [int((amount / total_spent) * 100 // 10 * 10) for amount in spending]
    chart_rows = []

    for i in range(100, -1, -10):
        row = f"{i:>3}|"
        for perc in percentages:
            row += " o " if perc >= i else "   "
        row += " "
        chart_rows.append(row)

    chart = "\n".join(chart_rows)
    chart += "\n    " + "-" * (len(categories) * 3 + 1)
    max_len = max(len(cat.name) for cat in categories)
    name_rows = []

    for i in range(max_len):
        row = "     "
        for cat in categories:
            if i < len(cat.name):
                row += cat.name[i] + "  "
            else:
                row += "   "
        name_rows.append(row)

    chart += "\n" + "\n".join(name_rows)

    return title + chart