import random
import json
import sys





data = 0
with open('./training_data/data.txt') as json_data:
    data = json.load(json_data)

targets = 0
with open('./training_data/targets.txt') as json_data:
    targets = json.load(json_data)


#0 rated people
def saver_big_months(num):
    MI = data[num][0];
    ME = data[num][1];
    TI = data[num][2];
    RCS = data[num][3];
    Age = data[num][4];
    TA = data[num][5];
    price = 10000;


    yearly_income = []

    for i in range (0,11):
        monthly_income = MI + (random.randint(-1,1) * (MI/100))
        monthly_expenditure = (random.randint(7,9)*0.1) * monthly_income
        TI += ( monthly_income - ((random.randint(3,45)*0.01) * monthly_income)) - monthly_expenditure
        yearly_income.append([monthly_income,monthly_expenditure,TI]);

    return yearly_income

#1 rated people
def saver_small_months(num):
    MI = data[num][0];
    ME = data[num][1];
    TI = data[num][2];
    RCS = data[num][3];
    Age = data[num][4];
    TA = data[num][5];
    price = 10000;


    yearly_income = []

    for i in range (0,11):
        monthly_income = MI + (random.randint(-1,1) * (MI/100))
        monthly_expenditure = (random.randint(1,3)*0.1) * monthly_income
        TI += ( monthly_income - ((random.randint(3,8)*0.01) * monthly_income)) - monthly_expenditure
        yearly_income.append([monthly_income,monthly_expenditure,TI]);

    return yearly_income

#2 rated people
def poor_big_months(num):
    MI = data[num][0];
    ME = data[num][1];
    TI = data[num][2];
    RCS = data[num][3];
    Age = data[num][4];
    TA = data[num][5];
    price = 10000;


    yearly_income = []

    for i in range (0,11):
        monthly_income = MI + (random.randint(-1,1) * (MI/100))
        monthly_expenditure = (random.randint(8,11)*0.1) * monthly_income
        TI += ( monthly_income - ((random.randint(50,70)*0.01) * monthly_income)) - monthly_expenditure
        yearly_income.append([monthly_income,monthly_expenditure,TI]);

    return yearly_income

#3 rated people
def average_months(num):
    MI = data[num][0];
    ME = data[num][1];
    TI = data[num][2];
    RCS = data[num][3];
    Age = data[num][4];
    TA = data[num][5];
    price = 10000;


    yearly_income = []

    for i in range (0,11):
        monthly_income = MI + (random.randint(-1,1) * (MI/100))
        monthly_expenditure = (random.randint(4,7)*0.1) * monthly_income
        TI += ( monthly_income - ((random.randint(15,35)*0.01) * monthly_income)) - monthly_expenditure
        yearly_income.append([monthly_income,monthly_expenditure,TI]);

    return yearly_income

def main():
    input0 = sys.argv[1]
    input1 = int(input0)
    if input1 == 0:
        startNum = random.randint(0,1000)
        indexNum = targets.index(2,startNum)
        print(saver_big_months(indexNum))
    elif input1 == 1:
        startNum = random.randint(0,1000)
        indexNum = targets.index(1,startNum)
        print(saver_small_months(indexNum))
    elif input1 == 2:
        startNum = random.randint(0,1000)
        indexNum = targets.index(0,startNum)
        print(poor_big_months(indexNum))
    else:
        startNum = random.randint(0,1000)
        indexNum = targets.index(3,startNum)
        print(average_months(indexNum))


main()
"""print("save and big spender")
firstzero = targets.index(2)
secondzero = targets.index(2,firstzero+1)
print(firstzero)
print(secondzero)
print(saver_big_months(firstzero))
print(saver_big_months(secondzero))
print("save and small spender")
firstone = targets.index(1)
secondone = targets.index(1,firstone+1)
print(saver_small_months(firstone))
print(saver_small_months(secondone))
print("poor and big spender")
firsttwo  = targets.index(0)
secondtwo = targets.index(0,firsttwo+1)
print(poor_big_months(firsttwo))
print(poor_big_months(secondtwo))
print("average spender")
firstthree = targets.index(3)
secondthree = targets.index(3,firstthree+1)
print(average_months(firstthree))
print(average_months(secondthree))"""
