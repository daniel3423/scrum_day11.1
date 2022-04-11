import matplotlib.pyplot as plt
import numpy as np


labels = ['2016', '2017', '2018', '2019', '2020']
spain_out = [31552,31109,31088,34296,34421]
poland_out = [11215, 10036, 10006, 9692, 9044]
turkey_out = [12964, 13303, 13834, 13197, 12968]
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
plt.figure(figsize=(12,8))
rects1 = ax.bar(x - width/2, spain_out, width, label='spanish students outgoing')
rects2 = ax.bar(x + width/2, poland_out, width, label='polish students outgoing')
rects3 = ax.bar(x + 1.5*width, turkey_out, width, label='turkish students outgoing')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Erasmus students')
ax.set_title('Erasmus students from Spain, Poland and Turkey')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()

