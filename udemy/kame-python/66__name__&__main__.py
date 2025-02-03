# __main__
import mymodule
mymodule.myfunc()
# __name__が属しているプログラムが実行されたら、__name__に__main__が入る
print(__name__)
# mymodule.pyの__name__はimportされると自分のモジュール名が入る
"""
モジュール開発中は以下ようなif文を通るプログラムを書いてコマンドを叩く
外から呼ぶ時は実行されないようにする
if __name__ == "__main__":
    print(f"mymodule.__name__:{__name__}")
"""