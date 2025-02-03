# nested function（関数の中で関数を定義）
def outer(outer_param):
    def innner():
        # outerの引数（parameter）を使える
        print(outer_param)
        print("This is inner func")
    innner()

# inner()は外から見えない、outer関数のみ使える
outer(5)

msg = "I am global"

def outer2():
    msg = "I am outer" #関数内の変数が上書きされる
    
    def inner():
        nonlocal msg #local変数ではない
        msg = "I am inner"
        print(msg)
    inner()
    print(msg)

outer2()
print(msg)