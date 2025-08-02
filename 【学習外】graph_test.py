import matplotlib.pyplot as plt

# データの準備
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# 折れ線グラフを描画
plt.plot(x, y, marker='o', color='blue')

# グラフにタイトルとラベルを追加
plt.title('Sample Line Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# グラフを表示
plt.grid(True)
plt.show()
