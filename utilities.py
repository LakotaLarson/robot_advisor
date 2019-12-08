import matplotlib.pyplot as plt
import numpy as np

class fin_plan:
    def __init__(self, income, IA_or_IL, savingsgoal):
        "User must enter their yearly income and savings goal. In order to create a budget, run the after tax form, then budget"
        self.income = income
        self.IA_or_IL = IA_or_IL
        self.after_tax_inc = 0 #setting equal to income incase they want their budget created on their income before taxes
        self.f=0
        self.d=0
        self.s=0
        self.expenses_list = []
        self.savingsgoal = savingsgoal

    def after_tax(self):
        "This function computes the user's income after federal income taxes and state income taxes. Assuming: The user is from Iowa."
        #computing the max federal tax brackets
        maxfed1 = 9700*.10
        maxfed2 = maxfed1 + 39475*.12
        maxfed3 = maxfed2 + 84200*.22
        maxfed4 = maxfed3 + 160725*.24
        maxfed5 = maxfed4 + 204100*.32
        maxfed6 = maxfed5 + 510300*.35
        if self.income <= 9700:
            fedtax = self.income*.10
        elif self.income <= 39475:
            fedtax = (self.income-9700)*.12 + maxfed1
        elif self.income <= 84200:
            fedtax = (self.income-39475)*.22 + maxfed2
        elif self.income <= 160725:
            fedtax = (self.income-84200)*.24 + maxfed3
        elif self.income <= 204100:
            fedtax = (self.income-160725)*.32 + maxfed4
        elif self.income <= 510300:
            fedtax = (self.income-204100)*.35 + maxfed5
        else:
            fedtax = (self.income-510300)*.37 + maxfed6
        #computing the max state tax brackets
        if self.IA_or_IL == 'IA':
            maxst1 = 1598*.0036
            maxst2 = maxst1 + 3196*.0243
            maxst3 = maxst2 + 6392*.045
            maxst4 = maxst3 + 14382*.0612
            maxst5 = maxst4 + 23970*.0648
            maxst6 = maxst5 + 31960*.068
            maxst7 = maxst6 + 47940*.0792
            if self.income <= 1598:
                sttax = self.income*.0036
            elif self.income <= 3196:
                sttax = (self.income-1598)*.0243 + maxst1
            elif self.income <= 6392:
                sttax = (self.income-3196)*.045 + maxst2
            elif self.income <= 14382:
                sttax = (self.income-6392)*.0612 + maxst3
            elif self.income <= 23970:
                sttax = (self.income-14382)*.0648 + maxst4
            elif self.income <= 31960:
                sttax = (self.income-23970)*.068 + maxst5
            elif self.income <= 47940:
                sttax = (self.income-31960)*.0792 + maxst6
            else:
                sttax = (self.income-71910)*.0898 + maxst7
        else:
            sttax = self.income *.0495
        self.after_tax_inc = self.income - fedtax - sttax #reassigning the after-tax income variable
        return f'Your after-tax income is {self.after_tax_inc:.2f}!'

    def budget(self):
        "This computes the users budget using their income. The user must run the after-tax function first."
        income=self.after_tax_inc
        if income ==0:
            print("Please run the after-tax function first.")
        else:
            labels = 'Fixed Expenses', 'Discretionary Expenses','Savings'
            self.f=((income)*.50)/12
            self.d=((income)*.3)/12
            self.s=((income)*.2)/12
            values = [self.f,self.d,self.s]
            colors = ['#627798', '#E3E8FC', '#6C7CCC']
            explode = (.05, .05, .05)
            def make_autopct(values): 
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return '${v:d}  ({p:.0f}%)'.format(p=pct,v=val)
                return my_autopct
            plt.pie(values, explode=explode, colors=colors, textprops={'color':"black"},autopct=make_autopct(values), shadow=True, startangle=90,)
            plt.legend(labels, loc='lower right')
            plt.axis('equal')
            plt.title('Monthly Budget')
            plt.show()
            return f'You should dedicate ${self.f:.0f} of your monthly income to fixed expenses, such as: rent, debt payments, groceries, car payments, utilities and other mandatory payments. You should dedicate ${self.d:.0f} of your monthly income to your discretionary expenses, such as: eating at restuarants, coffee, clothes shopping or other purchases that are not mandatory. You should dedicate ${self.s:.0f} of your monthly income to savings.' #returns amount for fixed expenses, discretionary expense, and savings

    def expenses(self):
        "This allows the user to input their monthly expenses through a series of questions"
        rent = int(input('Enter amount spent on rent a month: '))
        self.expenses_list.append(('rent', rent))

        utilities = int(input('Enter amount spent on utilities a month: '))
        self.expenses_list.append(('utilities', utilities))

        car_pymt = int(input('Enter amount spent on a car payment a month: '))
        self.expenses_list.append(('car', car_pymt))

        groceries = int(input('Enter amount spent on groceries a month: '))
        self.expenses_list.append(('groceries', groceries))

        eating_out = int(input('Enter amount spent on eating out a month: '))
        self.expenses_list.append(('eating_out', eating_out))

        shopping = int(input('Enter amount spent on shopping a month: '))
        self.expenses_list.append(('shopping', shopping))

        other = int(input('Enter other amounts that you spend a month: '))
        self.expenses_list.append(('other', other))

        return(self.expenses_list)
        
    #Assumptions: The retiree will retire at the age of 60. The retiree will will be invested in bonds during retirement that yield on average 5% return.
    #Preretirement the user will primarily be more invested in stocks and will return on average 8%
    def savings_goal(self):
        retirement_income = self.savingsgoal
        if self.s ==0:
            print("Please run after-tax and budget first.")
        else:
            years_of_savings = 38
            amount_saved = self.s * 12
            fv_retirementincome = retirement_income*(1+.03)**years_of_savings
            nestegg = (fv_retirementincome/(.05-.03))*(1-((1+.03)**20)/((1+.05)**20))
            neccesary_savingsperyear = (nestegg/(((1+.08)**years_of_savings)-((1+.02)**years_of_savings))*(.08-.02))
            on_target = amount_saved - neccesary_savingsperyear
            if on_target > 0:
                print(f"You are on-target to meet your savings goal. You are saving ${on_target:.2f} more per year than you need.")
            else:
                print(f"You are not on-target to meet your savings goal. You need to save ${-on_target:.2f} more per year.")
            return f"On-Target By (Off-Target):{on_target:.2f}"
        
    def bud_vs_act(self):
        "This compares the user's budget versus what they actually spend."
        actual_fixed_expenses = self.expenses_list[0][1] + self.expenses_list[1][1] + self.expenses_list[2][1] + self.expenses_list[3][1]
        actual_discretionary_expense = self.expenses_list[4][1] + self.expenses_list[5][1] + self.expenses_list[6][1]
        fixed_expenses = self.f
        discretionary_expenses = self.d
        fig, ax = plt.subplots()
        actual=ax.bar(np.arange(2), (actual_fixed_expenses,actual_discretionary_expense), 0.35, alpha=0.8, color='b',label='Actual')
    
        budget=ax.bar(np.arange(2) + 0.35, (fixed_expenses,discretionary_expenses), 0.35, alpha=0.8,color='g',label='Budget')

        ax.set_ylabel('Dollar Per Month($)')
        ax.set_title('Budget Versus Actual Expense')
        ax.set_xticks(np.arange(2) + 0.35)
        ax.set_xticklabels(['Fixed Expenses', 'Discretionary Expenses'])
        ax.legend()
    