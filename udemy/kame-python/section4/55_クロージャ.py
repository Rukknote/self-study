# 関数もオブジェクト
def compute_square(num):
    return num * num

f = compute_square #関数のオブジェクトを変数に入れられる
print(type(f))
print(f(10))

function_list = [1, True, f] #リストの要素に入れられる
print(function_list[-1](10))

#関数も引数として渡せる
def execute_func(func, param):
    return func(param)

print(execute_func(f, 10))


# 関数をreturnする
def return_func():

    def inner_func():
        print("This is an inner function")
    return inner_func # ()をつけるとprint結果を出力して終わりだけれど、（)を消すとオブジェクトとして返す

f = return_func()
print(f) #<function return_func.<locals>.inner_func at 0x1072f3b50>と、inner_funcであることがわかる
print(type(f))
f() #This is an inner function

# Closure: 状態をキープした関数を作る
# 状態が静的なパターン
def power(exponent):

    def inner_power(base):
        return base ** exponent # baseをexponent乗する
    return inner_power

power_four = power(4) #power関数の引数に4を入れた状態をキープするオブジェクト
print(power_four(2)) #inner_power(2)を入れて、2の4乗が返る

# 状態が動的なパターン
def average():
    nums = [] # 1回目に5が入る([5])→平均は5 2回目は10も入る([5, 10])→平均は7.5

    def innner_average(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return innner_average

average_nums = average()
print(average_nums(5))
print(average_nums(10))