from utilities import fin_plan
p=fin_plan(75000, 'IL', 60000)
#p.expenses()
print(p.after_tax())
print(p.budget())
print(p.savings_goal())