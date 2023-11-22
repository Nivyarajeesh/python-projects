import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('C:/Users/Nivya Rajeesh/Downloads/Financial Sample.xlsx')

segments = data['Segment']
Total_sales = data['Sales']

plt.figure(figsize=(8,6))
plt.bar(segments,Total_sales , color='skyblue')

plt.xlabel('Segment',color ='blue')
plt.ylabel('Sales',color ='blue')
plt.title('SALES REPORT BY SEGMENT',color ='red')

plt.xticks(segments)
plt.tight_layout()
plt.show()