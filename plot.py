import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

result = pd.read_csv('result2.csv', sep=',')

'''
# ==============================================Health Literacy============================================
data = result[['Level_HL']]
lev_hl = []
hl_poor = 0
hl_fair = 0
hl_good = 0
hl_exc = 0
for i in range(len(data)):
    index = 0
    for j in data:
        val = data.iloc[i][j]
        index += 1
        if val == 'Poor':
            hl_poor += 1 
        elif val == 'Fair':
            hl_fair += 1 
        elif val == 'Good':
            hl_good += 1 
        else:
           hl_exc += 1 
    
lev_hl.append(hl_poor)
'''

# Function for count each Level
def countLev(col, poor, fair, good, exc):
    lst = []
    data = result[[col]]
    for i in range(len(data)):
        index = 0
        for j in data:
            val = data.iloc[i][j]
            index += 1
            if val == 'Poor':
                poor += 1 
            elif val == 'Fair':
                fair += 1 
            elif val == 'Good':
                good += 1 
            else:
                exc += 1 
    lst.append(poor)
    lst.append(fair)
    lst.append(good)
    lst.append(exc)
    return lst


# Function for plot Level Bar Chart 
def plotBarLev(obj, data: [], title):
    ylim = plt.ylim(0, len(result))
    pos = np.arange(len(obj))

    plt.bar(pos, data, align='center', alpha=0.5, color=['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'])
    for index, value in enumerate(data):
        plt.text(index, value, str(value), horizontalalignment='center', verticalalignment='center')

    plt.xticks(pos, obj)
    plt.xlabel('Level')
    plt.ylabel('Number of Responses')
    plt.title(title)
    plt.show()

def plotPieHL(list_hl):
    labels = ['HL1', 'HL2', 'HL3', 'HL4', 'HL5', 'HL6']
    # colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'gray', 'pink']

    explode = (0, 0, 0, 0.1, 0, 0) 
    fig1, ax1 = plt.subplots()
    ax1.pie(list_hl, explode=explode, labels=labels, autopct='%.2f', shadow=True, startangle=0)
    ax1.axis('equal')


plt.title("Health Literacy")
plt.show()
# Function Main!!
def main():
    lev = ('Poor', 'Fair', 'Good','Excellent')
    plotBarLev(lev, countLev('Level_HL', 0, 0, 0, 0), 'Health Literacy Level')
    plotBarLev(lev, countLev('Level_Beh', 0, 0, 0, 0), 'Behavior Level')

main()
