## Epaminondas Aguiar
## Oct 3 23

import matplotlib.pyplot as plt
import numpy as np

x = ['KA','StarlingX (OOK)']
values = [758.630, 752.230]
colors= ['r','b']

fig,ax = plt.subplots()

ax.bar(x=x, height=values, color=colors)

for i in range(len(values)):
    plt.text(i, values[i] + 10, round(values[i],3), ha = 'center', weight='bold', color='black')


ax.set_ylim(0,1024)

ax.set_ylabel('External Throughput Rate (Mbps)')
ax.set_xlabel('OpenStack')

plt.savefig("network_ext_throughput_rate.png",
            transparent=True)

plt.show()