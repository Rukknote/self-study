import time
from functools import lru_cache

# .time(): 1970/1/1 秒数表示(Unix時間)
print(time.time())
# 年数に直す
print(time.time()/(60*60*24*365))

before = time.time()
a = 10*2
after = time.time()
print(f"it took {after - before:.2f}sec")#小数点第2位まで表示

@lru_cache #1度計算したフィボナッチ数をキャッシュとして保持してくれる
def facctorial(n):
    if n == 1:
        return 1
    else:
        return n * facctorial(n-1)#自身を何度も呼ぶ

before = time.time()
print(facctorial(10)) #it took 0.00sec 早くなった
after = time.time()
print(f"it took {after - before:.2f}sec")#小数点第2位まで表示

# .ctime() 今のローカル時間を文字列で返す
print(time.ctime())# Sun Jan 26 16:45:21 2025

# .localtime() 構造化データで返す
localtime = time.localtime()
print(localtime)
print(f"今年は{localtime.tm_year}")

# .sleep(secs) secs秒だけプログラムが待機する
sec = 10
print(f"{sec}秒待ってください")
#time.sleep(sec)
print(f"{sec}秒経ちました")

def timer(func):
    def innner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__} took {after - before:.2f} sec")
    return innner

@timer
def lazy_func(sec):
    print("I'm working")
    time.sleep(sec)
    print("Done")

lazy_func(10)