
# coding: utf-8

# $$f(x)= 1 / \sqrt[2]{2\pi \sigma^2 }e^-(x^2/2 \sigma^2)$$

# In[3]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt

sigma=0.01
x=np.linspace(-100,100)
e=np.e
pi=np.pi
def f(x):
    return (1/np.sqrt(2*pi*sigma**2))*(e**-((x**2)/2*(sigma**2)))

plt.plot(x,f(x),'--',color='r')
plt.xlabel('EJE X')
plt.title('FUNCION GAUSSIANA')
plt.grid()


# In[ ]:



