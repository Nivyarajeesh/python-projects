import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('C:/Users/Nivya Rajeesh/Downloads/Financial Sample.xlsx')

sum = data.groupby('Product')['Profit'].sum()
plt.figure(figsize=(8, 6))
plt.pie(sum, labels=sum.index,autopct='%1.1f%%')
plt.title('PROFIT REPORT OF PRODUCTS',color ='green')

plt.show()
