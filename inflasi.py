import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_excel('inflasi.xlsx')
print(table)

inflasi = pd.DataFrame(table, columns=['Inflasi'])
print(inflasi)

plt.plot(inflasi)
plt.ylabel('Inflasi')
plt.show()

