import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Read data file, separate by ','
form = pd.read_csv('data_clean.csv', sep=',')

#==============================================Demographic============================================
'''
temp = {
    "ชาย": 1,
    "หญิง": 2,
    "ไม่ต้องการระบุ": 3,
    "Bisexual": 4,
    "น้อยกว่า 20 ปี": 1,
    "20-29 ปี": 2,
    "30-39 ปี": 3,
    "40-49 ปี": 4,
    "50-59 ปี": 5,
    "60 ปีขึ้นไป": 6,
    "ไม่ได้เรียนหนังสือ": 1,
    "ประถมศึกษา": 2,
    "มัธยมศึกษาตอนต้น": 3,
    "มัธยมศึกษาตอนปลาย/ปวช.": 4,
    "อนุปริญญา/ปวส.": 5,
    "ปริญญาตรีขึ้นไป": 6
}
'''
dt_demo = form[['sex', 'age', 'edu']]
demo = []
for i in range(len(dt_demo)):
    value = ''
    index = 0
    person = []
    for j in dt_demo:
        value = dt_demo.iloc[i][j]
        index += 1
        if index in [1, 2, 3]:
            person.append(value)
            value = 0
    demo.append(person)

sex = []
for i in range(125):
    val = demo[i][0]
    sex.append(val)

age = []
for i in range(125):
    val = demo[i][1]
    age.append(val)

edu = []
for i in range(125):
    val = demo[i][2]
    edu.append(val)

#==============================================Health Literacy============================================
# Create dataframe all questions about HL
dt_hl = form[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13' ,'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24']]

hl = []
sum_hl = []; l_poor = []
l_fair = []; l_good = []; l_exc = []

for i in range(len(dt_hl)):
    value = 0
    index = 3
    pointPerOne = []
    temp = 0
    for j in dt_hl:
        # Check NaN value
        if pd.isna(dt_hl.iloc[i][j]) == False:
            value += int(dt_hl.iloc[i][j])
        index += 1
        # Check index for split each HL
        if index in [7, 11, 15, 19 ,23, 27]:
            pointPerOne.append(value)
            value = 0
    for k in pointPerOne:
        value += k
    pointPerOne.append(value)

    if value < 72:
        pointPerOne.append('Poor')
    elif 72 <= value < 84:
        pointPerOne.append('Fair')
    elif 84 <= value < 96:
        pointPerOne.append('Good')
    else:
        pointPerOne.append('Excellent')
    
    hl.append(pointPerOne)
# print('HL each person:', hl)

def addition(n): 
    return n + n

def getResult_HL(index: int):
    return sum(list(map(lambda x: x[index], hl)))/(len(form))
# for indexs in range(6):
#     print((getResult_HL(indexs)))
'''
sum_hl = []; l_poor = []
l_fair = []; l_good = []; l_exc = []
for i in range(125):
    if hl[i][6] < 72:
        l_poor.append('Poor')
    elif 72 <= hl[i][6] < 84:
        l_fair.append('Fair')
    elif 84 <= hl[i][6] < 96:
        l_good.append('Good')
    else:
        l_exc.append('Excellent')
sum_hl.append(l_poor)
sum_hl.append(l_fair)
sum_hl.append(l_good)
sum_hl.append(l_exc)
# print(sum_hl)
'''

lst_hl1 = []
for i in range(125):
    val = hl[i][0]
    lst_hl1.append(val)

lst_hl2 = []
for i in range(125):
    val = hl[i][1]
    lst_hl2.append(val)

lst_hl3 = []
for i in range(125):
    val = hl[i][2]
    lst_hl3.append(val)

lst_hl4 = []
for i in range(125):
    val = hl[i][3]
    lst_hl4.append(val)

lst_hl5 = []
for i in range(125):
    val = hl[i][4]
    lst_hl5.append(val)

lst_hl6 = []
for i in range(125):
    val = hl[i][5]
    lst_hl6.append(val)

lst_hl = []
for i in range(125):
    val = hl[i][6]
    lst_hl.append(val)
# print(hl)

lev_hl = []
for i in range(125):
    val = hl[i][7]
    lev_hl.append(val)
'''
def loop (lst, val):
    for i in hl:
        for j in i:
            val[j]
            lst.append(val)
    print(lst)

loop(lst_hl1, hl[i][1])
'''

# ==============================================Behavior=========================================================
# Create dataframe all questions about Behavior
beh = form[['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B16', 'B17', 'B18']]
# Create dict for convert str to int
val = {
    "ทุกครั้ง": 4,
    "บ่อยครั้ง": 3,
    "น้อยครั้ง": 2,
    "ไม่ปฏิบัติ": 1,
    "6-7 วัน (5)": 5,
    "4-5 วัน (4)": 4,
    "3 วัน (3)": 3,
    "1-2 วัน (2)": 2,
    "ไม่ปฏิบัติ (1)": 1
}

data = []
lev_beh = []
for i in range(len(beh)):
    value = 0
    for j in beh:
        if beh.iloc[i][j] in val:
            value += int(val[beh.iloc[i][j]])
        else:
            beh.iloc[i][j]
    data.append(value)
    value += 16
    if value < 49:
        lev_beh.append('Poor')
    elif 50 < value < 57:
        lev_beh.append('Fair')
    elif 58 < value < 65:
        lev_beh.append('Good')  
    else:
        lev_beh.append('Excellent')
    
    data.append(value)
# print("Behavior each person", data)


# ==============================================Write to csv=========================================================

zipList =  list(zip(sex, age, edu, lst_hl1, lst_hl2, lst_hl3, lst_hl4, lst_hl5, lst_hl6, lst_hl, lev_hl, data, lev_beh))

result = pd.DataFrame(zipList, columns=['Sex', 'Age', 'Education', 'HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6', 'SUM_HL','Level HL', 'Behavior', 'Level Beh'])
result.to_csv('result.csv')
