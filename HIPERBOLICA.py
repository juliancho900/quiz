
# coding: utf-8

# $f(x) = \frac{e^x-e^-x}{e^x+e^-x}$

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3)
e = np.e
def f(x, e):
    return ((e ** x)-(e ** -x))/((e ** x)+(e ** -x))
plt.plot(x, f(x, e), '*')
plt.xlabel("Eje X")
plt.ylabel("Funcion f(x)")
plt.title('Tangente Hiperbolica')
plt.grid()


# In[ ]:



