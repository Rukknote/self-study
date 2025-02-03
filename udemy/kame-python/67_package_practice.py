"""
パターン1
他のパッケージとモジュール名が被らないようにすることに注意
from myfirstpackage import module1, module2
module1.myfunc()
module2.myfunc()
"""


"""
パターン2
一番安全
import myfirstpackage.module1
import myfirstpackage.module2
myfirstpackage.module1.myfunc()
myfirstpackage.module2.myfunc()

output:
This is myfunc from module1!
This is myfunc from module2!
"""
from myfirstpackage.module1 import myfunc
# from myfirstpackage.module2 import myfunc は使えない
myfunc()

"""
module1のmyfuncは、myfirstpackage.module1.myfuncという名前空間に属する
そのため、myfirstpackage.module2.myfuncは上と属する名前空間が異なるので別物として認識できる

異なるパスに存在する同盟のパッケージを共通のものとしてまとめることが可能（ただし処理は遅い）
理由がなければ__init__.pyを作って通常のパッケージとする
"""

import myfirstpackage
myfirstpackage.myfunc()#__init__.pyでfrom myfirstpackage.subdir.module2 import *と定義することでmodule2を呼べた
"""
1. import myfirstpackageを実行
2. myfirstpackage/__init__.pyを実行
3. from myfirstpackage.subdir.module2 import *を実行
すると、myfirstpackage.myfunc()でmodule2に関する内容が実行される
"""

from myfirstpackage.subdir import *
myfunc2()