## Epaminondas Aguiar
## Oct 2 23

import matplotlib.pyplot as plt
import numpy as np

x = ['KA','StarlingX (OOK)']
values = [11356/1024, 11894/1024]
colors= ['r','b']

fig,ax = plt.subplots()

ax.bar(x=x, height=values, color=colors)

for i in range(len(values)):
    plt.text(i, values[i] + 0.5, round(values[i],3), ha = 'center', weight='bold', color='black')


ax.set_ylim(0,32)

ax.set_ylabel('Memory Usage (GB)')
ax.set_xlabel('OpenStack')

plt.savefig("memory_usage.png",
            transparent=True)

plt.show()