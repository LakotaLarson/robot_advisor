from utilities import fin_plan
p=fin_plan(75000, 'IL', 60000)
#p.expenses()
after_tax= (p.after_tax())
print(p.budget(after_tax))
print(p.savings_goal())
print(p.expenses())
print(p.bud_vs_act())
