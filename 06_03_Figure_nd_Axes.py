import matplotlib.pyplot as plt
import matplotlib
import numpy as np

figlabels = plt.get_figlabels()
fignums = plt.get_fignums()
gcf = plt.gcf()

print("figlabels:", figlabels)
print("fignums:", fignums)
print("gcf:", gcf)
print("--------" * 3)

figlabels = plt.get_figlabels()
fignums = plt.get_fignums()

print("figlabels:", figlabels)
print("fignums:", fignums)
print("--------" * 3)

fig1 = plt.figure()
figlabels = plt.get_figlabels()
fignums = plt.get_fignums()

print("figlabels:", figlabels)
print("fignums:", fignums)
print("--------" * 3)

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=3, label="plot figure")
plt.legend()
plt.savefig("06_03_Figure_nd_Axes.png")

print("figlabels:", figlabels)
print("fignums:", fignums)

"""
(base) jovyan@0dd04ba1e306:~/work$ python 06_02_Figure_nd_Axes.py
figlabels: []
fignums: []
gcf: Figure(640x480)
------------------------
figlabels: ['']
fignums: [1]
------------------------
figlabels: ['', '']
fignums: [1, 2]
(base) jovyan@0dd04ba1e306:~/work$
"""
