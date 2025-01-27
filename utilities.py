import matplotlib.pyplot as plt
import numpy as np

class fin_plan:
    def __init__(self, income, IA_or_IL, savingsgoal):
        """User must enter their yearly income, state and savings goal.

        Assumptions: Income is yearly incomr before tax and the state is either IA or IL.
        Savings goals is desired retirement income per year.

        In order to create a budget, run the after tax form, then budget"""

        self.income = income
        self.IA_or_IL = IA_or_IL
        self.after_tax_inc = 0 #setting equal to income incase they want their budget created on their income before taxes
        self.f=0 #fixed expenses
        self.d=0 #discretionary expenses
        self.s=0  #savings
        self.expenses_list = []
        self.savingsgoal = savingsgoal

    def after_tax(self):
        """
        Assumptions: The user is either from Iowa or Illinois. The tax rate come from 2019 tax year.

        Computes the user's income after federal income taxes, state income taxes and FICA taxes.

        Returns the user's after-tax income.
        """

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

        if self.IA_or_IL == 'IA' or self.IA_or_IL == 'Iowa':
             #computing the max state tax brackets for iowa
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
        elif self.IA_or_IL == 'IL' or self.IA_or_IL == 'Illinois':
            sttax = self.income *.0495
        else:
            print("Please enter either Iowa (IA) or Illinois (IL).")
        self.after_tax_inc = self.income - fedtax - sttax  -(self.income*.0765)#reassigning the after-tax income variable
        print(f'Your after-tax income is ${self.after_tax_inc:.2f}!')
        return f'{self.after_tax_inc:.2f}'

    def budget(self):
        """
        Assumptions: The fuction computes after-tax income based on their after-tax income.
        Fixed expenses should be 50% of income. Discretionary should be 30%.
        Savings should be 20% of income.

        Generates a pie chart with the amount the user ca spent on a monthly basis.

        Returns the user's budgeted fixed, discretionary and savings based on after-tax income.
        """
        income=self.after_tax_inc
        if income ==0:
            print("Please run the after-tax function first.")
        else:
            labels = 'Fixed Expenses', 'Discretionary Expenses','Savings'
            self.f=((income)*.50)/12 #fixed
            self.d=((income)*.3)/12 #discretionary
            self.s=((income)*.2)/12 #savings
            values = [self.f,self.d,self.s]
            colors = ['#627798', '#E3E8FC', '#6C7CCC']
            explode = (.05, .05, .05)

            #Adding two labels (monthly amount, percentage of monthly income) to each slice of the pie chart
            def make_autopct(values):
                def my_autopct(pct):
                    total = sum(values)
                    val = int(round(pct*total/100.0))
                    return '${v:d}  ({p:.0f}%)'.format(p=pct,v=val)
                return my_autopct

            #plotting the pie chart and adding legend, and title
            plt.pie(values, explode=explode, colors=colors, textprops={'color':"black"},autopct=make_autopct(values), shadow=True, startangle=90,)
            plt.legend(labels, loc='lower right')
            plt.axis('equal')
            plt.title('Monthly Budget')
            plt.show()
            print( f'You should dedicate ${self.f:.0f} of your monthly income to fixed expenses, such as: rent, debt payments, groceries, car payments, utilities and other mandatory payments.')
            print(f'You should dedicate ${self.d:.0f} of your monthly income to your discretionary expenses, such as: eating at restuarants, coffee, clothes shopping or other purchases that are not mandatory.')
            print(f'You should dedicate ${self.s:.0f} of your monthly income to savings.') #returns amount for fixed expenses, discretionary expense, and savings

            return (self.f, self.d, self.s)

    def expenses(self):
        """
        This allows the user to input their monthly expenses through a series of questions.
        The answers are saved in a list.

        Returns list of expenses entered by the user.
        """
        #appends the list to add the expense added by the user
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


    def savings_goal(self):
        """
        Assumptions: The retiree will retire at the age of 60.
        The retiree will will be invested in bonds during retirement that yield on average 5% return.
        Preretirement the user will primarily be more invested in stocks and will return on average 8%.
        Savings come from the 20% of after-tax income generated in the budget.

        Returns whether is the user is on-target or not to save their desired level of income.
        """
        retirement_income = self.savingsgoal
        if self.s ==0:
            print("Please run after-tax and budget first.")
        else:
            years_of_savings = 38 #graduate at 22 years old. can start using 401k at 59.5 years.
            amount_saved = self.s * 12 #yearly saved for retirement
            fv_retirementincome = retirement_income*(1+.03)**years_of_savings #future value of desired retirement income. Assume average inflation of 3%
            nestegg = (fv_retirementincome/(.05-.03))*(1-((1+.03)**20)/((1+.05)**20)) #total amount needed when stepping into retirement if alive for 20 years.
            neccesary_savingsperyear = (nestegg/(((1+.08)**years_of_savings)-((1+.02)**years_of_savings))*(.08-.02))
            on_target = amount_saved - neccesary_savingsperyear 
            if on_target > 0:
                print(f"You are on-target to meet your savings goal. You are saving ${on_target:.2f} more per year than you need.")
            else:
                print(f"You are not on-target to meet your savings goal. You need to save ${-on_target:.2f} more per year.")
            return f"On-Target By (Off-Target):{on_target:.2f}"

    def bud_vs_act(self):
        """
        Assumptions: Actual expenses are added in expenses function.
        Budgeted are generated in the budget.

        The function compares the user's budgeted expenses versus what they actually spent.

        Generates a bar graph comparing budgeted to actual.

        Returns
        """
        actual_fixed_expenses = self.expenses_list[0][1] + self.expenses_list[1][1] + self.expenses_list[2][1] + self.expenses_list[3][1]
        actual_discretionary_expense = self.expenses_list[4][1] + self.expenses_list[5][1] + self.expenses_list[6][1]
        fixed_expenses = self.f
        discretionary_expenses = self.d
        fig, ax = plt.subplots()

        #actual expenses are graphed
        ax.bar(np.arange(2), (actual_fixed_expenses,actual_discretionary_expense), 0.35, alpha=0.8, color='#CC5227',label='Actual')
        #budgeted expenses are graphed
        ax.bar(np.arange(2) + 0.35, (fixed_expenses,discretionary_expenses), 0.35, alpha=0.8,color='#627798',label='Budget')
        #creating legend, title and axis labels
        ax.set_ylabel('Dollar Per Month($)')
        ax.set_title('Budget Versus Actual Expense')
        ax.set_xticks(np.arange(2) + 0.35)
        ax.set_xticklabels(['Fixed Expenses', 'Discretionary Expenses'])
        ax.legend()
        return (actual_fixed_expenses, actual_discretionary_expense)
