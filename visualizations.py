import glob
import pandas as pd
import csv
import matplotlib.pyplot as plt

path_result, ids, name, points, reviews, price = [], [], [], [], [], []
# Get all list of result
files = glob.glob("./data/*")
for f in files:
    path_result.append(f)

# for y in path_result:

with open(path_result[0], 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        ids.append(row[0])
        name.append(row[1])
        points.append(row[3])
        reviews.append(row[4])
        price.append(row[6])

print(name)

plt.plot(name, price, color='g',
         marker='o', label="Data Transaksi")

# plt.xticks(rotation=25)
plt.xlabel('Nama Produk')
plt.ylabel('Harga Produk')
plt.title('Data Visualisasi', fontsize=20)
plt.grid()
plt.legend()
plt.show()

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# columns = ["Name", "Marks"]
# df = pd.read_csv(path_result[0], usecols=columns)
# print("Contents in csv file:\n", df)
# plt.plot(df.Name, df.Marks)
# plt.show()
