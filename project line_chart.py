import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('C:/Users/Nivya Rajeesh/Downloads/Financial Sample.xlsx')

sales_sum = data.groupby('Month Name')['Sales'].sum()

plt.figure(figsize=(8, 6))
plt.plot(sales_sum, marker='o', linestyle='-')

plt.xlabel('Months',color='purple')
plt.ylabel('Sales',color='purple')
plt.title('MONTHLY SALES',color= 'purple')

plt.xticks(rotation =45)
plt.tight_layout()
plt.show()