class payroll:
    def __init__(self,name,monthly,deduction,bonus):
        self.name = name
        self.monthly = monthly
        self.deduction = deduction
        self.bonus = bonus

    def calulatesal(self):
        total = self.monthly + self.bonus - self.deduction
        #print(total)
        return total
    def function(self):
        print("Name of employee  is: " + self.name)
        print("Monthly salary is: " , self.monthly)
        print("Deduction amount is: " , self.deduction)
        print("Bonus amount is" , self.bonus)
        #total = self.monthly + self.bonus - self.deduction
        total = self.calulatesal()
        print("Total amount: " , total)
if __name__ == "__main__":
    p = payroll("Sarwesh", 30000, 2000 ,200)
    p.calulatesal()
    p.function()
