# Tax calculator - input : CTC, HRA, RENT, EPF, 80C ; output : BASIC, GROSS, TAX, TAXABLE INCOME, HAND-IN SALARY
# Missing features : adding new employees or user and storing their data, optimized code class features,
#                    getting details of one user (after storing data in objects), Exceptions handling
# Reference : https://www.naukri.com/blog/salary-and-its-components/
class TaxCalculator:
    std_deduction = 50000

    def __init__(self):
        while True:
            print("\n T A X   C A L C U L A T O R \n")
            self.age_group = int(input('''Enter your age group:
                    1 - Less than 60 years
                    2 - Between 60 and 80 years (Senior Citizen)
                    3 - More than 80 years (Super Senior Citizen) 
                    Your Choice :   '''))
            if self.age_group > 3 or self.age_group < 0:
                print("Invalid Choice")
                break
            else:
                self.income()
                self.hra()
                self.deductions_cal()
                self.tax_calculate()
                self.print_tax()
                while True:
                    choice = int(input('''Press 1 to Calculate again\nPress 2 to Exit '''))
                    if choice == 1:
                        break
                    elif choice == 2:
                        self.exit_calculator()
                    else:
                        print("Invalid Choice")
                        continue

    def hra(self):
        print("HRA : ")
        print("--------------------------------------------------------------")
        self.hra_recieved = int(input("\tEnter HRA recieved per annum : "))
        self.rent = int(input("\tEnter Total Rent paid per annum : "))
        self.city = int(input('''\tAre you from Metropolitan City ? :
                                    Press 1 for YES 
                                    Press 2 for NO
                                    Your Choice : '''))
        print("\n")
        # HRA can be claimed in three ways
        # 1. Rent - 10% of basic
        # 2. Actual HRA
        # 3. 50% or 40% of basic
        # Select lowest one
        self.hra_1 = self.rent - 0.1 * self.basic
        self.hra_2 = self.hra_recieved
        if self.city == 1:
            self.hra_3 = 0.5 * self.basic
        else:
            self.hra_3 = 0.4 * self.basic
        self.min_hra = int(min(self.hra_1, self.hra_2, self.hra_3))
        if self.min_hra == self.hra_recieved:
            self.taxable_hra = self.hra_recieved
        else:
            self.taxable_hra = self.min_hra

    def deductions_cal(self):
        print("DEDUCTIONS : ")
        print("--------------------------------------------------------------")
        # taking only EPF and Investments under 80C
        self.EPF = int(input("\tEnter EPF : "))
        self.i80C = int(input("\tEnter Investments under 80C : "))
        print("\n")
        if self.EPF + self.i80C >= 150000:  # max allowance is 1.5 lakhs
            self.deductions = 150000
        else:
            self.deductions = self.EPF + self.i80C

    def income(self):
        print("INCOME : ")
        print("--------------------------------------------------------------")
        self.ctc = int(input("\tEnter your CTC : "))
        print("\n")
        self.basic = int(0.4 * self.ctc)

    def tax_calculate(self):
        # gross salary = ctc - (EPF + gratuity)
        # there is no gratuity
        self.gross_salary = self.ctc - self.EPF
        # calculating total taxable income (also known as Gross Taxable income)
        # Taxable Income = Gross Salary – Section 80C deduction – Standard Deduction – HRA – Professional Tax
        # There is no professional tax
        self.taxable_income = self.gross_salary - self.i80C - TaxCalculator.std_deduction - self.taxable_hra
        # Calculating Tax
        # on the basis of age group
        if self.age_group == 1:
            # Tax Slab for < 60 yrs
            if self.taxable_income < 250000:
                self.final_tax = 0
            elif 250000 < self.taxable_income < 500000:
                self.tax = 0.05 * (self.taxable_income - 250000)
                self.final_tax = int(self.tax + (0.04 * self.tax))
            elif 500000 < self.taxable_income < 1000000:
                self.tax = 12500 + (0.2 * (self.taxable_income - 500000))
                self.final_tax = int(self.tax + (0.04 * self.tax))
            elif self.taxable_income > 1000000:
                self.tax = 112500 + (0.3 * (self.taxable_income - 1000000))
                self.final_tax = int(self.tax + (0.04 * self.tax))

        elif self.age_group == 2:
            # Tax slab for 60 < age < 80
            if self.taxable_income < 300000:
                self.final_tax = 0
            elif 300000 < self.taxable_income < 500000:
                self.tax = 0.05 * (self.taxable_income - 300000)
                self.final_tax = int(self.tax + (0.04 * self.tax))
            elif 500000 < self.taxable_income < 1000000:
                self.tax = 10000 + (0.2 * (self.taxable_income - 500000))
                self.final_tax = int(self.tax + (0.04 * self.tax))
            elif self.taxable_income > 1000000:
                self.tax = 110000 + (0.3 * (self.taxable_income - 1000000))
                self.final_tax = int(self.tax + (0.04 * self.tax))

        elif self.age_group == 3:
            # Tax slab for > 80
            if self.taxable_income < 500000:
                self.final_tax = 0
            elif 500000 < self.taxable_income < 1000000:
                self.tax = int(0.2 * (self.taxable_income - 500000))
                self.final_tax = int(self.tax + (0.04 * self.tax))
            elif self.taxable_income > 1000000:
                self.tax = 100000 + (0.3 * (self.taxable_income - 1000000))
                self.final_tax = int(self.tax + (0.04 * self.tax))

    def print_tax(self):
        print("FINAL REPORT : ")
        print("--------------------------------------------------------------")
        print("\t\tBASIC INCOME : ", self.basic)
        print("\t\tGROSS SALARY:", self.gross_salary)
        print("\t\tHRA EXEMPTION : ", self.taxable_hra)
        print("\t\tTAXABLE INCOME : ", self.taxable_income)
        print("\t\tT A X : ", int(self.final_tax))
        # Take Home Salary = Gross Salary – (Income Tax + Professional Tax)
        print("\t\tTAKE-HOME SALARY : ", self.gross_salary - self.final_tax)
        print("\n")

    def user_details(self):
        print("\t\tAGE GROUP", end="")
        if self.age_group == 1:
            print("Less than 60 years")
        elif self.age_group == 2:
            print("Between 60 and 80 years")
        elif self.age_group == 3:
            print("More than 80 years")
        print("\t\tCTC : ", self.ctc)
        print("\t\tBASIC INCOME : ", self.basic)
        print("\t\tEPF : ", self.EPF)
        print("\t\t80C : ", self.i80C)
        print("\t\tGROSS SALARY : ", self.gross_salary)
        print("\t\tHRA EXEMPTION : ", self.taxable_hra)
        print("\t\tTAXABLE INCOME : ", self.taxable_income)
        print("\t\tT A X : ", int(self.final_tax))
        # Take Home Salary = Gross Salary – (Income Tax + Professional Tax)
        print("\t\tTAKE-HOME SALARY : ", self.gross_salary - self.final_tax)

    def exit_calculator(self):
        exit()


emp_1 = TaxCalculator()
