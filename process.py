import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Read data file, separate by ','
form = pd.read_csv('data_clean.csv', sep=',')

#==============================================Demographic============================================
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

dt_demo = form[['sex', 'age', 'edu']]
demo = []
# for i in range(len(dt_demo)):
#     value = 0
#     index = 0
#     pointPerOne = []
#     for j in dt_demo:
#         if index in [2, 3, 4]:
#             pointPerOne.append(value)
#             value = 0
#     demo.append(pointPerOne)

# print(demo)

#==============================================Health Literacy============================================
# Create dataframe all questions about HL
dt_hl = form[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13' ,'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24']]

hl = []
for i in range(len(dt_hl)):
    value = 0
    index = 3
    pointPerOne = []
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

    hl.append(pointPerOne)
print('HL each person:', hl)

def addition(n): 
    return n + n

def getResult_HL(index: int):
    return sum(list(map(lambda x: x[index], hl)))/(len(form))
# for indexs in range(6):
#     print((getResult_HL(indexs)))

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
sum_hl.append(len(l_poor))
sum_hl.append(len(l_fair))
sum_hl.append(len(l_good))
sum_hl.append(len(l_exc))

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



# Plot bar chart AllHL------------------------------------------------------------
obj = ('Poor', 'Fair', 'Good','Excellent')
ylim = plt.ylim(0, 125)
pos = np.arange(len(obj))

plt.bar(pos, sum_hl, align='center', alpha=0.5, color=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'])
for index, value in enumerate(sum_hl):
    plt.text(index, value, str(value), horizontalalignment='center', verticalalignment='center')

plt.xticks(pos, obj)
plt.xlabel('Level')
plt.ylabel('Person')
plt.title('Health Literacy Level')
# plt.show()
# --------------------------------------------------------------------------------



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
for i in range(len(beh)):
    value = 0
    for j in beh:
        if beh.iloc[i][j] in val:
            value += int(val[beh.iloc[i][j]])
        else:
            beh.iloc[i][j]
    data.append(value)

print("Behavior each person", data)

'''
for i in data:
    val = data[i]+16
    if val < 49:
        print(val, 'Poor')
    elif 50 < val < 57:
        print(val, 'Fair')
    elif 58 < val < 65:
        print(val, 'Good')  
    else:
        print(val, 'Excellent')
'''


# ==============================================Write to csv=========================================================
zipList =  list(zip(lst_hl1, lst_hl2, lst_hl3, lst_hl4, lst_hl5, lst_hl6, lst_hl, data))

result = pd.DataFrame(zipList, columns=['HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6', 'SUM_HL', 'Behavior'])
result.to_csv('result.csv')