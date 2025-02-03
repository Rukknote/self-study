# デコレータ：関数に機能を付属する

def greeting(func):
    def inner(*args, **kwargs): #引数nameのみだと、say_name_and_originの2つの引数を受け取れずエラーになるので*argsと一応**kwargsへ
        print("Hello")
        func(*args, **kwargs)
        print("Nice to meet you")
    return inner

@greeting
def say_name(name):
    print(f"I'm {name}")

@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")

#say_name("Jiro")

#f = greeting(say_name)
#f("Taro")

#say_name = greeting(say_name) #innerのprintが追加された新しいsay_name関数ができる
# @greetingをつけることでデコレーション（greeting関数がsay_name関数に入る、装飾）される
say_name("Taro")


say_name_and_origin("Taro", "Tokyo")