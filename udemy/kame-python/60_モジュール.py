from mymodule import myfunc, myvariable

myfunc()
print(myvariable)
"""
# 自作モジュール全体を読み込む場合
import mymodule
mymodule.myfunc() # 関数を呼べる
print(mymodule.myvariable) # global変数も呼べる
"""

# from mymodule import *
# 何をインポートしているかわからないから非推奨（別のモジュールで同じ関数名があったらpythonがどっちを確認すべきかわからなくなる）
# _関数名は呼べない