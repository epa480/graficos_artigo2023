## Epaminondas Aguiar
## Oct 2 23

import matplotlib.pyplot as plt
import numpy as np

x = ['KA','StarlingX (OOK)']
values = [3.86, 27.65]
colors= ['r','b']

fig,ax = plt.subplots()

ax.bar(x=x, height=values, color=colors)

for i in range(len(values)):
    plt.text(i, values[i] + 0.5, values[i], ha = 'center', weight='bold', color='black')

ax.set_ylim(0,100)

ax.set_ylabel('CPU Usage (%)')
ax.set_xlabel('OpenStack')

plt.savefig("cloud_cpu_util.png",
            transparent=True)

plt.show()