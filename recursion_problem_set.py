'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.

def personal_investment(money, month, index):
    money += money * (0.20/12)
    index += 1
    if index < month:
        personal_investment(money, month, index)
    else:
        print("After", month, "months, your balance is: ", money)

personal_investment(10000, 6, 0)

#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.

def personal_investment2(money, month, index):
    money += money * (0.2/12)
    money -= 100
    index += 1
    if index < month:
        personal_investment2(money, month, index)
    else:
        print("After", month, "months, you balance is: ", money)

personal_investment2(5000, 36, 0)


#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.
'''
def personal_investment3(money, month, index, payed):
    money += money * (0.2/12)
    money -= 100
    index += 1
    if money <= 0:
        payed = True
        print("You payed it off in", month, "months")


personal_investment3(10000, months, 0, False)
'''

#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.
'''
def pyramid(height, boxes, row):
    if row == 0:
        #boxes = 0
    boxes += height
    if height != 0:
        pyramid(height-1, boxes, index + 1)
    else:
        print("There are", boxes, "boxes")

pyramid(int(input("Enter a positive, whole value: ")), 0, 0)
'''