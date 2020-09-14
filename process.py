import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from csv import writer


'''==============================================Demographic Data============================================'''
def calculateDemographic(form):
    dt_demo = form[['sex', 'age', 'edu']]
    demo = []
    for i in range(len(dt_demo)):
        index = 0
        person = []
        for j in dt_demo:
            value = dt_demo.iloc[i][j]
            index += 1
            if index in [1, 2, 3]:
                person.append(value)
        demo.append(person)

    sex = []
    age = []
    edu = []
    sexDict = {}
    ageDict = {}
    eduDict = {}
    for i in range(len(demo)):
        sexVal = demo[i][0]
        if sexVal in sexDict:
            sexDict[sexVal] += 1
        else:
            sexDict[sexVal] = 1
        sex.append(sexVal)
        
        ageVal = demo[i][1]
        if ageVal in ageDict:
            ageDict[ageVal] += 1
        else:
            ageDict[ageVal] = 1
        age.append(ageVal)

        eduVal = demo[i][2]
        if eduVal in eduDict:
            eduDict[eduVal] += 1
        else:
            eduDict[eduVal] = 1
        edu.append(eduVal)
# print(sexDict, eduDict, ageDict)
    sex.sort()
    age.sort()
    edu.sort()
    return sex, age, edu


'''==============================================Health Literacy Data============================================'''
def averageHL(index: int, form, hl: []):
    return sum(list(map(lambda x: x[index], hl)))/(len(form))

def calculateHL(form):
# Create dataframe all questions about HL
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
    lastIndex = 0
    for i in range(len(hl)):
        lastIndex += 1
        lst_hl1.append(hl[i][0])
        lst_hl2.append(hl[i][1])
        lst_hl3.append(hl[i][2])
        lst_hl4.append(hl[i][3])
        lst_hl5.append(hl[i][4])
        lst_hl6.append(hl[i][5])
        lst_hl.append(hl[i][6])
        lev_hl.append(hl[i][7])

    return lst_hl1, lst_hl2, lst_hl3, lst_hl4, lst_hl5, lst_hl6, lst_hl, lev_hl

'''==============================================Behavior Data========================================================='''
def calculateBehavior(form):
    # Create dataframe all questions about Behavior
    dt_beh = form[['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B16', 'B17', 'B18']]
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

    beh = []
    lev_beh = []
    for i in range(len(dt_beh)):
        value = 0
        for j in dt_beh:
            if dt_beh.iloc[i][j] in val:
                value += int(val[dt_beh.iloc[i][j]])
            else:
                dt_beh.iloc[i][j]
        value += 16
        if value < 49:
            lev_beh.append('Poor')
        elif 50 < value < 57:
            lev_beh.append('Fair')
        elif 58 < value < 65:
            lev_beh.append('Good')  
        else:
            lev_beh.append('Excellent')
        
        beh.append(value)
    # print("Behavior each person", beh)
    return beh, lev_beh

'''==============================================Write to csv========================================================='''
def writeCSV(output: {}, form):
    hl_avg = ['lst_hl1', 'lst_hl2', 'lst_hl3', 'lst_hl4', 'lst_hl5', 'lst_hl6']

    for item in output:
        valueCal = 0
        if item in hl_avg:
            for i in output[item]:
                valueCal += i
            output[item].append(valueCal / len(form))
        
    output['sex'].append('')
    output['age'].append('')
    output['edu'].append('Average')
    output['lst_hl'].append('')
    output['beh'].append('')
    output['lev_beh'].append('')
    output['lev_hl'].append('')
    
    zipList =  list(zip(
        output['sex'],
        output['age'],
        output['edu'],
        output['lst_hl1'],
        output['lst_hl2'],
        output['lst_hl3'],
        output['lst_hl4'], 
        output['lst_hl5'],
        output['lst_hl6'],
        output['lst_hl'],
        output['lev_hl'],
        output['beh'],
        output['lev_beh']
    ))

    result = pd.DataFrame(zipList, columns=['Sex', 'Age', 'Education', 'HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6', 'SUM_HL', 'Level_HL', 'Behavior', 'Level_Beh'])
    result.to_csv('result2.csv')

'''
def append_row(file_name, lst_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(lst_of_elem)
'''

# Function for read csv file
def readCSVFile():
    return pd.read_csv('data_clean.csv', sep=',')

# Function Main!!
def main():
    output = {}
    form = readCSVFile()
    # Call function calculateDemographic()
    output['sex'], output['age'], output['edu'] = calculateDemographic(form)

    # Call function calculateHL()
    output['lst_hl1'], output['lst_hl2'], output['lst_hl3'], output['lst_hl4'], \
    output['lst_hl5'], output['lst_hl6'], output['lst_hl'], output['lev_hl'] = calculateHL(form)

    # Call function calculateBehavior() 
    output['beh'], output['lev_beh'] = calculateBehavior(form)

    # Call function writeCSV
    writeCSV(output, form)

    # append_row('result2.csv', output['mean_hl'])
main()