import matplotlib.pyplot as plt

class fin_plan:
    def __init__(self, income, savingsgoal):
        self.income = income
        self.after_tax_inc = 0
        self.expenses_list = []
        self.savingsgoal = savingsgoal

    def after_tax(self):
        "This function computes the user's income after federal income taxes and state income taxes. Assuming: The user is from Iowa."
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
        self.after_tax_inc = self.income - fedtax - sttax
        return self.after_tax_inc

    def budget(self):
        "This computes the users budget using their after-tax income."
        income=self.after_tax_inc
        labels = 'Fixed Expenses', 'Discretionary Expenses','Savings'
        f=((income)*.50)
        d=((income)*.3)
        s=((income)*.2)
        values = [f,d,s]
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
        print(f'You should dedicate ${f:.0f} of your monthly income to fixed expenses, such as: rent, debt payments, groceries, car payments, utilities and other mandatory payments.')
        print(f'You should dedicate ${d:.0f} of your monthly income to your discretionary expenses, such as: eating at restuarants, coffee, clothes shopping or other purchases that are not mandatory.')
        print(f'You should dedicate ${s:.0f} of your monthly income to savings.')
        return (f,d,s)

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

p=fin_plan(100000, 200000)
p.after_tax()
#p.expenses()
p.budget()
