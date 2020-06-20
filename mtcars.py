import pandas as pd

table = pd.read_excel('mtcars.xlsx')
print(table)

mpg = pd.DataFrame(table,columns=['mpg'])
print(mpg)

mpg.loc[mpg['mpg'] < 20, 'mpg_level'] = 'Low'
mpg.loc[mpg['mpg'] >= 20, 'mpg_level'] = 'medium'
mpg.loc[mpg['mpg'] >30, 'mpg_level'] = 'hard'
print(mpg)

import matplotlib.pyplot as plt
plt.plot ([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

mpg.plot(kind='scatter', x='mpg', y='mpg_level',color='red')
plt.show()
