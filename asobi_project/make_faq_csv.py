import pandas as pd

questions = ["商品の返品方法は？", "営業時間は何時？", "送料はいくら？", "支払い方法は？", "会員登録は必要？"]
answers = [
    "未開封であれば7日以内に可能です。",
    "平日9時〜18時です。",
    "全国一律500円です。",
    "クレジットカード・代引きに対応しています。",
    "無料で登録できます。"
]

rows = []
for i in range(1000):
    q = questions[i % len(questions)] + f"（サンプル{i+1}）"
    a = answers[i % len(answers)]
    rows.append({"質問": q, "回答": a})

df = pd.DataFrame(rows)
df.to_csv("faq_sample_1000.csv", index=False, encoding="utf-8-sig")
print("faq_sample_1000.csv を作成しました。")

