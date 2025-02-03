# *args：不特定多数の引数を受け取る
def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total

average = get_average(1, 2)
print(average)

# **kwargs：不特定多数の引数を辞書で受け取る
def kwargs_func(**kwargs):
    # argumentsで受け取った情報を辞書で返す
    print(kwargs)

    # 受け取った情報を書き換えられる
    param1 = kwargs.get("param1", 10)# param1がなければデフォルトの10を返す
    param2 = kwargs.get("param2", 20)
    print(f"param1: {param1}, param2: {param2}")

kwargs_func(param1=1, param2=3)
kwargs_func()# param1とparam2のデフォルトを返す

# *と**はunpacking operator
numbers = (1, 2, 3)
print(*numbers)#(1, 2, 3)が1, 2, 3で受け取る
print(1, 2, 3)

a = {"a": 1, "b":2}
print({**a})# {"a": 1, "b":2}がkey : value（"a"と1のみ）になる