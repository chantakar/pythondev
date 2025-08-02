def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 動作確認例
for i in range(1, 11):
    print(f"第{i}項: {fibonacci(i)}")