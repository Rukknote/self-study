s = lambda x: x * x
print(s(3))

"""
以下、クロージャの書き方をシンプルにできる
def power(exponent):
    def inner_power(base):
        return base ** exponent # baseをexponent乗する
    return inner_power
"""
def power(exponent):
    return lambda base: base ** exponent
third_power = power(3)
print(third_power(2))

t = lambda exponent, base: exponent ** base
print(t(4, 3))


numbers = [1, 2, 3, 4, 5]

def filterfunc(num):
    if num % 2 == 0:
        return False
    else:
        return True

filterd_num = filter(filterfunc, numbers)#filterは第一引数を関数に、第二引数を関数に入れて返す
print(list(filterd_num))

# もっと簡潔に書く
def filterfunc2(num):
    return num % 2
filterd_num = filter(filterfunc2, numbers)#filterは第一引数を関数に、第二引数を関数に入れて返す
print(list(filterd_num))

# lambdaで簡潔に書く
print(list(filter(lambda num: num % 2, numbers)))