import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Read data file, separate by ','
form = pd.read_csv('.csv', sep=',')


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
# print('HL each person:', hl)

def addition(n): 
    return n + n

def getResult_HL(index: int):
    return sum(list(map(lambda x: x[index], hl)))/(len(form))
# for indexs in range(6):
#     print((getResult_HL(indexs)))



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

# print("Behavior each person", data)