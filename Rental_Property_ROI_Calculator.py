import sys, os

class ROIcalc():
    """
    Class to calculate a rental property's potential RIO
    based on user input parameters
    """
    def __init__(self):
        #income attributes 
        self.in_dict = {
            'Rent': None,
            'Laundry': None,
            'Storage': None,
            'Misc' : None,
            }
        self.in_list = []
        self.in_monthly = None

        #expense attributes 
        self.ex_dict = {
            'Mortgage' : None,
            'Taxes': None,
            'Insurance': None,
            'Repair' : None,
            'CapEx': None,
            'Property Managment' : None,
            'Vacancy' : None,
            'Grounds' : None,
            'Electric' : None,
            'Gas' : None,
            'Water' : None,
            'Trash' : None,
            'Misc' : None,
            }
        self.ex_list = []
        self.ex_monthly = None
        self.cashflow_monthly = None
        self.cashflow_annual = None

        #cash on cash return attributes
        self.ccr_dict = {
            'Down Payment' : None,
            'Closing Costs' : None,
            'Rehab Budget' : None,
            'Misc' : None,
            }

        self.total_investment = 0  #initial total invenstment var
        self.ccr = None  #cash on cash return

    def income(self):
        #income parameters collected here
        print("""
Enter anticipated monthly sources of income at these prompts.
(If no income is anticipated enter 0)
                """)

        self.in_dict['Rent'] = int(input("Rent: "))
        self.in_dict['Laundry'] = int(input("Laundry: "))
        self.in_dict['Storage'] = int(input("Storage: "))
        self.in_dict['Misc'] = int(input("Miscellaneous: "))

        for value in self.in_dict.values():  #get income values into a list
            self.in_list.append(value)
        self.in_monthly = sum(self.in_list)  #stores monthly income as a var

        print(f"Your anticipated total monthly income will be ${self.in_monthly:,}\n")

    def expenses(self):
        #expense parameters collected here
        
        print("""
Enter anticipated monthly expenses at these prompts.
(If no income is anticipated enter 0)
                """)

        self.ex_dict['Mortgage'] = int(input("Mortgage: "))
        self.ex_dict['Taxes'] = int(input("Taxes: "))
        self.ex_dict['Insurance'] = int(input("Insurance: "))
        self.ex_dict['Repair'] = int(input("Repair: "))
        self.ex_dict['CapEx'] = int(input("Capital Expenditures: "))
        self.ex_dict['Property Managment'] = int(input("Property Managment: "))
        self.ex_dict['Vacancy'] = int(input("Vacancy: "))
        self.ex_dict['Grounds'] = int(input("Grounds Maintenance: "))
        self.ex_dict['Electric'] = int(input("Electric: "))
        self.ex_dict['Gas'] = int(input("Gas: "))
        self.ex_dict['Water'] = int(input("Water: "))
        self.ex_dict['Trash'] = int(input("Trash: "))
        self.ex_dict['Misc'] = int(input("Miscellaneous: "))

        for value in self.ex_dict.values():  #get expense values into a list
            self.ex_list.append(value)
        self.ex_monthly = sum(self.ex_list)  #stores monthly expenses as a var

        print(f"Your anticipated total monthly expenses will be ${self.ex_monthly:,}\n")


    def cash_flow(self):
        #cash flow projections calculated here
        if not self.in_list:
            print("You must enter expected income before continuing to this step.")
                
        elif not self.ex_list:
            print("You must enter expected expenses before continuing to this step.")

        else:      
            self.cashflow_monthly = self.in_monthly - self.ex_monthly #calcs and stores monthly cashflow
            self.cashflow_annual = self.cashflow_monthly * 12 #calcs and stores annaul cashflow

            print(f"""
Given that your anticipated monthly: 
    Income = ${self.in_monthly:,}
  Expenses = ${self.ex_monthly:,}

Your anticipated cash flow is: 
              ${self.cashflow_monthly:,} monthly
              ${self.cashflow_annual:,} annualy
""")

    def cash_on_cash_return(self):
        if not self.in_list:
            print("You must enter expected income before continuing to this step.")      
        elif not self.ex_list:
            print("You must enter expected expenses before continuing to this step.")
        elif self.cashflow_monthly == None:
            print("You must calculate monthly cashflow before continuing to this step.")
        else:
            print("To calculate your potential Cash-on-Cash Return, I'll need to know a couple more things:")

            self.ccr_dict['Down Payment'] = int(input("Total Down Payment for this property: "))
            self.ccr_dict['Closing Costs'] = int(input("Total Closing Costs: "))
            self.ccr_dict['Rehab Budget'] = int(input("Your immediate rennovation budget: "))
            self.ccr_dict['Misc'] = int(input("Any other miscellaneous purchasing costs: "))

            for value in self.ccr_dict.values():
                self.total_investment += value

            print(f"\nYour total up-front investment on the property will be ${self.total_investment:,}")

            self.ccr = (self.cashflow_annual / self.total_investment) * 100


            print(f"and you anticipated Cash-on-Cash Return will be {self.ccr:.2f}%")

class Main():
    """Class to run the program, instructions, userinput."""

    def __init__(self):
        self.user1 = ROIcalc() #create an instance of ROIcalc to access its methods from Main
        
    def instructions(self):

        print(f"""  
-------  Rental Property ROI Calcuator 1.0 ------- 

    This program will assist you in determining
    if the rental property you are considering
    will be a profitable venture, and if so
    will calcualte your expected rate of return.

Please select from the below options:
    [1] Enter Anticipated Rental Income Variables
    [2] Enter Anticipated Rental Expenses
    [3] Calculate Expected Monthly Cash Flow
    [4] Calculate Expected Cash on Cash Return 
    [5] Quit     
""")
        
    def run(self):
        self.instructions()

        while True:
            option = input("Enter program command number: ")

            if option == '1':
                self.user1.income()
                # os.system ('cls')
            elif option == '2': 
                self.user1.expenses()
            elif option == '3': 
                self.user1.cash_flow()
            elif option == '4': 
                self.user1.cash_on_cash_return()
            elif option == '5':
                print("Good Bye!") 
                break
            else:
                print("That is not an option, please enter again: ")

calculator1 = Main() #create an instance of Main to access Main
calculator1.run()    #actually starts running the program
