from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

A = np.array([64.2,28.4,85.3,83.1,13.4,56.8,44.2,90])
B = np.array([45,29.5,32.3,49.3,18.3,34.2,43.9,13.8,27.4,43.4])

alpha = 0.05

mean_A = A.mean()
mean_B = B.mean()

size_A = A.shape[0]
size_B = B.shape[0]

S_2_A = A.var(ddof=1)
S_2_B = B.var(ddof=1)

t = (mean_A-mean_B)/np.sqrt((S_2_A/size_A+S_2_B/size_B))
df = (S_2_A/size_A+S_2_B/size_B)**2 / ((S_2_A/size_A)**2/(size_A-1)+(S_2_B/size_B)**2/(size_B-1))
pvalue = 1 - (stats.t.cdf(t,df) - stats.t.cdf(-t,df))

if pvalue/2<alpha:
    message = 'Гипотезу принимаем'
else:
    message = 'Гипотезу отвергаем'

x = np.linspace(mean_A-np.sqrt(S_2_A)*4,mean_A+np.sqrt(S_2_A)*4,200)

pdf1 = stats.norm.pdf(x,mean_A,np.sqrt(S_2_A))
pdf2 = stats.norm.pdf(x,mean_B,np.sqrt(S_2_B))

plt.plot(x,pdf1 , color = 'red')
plt.plot(x,pdf2 , color = 'blue')        
plt.savefig('plot.png')