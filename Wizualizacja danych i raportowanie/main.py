# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.__version__

#zadanie2
x=np.linspace(-5,5,100) #generuje wektor
y=x**2
print(x)
plt.plot(x,y,color='k') #łączy x i y linią
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykres funkcji kwadratowej y=x^2')