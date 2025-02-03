# 再帰関数（recursive function）: 関数ないで自身の関数をcallする関数（かなり処理に時間がかかる）
# 階乗：n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!

def facctorial(n):
    if n == 1:
        return 1
    else:
        return n * facctorial(n-1)#自身を何度も呼ぶ

print(facctorial(3))

# フィボナッチ数列：(0), 1, 1, 2, 3, 5, 8, 13...
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(4))
for i in range(500):
    print(i, fibonacci(i))

# 再帰関数を使わない
def fibonacci2(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result

#for i in range(500):
#    print(i, fibonacci2(i))