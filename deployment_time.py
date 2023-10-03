## Epaminondas Aguiar
## Oct 2 23

import matplotlib.pyplot as plt
import numpy as np

labels = ['KA','StarlingX (OOK)']
tempo1 = [34, 21]
tempo2 = [15, 26]

width = 0.35  

fig, ax = plt.subplots()

ax.bar (labels, tempo1, width, label='Resource provisioning time')
ax.bar (labels, tempo2, width, bottom=tempo1, label='Boot time')

## valores no meio da barra
for bar in ax.patches:
  ax.text(bar.get_x() + bar.get_width() / 2,
          bar.get_height() / 2 + bar.get_y(),
          round(bar.get_height()), ha = 'center',
          color = 'w', weight = 'bold', size = 10)

## valor total no topo da barra
total_values = np.add(tempo1, tempo2)
for i, total in enumerate(total_values):
  ax.text(i, total + 0.5, round(total),
          ha = 'center', weight = 'bold', color = 'black')

##
ax.set_ylim(0,60)

##
ax.set_ylabel('Deployment Time of a single VM (seconds)')
ax.set_xlabel ('OpenStack')
ax.legend(loc=1) ## loc=1 (upper right)

plt.show()