import pandas as pd
from collections import Counter
import re

# CSV読み込み
df = pd.read_csv("faq_sample_1000.csv", encoding="utf-8-sig")

# 質問文をすべてつなげて1つの長いテキストにする
all_text = " ".join(df['質問'].astype(str))

# 正規表現で日本語の単語っぽいものを抽出する（漢字・ひらがな・カタカナ・英数字を含む単語）
words = re.findall(r'[一-龥ぁ-んァ-ンa-zA-Z0-9]+', all_text)

# 単語の出現頻度をカウント
counter = Counter(words)

# 出現回数が多いトップ20を取得
top20 = counter.most_common(20)

# 画面表示
print("よく出るキーワード トップ20")
for word, count in top20:
    print(f"{word}: {count}回")

# ファイルに書き出し
with open("keyword_top20.txt", "w", encoding="utf-8") as f:
    f.write("よく出るキーワード トップ20\n")
    for word, count in top20:
        f.write(f"{word}: {count}回\n")

print("keyword_top20.txt に結果を書き出しました。")

