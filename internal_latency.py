## Epaminondas Aguiar
## Oct 3 23

import matplotlib.pyplot as plt

x = ['KA','StarlingX (OOK)']
values = [0.442, 0.212]
error_values = [0.078, 0.037]
colors= ['r','b']

# Bar plot
fig, ax = plt.subplots()
ax.bar(x = x, height = values, yerr = error_values, color=colors, capsize = 10)

for i in range(len(values)):
    plt.text(i, values[i]/2, round(values[i],3), ha = 'center', weight='bold', color='white')

ax.set_ylim(0,0.6)

ax.set_ylabel('RTT Ping (ms)')
ax.set_xlabel('OpenStack')

plt.savefig("network_internal_rtt.png",
            transparent=True)

plt.show()