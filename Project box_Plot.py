import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/Nivya Rajeesh/Downloads/Financial Sample.xlsx')

unit_sold = df['Units Sold']

plt.figure(figsize=(8, 6))
plt.boxplot(unit_sold, patch_artist=True)

plt.xlabel('Unit Sold ',color='violet')
plt.title('UNIT SOLD RATIO',color ='purple')

plt.tight_layout()
plt.show()