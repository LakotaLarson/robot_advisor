#robot_advisor

Requirements : matplotlib

Overview : As graduation approaches, we will be stepping into the real world. We understand the importance of a proper budget. After looking into the financial advisor sector, we found that people are more comfortable receiving advice from a robot than a financial advisor. As a result of this discovery we will be creating a robot advisor that ask the client a series of financial questions and their financial goals. We will give them a personalized budget and suggestions on where they should be allocating their money to receive their required return to meet their retirement needs.  

Class : Budget
Function 1 : __init__  
Initialize the ‘budget’ class. The class will include yearly income, expenses, savings goal and risk appetite.

Function 2: after_tax  
The function will begin with asking the user to input their yearly income. After the user inputs their yearly income, the income will flow through a series of if/if else statements the function to compute the user’s tax expenses. The function will return their after-tax income (including both state and federal income tax. (Assumption: the user resides in Iowa and pays state taxes in Iowa.)  

Function 3: expenses
The function will ask the user about their spending habits. The function will ask the user how much the spend on fixed expenses a month. The function will then ask for amount spent on discretionary expenses on a monthly basis.  

Function 4: create_budget
The function will return a pie chart using matplotlib to display how the user should be allocating their money. The allocation will be separated in a variety of areas such as fixed expenses, discretionary spending, saving etc.  

Function 5: saving_goal
The function will ask the user to input their savings goal and risk appetite. Their saving goal will be their total retirement goal. We will then estimate, depending on the amount the user anticipates saving, what type of financial product the user should be investing in.  

Function 6: bud_vs_act
The function will compare budget vs their actual spending using matplotlib.

Troubleshooting:

Commands

When you start working on the project:
1. cd Desktop/
2. cd robot_advisor
3. git pull origin master


When you have made a change that you want to save:
1. git add .
2. git commit -m"insert message here"
3. git push origin master
