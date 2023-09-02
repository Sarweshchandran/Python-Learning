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
        print("\n Name of employee  is: " + self.name)
        print("Monthly salary is: " , self.monthly)
        print("Deduction amount is: " , self.deduction)
        print("Bonus amount is" , self.bonus)
        #total = self.monthly + self.bonus - self.deduction
        total = self.calulatesal()
        print("Total amount: " , total)
if __name__ == "__main__":
    #p = payroll("Sarwesh", 30000, 2000 ,200)
    #p.calulatesal()
    name = input("Enter the Name of Employee:")
    monthly = int(input("Enter the monthly salary: "))
    deduction = int(input("Enter the deduction amount: "))
    bonus = int(input("Enter the Bonus Amount: "))
    p = payroll(name, monthly, deduction, bonus)
    #p.calulatesal()
    p.function()
