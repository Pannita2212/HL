import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

form = pd.read_csv('data_clean.csv', sep=',')


# =========demo===========

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



"""
HL1 = Q1	Q2	Q3	Q4
HL2 = Q5	Q6	Q7	Q8
HL3 = Q9	Q10	Q11	Q12
HL4 = Q13	Q14	Q15	Q16
HL5 = Q17	Q18	Q19	Q20
HL6 = Q21	Q22	Q23	Q24
"""
# HL1 = form[['Q1', 'Q2', 'Q3', 'Q4']]
# HL2 = form[['Q5', 'Q6',	'Q7', 'Q8']]
# HL3 = form[['Q9', 'Q10', 'Q11', 'Q12']]
# HL4 = form[['Q13' ,'Q14', 'Q15', 'Q16']]
# HL5 = form[['Q17', 'Q18', 'Q19', 'Q20']]
# HL6 = form[['Q21', 'Q22', 'Q23', 'Q24']]
dt_hl = form[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13' ,'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24']]

# --------------------------Sum HL1-6 & Mean--------------------------
hl1 = form.iloc[:, 3:7]
hl1["SUM_HL1"] = hl1.sum(axis=1)

hl2 = form.iloc[:, 7:11]
hl2["SUM_HL2"] = hl2.sum(axis=1)

hl3 = form.iloc[:, 11:15]
hl3["SUM_HL3"] = hl3.sum(axis=1)

hl4 = form.iloc[:, 15:19]
hl4["SUM_HL4"] = hl4.sum(axis=1)

hl5 = form.iloc[:, 19:23]
hl5["SUM_HL5"] = hl5.sum(axis=1)

hl6 = form.iloc[:, 23:27]
hl6["SUM_HL6"] = hl6.sum(axis=1)

tot_hl = form.iloc[:, 3:27]
tot_hl["SUM_HL"] = tot_hl.sum(axis=1)

hl = []
for i in range(len(dt_hl)):
    value = 0
    index = 3
    pointPerOne = []
    for j in dt_hl:
        if pd.isna(dt_hl.iloc[i][j]) == False:
        #     if 3 <= index <= 6:
        #         value += int(dt_hl.iloc[i][j])
        #     elif 7 <= index <= 10:
        #         value += int(dt_hl.iloc[i][j])
        #     elif 11 <= index <= 14:
        #         value += int(dt_hl.iloc[i][j])
        #     elif 15 <= index <= 18:
        #         value += int(dt_hl.iloc[i][j])
        #     elif 19 <= index <= 22:
        #         value += int(dt_hl.iloc[i][j])
        #     elif 23 <= index <= 26:
            value += int(dt_hl.iloc[i][j])
        index += 1
        if index in [7, 11, 15, 19 ,23, 27]:
            pointPerOne.append(value)
            value = 0
    for k in pointPerOne:
        value += k
    pointPerOne.append(value)

    hl.append(pointPerOne)
# print(hl, len(hl))


def addition(n): 
    return n + n

def getResult_HL(index: int):
    return sum(list(map(lambda x: x[index], hl)))/(len(form)*4)
# for indexs in range(6):
#     print((getResult_HL(indexs)))

# print(hl1['SUM_HL1'])
# for i in hl1['SUM_HL1']:
#     if i <12:
#         hl1["Status"] = ('Poor')
#         print(hl1)
#     elif 12<= i == 13:
#         hl1["Status"] = ('Fair')
#         print(hl1)
#     elif 14<= i == 15:
#         hl1["Status"] = ('Good')
#         print(hl1)
#     elif 16<= i == 20:
#         hl1["Status"] = ('Very Good')
#         print(hl1)

# print(hl1.info)

# for i in hl1['SUM_HL1']:
#     if i <12:
#         print(i, 'Poor')
#     elif 12<= i < 14:
#         print(i, 'Fair')
#     elif 14<= i < 15:
#         print(i, 'Good')
#     elif 16<= i < 21:
#         print(i, 'Very Good')

# print(hl['SUM_HL'])


l_poor = []
l_fair = []
l_good = []
l_exc = []

for i in tot_hl['SUM_HL']:
    if i < 72:
        l_poor.append(i)
        # print(i, 'Poor')
    elif 72 <= i < 84:
        # print(i, 'Fair')
        l_fair.append(i)
    elif 84 <= i < 96:
        # print(i, 'Good')
        l_good.append(i)
    else:
        # print(i, 'Excellent')
        l_exc.append(i)

# print(len(l_poor))
# print(len(l_fair))
# print(len(l_good))
# print(len(l_exc))
# print(len(form))

# print(l_fair)
# print(hl1); print(hl2); print(hl3)
# print(hl4); print(hl5); print(hl6)
# print(hl)

# print("Mean all val\n")
# print(hl1.mean()); print(hl2.mean()); print(hl3.mean())
# print(hl4.mean()); print(hl5.mean()); print(hl6.mean())

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

#------------------------ End sum and mean---------------------------

list_hl =[]
list_hl.append(hl1['SUM_HL1'].mean())
list_hl.append(hl2['SUM_HL2'].mean())
list_hl.append(hl3['SUM_HL3'].mean())
list_hl.append(hl4['SUM_HL4'].mean())
list_hl.append(hl5['SUM_HL5'].mean())
list_hl.append(hl6['SUM_HL6'].mean())
# print(list_hl)

list_allHL = []
# n = len(form)
list_allHL.append(len(l_poor))
list_allHL.append(len(l_fair))
list_allHL.append(len(l_good))
list_allHL.append(len(l_exc))

# print('Mean each question in HL1-6: ')
# print(HL1.mean())
# print(form.columns)
# print(form.head(10))

#==========================================Behavior============================================
# beh1 = form[['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10']]
# beh2 = form[['B11', 'B12', 'B13', 'B16', 'B17', 'B18']]
beh = form[['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B16', 'B17', 'B18']]

# for i in range(len(beh1)):
#     for j in beh1:
#         print(beh1.iloc[i][j])

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
for i in range(len(beh)):
    value = 0
    for j in beh:
        if beh.iloc[i][j] in val:
            value += int(val[beh.iloc[i][j]])
        else:
            beh.iloc[i][j]
    data.append(value)

data.sort()
# print(data)

bl_poor = []
bl_fair = []
bl_good = []
bl_exc = []
list_beh = []

for i in data:
    if i < 33:
        bl_poor.append(i)
        # print(i, 'Poor')
    elif 34 <= i <= 41:
        bl_fair.append(i)
        # print(i, 'Fair')
    elif 42 <= i <= 49:
        bl_good.append(i)
        # print(i, 'Good')  
    elif 50 <= i <= 66:
        bl_exc.append(i)
        # print(i, 'Excellent')

list_beh.append(len(bl_poor))
list_beh.append(len(bl_fair))
list_beh.append(len(bl_good))
list_beh.append(len(bl_exc))
# print(list_beh)

# ------------------------------------------Plot Pie chart-------------------------------------
'''
# Plot Pie Chart
labels = ['HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6']
# colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'gray', 'pink']

explode = (0, 0, 0, 0.1, 0, 0) 
fig1, ax1 = plt.subplots()
ax1.pie(list_hl, explode=explode, labels=labels, autopct='%.2f', shadow=True, startangle=0)
ax1.axis('equal')

plt.title("Health Literacy")
plt.show()
'''

'''
# Plot Pie Chart All HL
labels = ['Poor', 'Fair', 'Good','Excellent']

explode = (0, 0, 0, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(list_allHL, explode=explode, labels=labels, autopct='%0.2f%%', shadow=True, startangle=0, colors = ['lightcoral', 'gold', 'lightskyblue', 'yellowgreen'])
# ax1.axis('equal')

plt.title("Health Literacy Level")
plt.show()
'''

# -------------------------------------------Plot bar chart--------------------------------------------------
'''
# Plot bar chart
objects = ('HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6')
y_pos = np.arange(len(objects))
ylim = plt.ylim(0, 20)
plt.bar(y_pos, list_hl, align='center', alpha=0.5, color=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'gray', 'pink'])
for i, j in enumerate(list_hl):
    plt.text(i, j, str(j), horizontalalignment='center', verticalalignment='center')

plt.xticks(y_pos, objects)
plt.xlabel('Health Literacy', fontsize=10)
plt.ylabel('Point', fontsize=10)
plt.title('Health Literacy in 6 skill')
# plt.show()
'''

'''
# Plot bar chart AllHL
obj = ('Poor', 'Fair', 'Good','Excellent')
ylim = plt.ylim(0, 125)
pos = np.arange(len(obj))

plt.bar(pos, list_allHL, align='center', alpha=0.5, color=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'])
for index, value in enumerate(list_allHL):
    plt.text(index, value, str(value), horizontalalignment='center', verticalalignment='center')

plt.xticks(pos, obj)
plt.xlabel('Level')
plt.title('Health Literacy Level')
plt.show()
'''
'''
# Plot bar chart All Behavior
level = ('Poor', 'Fair', 'Good','Excellent')
poss = np.arange(len(level))
ylim = plt.ylim(0, 125)
plt.bar(poss, list_beh, align='center', alpha=0.5, color=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'])
for index, value in enumerate(list_beh):
    plt.text(index, value, str(value), horizontalalignment='center', verticalalignment='center')

plt.xticks(poss, level)
plt.xlabel('Level')
plt.title('Behavior Level')
plt.show()
'''
# ----------------------------------------------Plot Line chart----------------------------------------------------
'''
x_lst = []
for i in range(125):
    x_lst.append(i)

plt.plot(x_lst, data, color='red')
ylim = plt.ylim(0, 74)
plt.title('Behavior point per person', fontsize=14)
plt.xlabel('Person', fontsize=10)
plt.ylabel('Behavior point', fontsize=10)
plt.grid(True)
# plt.show()
'''


