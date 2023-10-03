## Epaminondas Aguiar
## Oct 3 23

import matplotlib.pyplot as plt

x = ['Idle','with workload (iperf)']
values = [2.4, 2.9]
error_values = [0.51, 1.39]
colors= ['r','b']

# Bar plot
fig, ax = plt.subplots()
ax.bar(x = x, height = values, yerr = error_values, color=colors, capsize = 10)

for i in range(len(values)):
    plt.text(i, values[i]/2 - 0.2, round(values[i],3), ha = 'center', weight='bold', color='black')



ax.set_ylim(0,6)

ax.set_ylabel('Latency (ms)')
#ax.set_xlabel('OpenStack')

plt.show()