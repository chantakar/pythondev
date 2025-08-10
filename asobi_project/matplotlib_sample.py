import matplotlib.pyplot as plt
import numpy as np

# データ作成
x = [1, 2, 3, 4, 5]
y = [2, 5, 1, 8, 7]

# 1. 折れ線グラフ
plt.figure(figsize=(6,4))
plt.plot(x, y, marker="o", color="blue", label="データ1")
plt.title("折れ線グラフの例")
plt.xlabel("X軸")
plt.ylabel("Y軸")
plt.legend()
plt.grid(True)
plt.show()

# 2. 棒グラフ
categories = ["A", "B", "C"]
values = [5, 3, 7]
plt.figure(figsize=(6,4))
plt.bar(categories, values, color="orange")
plt.title("棒グラフの例")
plt.xlabel("カテゴリー")
plt.ylabel("値")
plt.show()

# 3. ヒストグラム
data = np.random.randn(1000)  # 平均0、標準偏差1の乱数
plt.figure(figsize=(6,4))
plt.hist(data, bins=20, color="green", edgecolor="black")
plt.title("ヒストグラムの例")
plt.xlabel("値")
plt.ylabel("頻度")
plt.show()
