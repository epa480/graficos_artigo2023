## Epaminondas Aguiar
## Oct 3 23

import matplotlib.pyplot as plt

x = ['KA','StarlingX (OOK)']
values = [21.3, 29.15]
error_values = [0.44, 1.30]
colors= ['r','b']

# Bar plot
fig, ax = plt.subplots()
ax.bar(x = x, height = values, yerr = error_values, color=colors, capsize = 10)

for i in range(len(values)):
    plt.text(i, values[i]/2, round(values[i],3), ha = 'center', weight='bold', color='black')

ax.set_ylim(0,36)

ax.set_ylabel('Throughput (Gbps)')
ax.set_xlabel('OpenStack')

plt.show()
