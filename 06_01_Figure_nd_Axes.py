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

"""
(base) jovyan@0dd04ba1e306:~/work$ python 06_01_Figure_nd_Axes.py
figlabels: []
fignums: []
gcf: Figure(640x480)
------------------------
figlabels: ['']
fignums: [1]
(base) jovyan@0dd04ba1e306:~/work$
"""
