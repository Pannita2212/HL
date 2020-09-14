import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

form = pd.read_csv('data_clean.csv', sep=',')


dt_hl = form[['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13' ,'Q14', 'Q15', 'Q16', 'Q17', 'Q18', 'Q19', 'Q20', 'Q21', 'Q22', 'Q23', 'Q24']]

hl = []
sum_hl = []
l_poor = []
l_fair = []
l_good = []
l_exc = []

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

        # Check Level of HL
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



def averageHL(index: int, form, hl: []):
        return sum(list(map(lambda x: x[index], hl)))/(len(form))

    # ---------This is average of 6 HL----------
mean_hl =[]
for indexs in range(6):
        mean_hl.append((averageHL(indexs, form, hl)))

lst_hl1 = []
lst_hl2 = []
lst_hl3 = []
lst_hl4 = []
lst_hl5 = []
lst_hl6 = []
lst_hl = []
lev_hl = []

for i in range(len(hl)+1):
        lst_hl1.append(hl[i][0])
        lst_hl2.append(hl[i][1])
        lst_hl3.append(hl[i][2])
        # lst_hl3.append(mean_hl[i][2])
        lst_hl4.append(hl[i][3])
        # lst_hl4.append(mean_hl[i][3])
        lst_hl5.append(hl[i][4])
        # lst_hl5.append(mean_hl[i][4])
        lst_hl6.append(hl[i][5])
        # lst_hl6.append(mean_hl[i][5])
        lst_hl.append(hl[i][6])
        lev_hl.append(hl[i][7])

print(lst_hl1, lst_hl2)