import numpy as np
import matplotlib
import matplotlib.pyplot as plt


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