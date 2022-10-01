"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contracts_no=0, contract_rate=0, bonus_commission=0):
        self.name = name
        self.contracts_no = contracts_no
        self.contract_rate = contract_rate
        self.bonus_commission = bonus_commission


    def get_pay(self):
        total_pay = 0
        if self.contracts_no != 0:
            total_pay += self.contracts_no * self.contract_rate
        if self.bonus_commission != 0:
            total_pay += self.bonus_commission
        return total_pay

    def __str__(self):
        text = ""
        if self.contracts_no != 0:
            text2 = f' and receives a commission for {self.contracts_no} contract(s) at {self.contract_rate}/contract.'
        elif self.bonus_commission != 0:
            text2 = f' and receives a bonus commission of {self.bonus_commission}.'
        else:
            text2 = "."
        text = text + text2
        return text

class Monthly_Employee(Employee):
    def __init__(self, name, salary, contracts_no=0, contract_rate=0, bonus_commission=0):
        super().__init__( name, contracts_no, contract_rate, bonus_commission)
        self.salary = salary
    
    def get_pay(self):
        total_pay = super().get_pay()
        total_pay += self.salary
        return total_pay

    def __str__(self):
        # Billie works on a monthly salary of 4000.  Their total pay is 4000.
        # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
        text = f'{self.name} works on a monthly salary of {self.salary}'
        text2 =  super().__str__()
        text3 = f'  Their total pay is {self.get_pay()}.'
        text = text + text2 + text3
        # print(text)
        return text

class Hourly_Employee(Employee):
    def __init__(self, name, hours, hourly_rate, contracts_no=0, contract_rate=0, bonus_commission=0):
        super().__init__(name, contracts_no, contract_rate, bonus_commission)
        self.hours = hours
        self.hourly_rate = hourly_rate
        

    def get_pay(self):
        total_pay = super().get_pay()
        total_pay += self.hours * self.hourly_rate
        return total_pay

    def __str__(self):
        # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
        text = f'{self.name} works on a contract of {self.hours} hours at {self.hourly_rate}/hour'
        text2 = super().__str__()
        text3 = (f'  Their total pay is {self.get_pay()}.')
        text = text + text2 + text3
        # print(text)
        return text


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Monthly_Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Employee('Charlie', hours=100, hourly_rate=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Monthly_Employee('Renee', salary=3000, contract_rate=200, contracts_no=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Employee('Jan', hours=150, hourly_rate=25, contracts_no=3, contract_rate=220)


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Monthly_Employee('Robbie', salary = 2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Employee('Ariel', hours=120, hourly_rate=30, bonus_commission=600)