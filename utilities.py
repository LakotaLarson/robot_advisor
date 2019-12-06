
class fin_plan:
    def __init__(self, savingsgoal, riskappetite):
        self.income = 0
        self.expenses = 0
        self.expenses_list = []
        self.expense_name = []
        self.savingsgoal = savingsgoal
        self.riskappetite = riskappetite

    def after_tax(self, income):
        self.income = income
        maxfed1 = 9700*.10
        maxfed2 = maxfed1 + 39475*.12
        maxfed3 = maxfed2 + 84200*.22
        maxfed4 = maxfed3 + 160725*.24
        maxfed5 = maxfed4 + 204100*.32
        maxfed6 = maxfed5 + 510300*.35
        if income <= 9700:
            fedtax = income*.10
        elif income <= 39475:
            fedtax = (income-9700)*.12 + maxfed1
        elif income <= 84200:
            fedtax = (income-39475)*.22 + maxfed2
        elif income <= 160725:
            fedtax = (income-84200)*.24 + maxfed3
        elif income <= 204100:
            fedtax = (income-160725)*.32 + maxfed4
        elif income <= 510300:
            fedtax = (income-204100)*.35 + maxfed5
        else:
            fedtax = (income-510300)*.37 + maxfed6
        maxst1 = 1598*.0036
        maxst2 = maxst1 + 3196*.0243
        maxst3 = maxst2 + 6392*.045
        maxst4 = maxst3 + 14382*.0612
        maxst5 = maxst4 + 23970*.0648
        maxst6 = maxst5 + 31960*.068
        maxst7 = maxst6 + 47940*.0792
        if income <= 1598:
            sttax = income*.0036
        elif income <= 3196:
            sttax = (income-1598)*.0243 + maxst1
        elif income <= 6392:
            sttax = (income-3196)*.045 + maxst2
        elif income <= 14382:
            sttax = (income-6392)*.0612 + maxst3
        elif income <= 23970:
            sttax = (income-14382)*.0648 + maxst4
        elif income <= 31960:
            sttax = (income-23970)*.068 + maxst5
        elif income <= 47940:
            sttax = (income-31960)*.0792 + maxst6
        else:
            sttax = (income-71910)*.0898 + maxst7
        after_tax = income -fedtax - sttax
        return(after_tax)

p=fin_plan(200000,'x')
p.after_tax(75000)