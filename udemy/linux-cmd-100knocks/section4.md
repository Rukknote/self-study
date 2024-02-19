## セクション4で学んだことメモ

### ファイル操作
* mkdir
  * 新たにディレクトリを作るコマンド
  * -p：複数の階層のディレクトリを作るためのオプション（p:parents)
    * 例：
    ```
    ~/Desktop/lesson > mkdir -p sales/2022/1
    ~/Desktop/lesson > cd sales/2022/1 
    ~/Desktop/lesson/sales/2022/1 > 
    ```
* touch
  * ファイルを新規作成するコマンド
  * 本来ファイルのタイムスタンプを変更するための機能
    * 指定したファイルが存在しない場合に新規がファイルが生成される（空ファイル）
* rm/rmdir
  * rm：ファイルを削除するコマンド
    * -r：中身があるディレクトリを削除するためのオプション（r:recursive（再起的な））
  * rmdir：ディレクトリを削除するコマンド
    * 中身があるディレクトリは削除できない
  * 基本的にはrmコマンドを使う、例外的にからのディレクトリだけに使えるのはrmdirコマンド
    * 例
    ```
    ~/Desktop/lesson > ls
    newdir  newfile sales
    ~/Desktop/lesson > rm newfile 
    ~/Desktop/lesson > ls
    newdir sales
    ~/Desktop/lesson > rmdir newdir 
    ~/Desktop/lesson > ls
    sales
    ~/Desktop/lesson > rmdir sales 
    rmdir: sales: Directory not empty
    ~/Desktop/lesson > rm -r sales 
    ~/Desktop/lesson > ls
    ```
* cat
  * ファイルの中身を表示するコマンド
  * catはconcatenate（連結する）の略
  * 以下のようにファイルを複数指定すると、ファイルを連結して順番に表示する
    * 例
    ```
    ~/Desktop/lesson > cat /etc/zshrc /etc/zprofile 
    (/etc/zshrcの中身が出力される)
    # System-wide profile for interactive zsh(1) shells.
    ・・・
    (/etc/zprofile の中身が出力される)
    # System-wide profile for interactive zsh(1) login shells.
    ```
* less
  * スクロール表示するコマンド
    * space：1画面単位で下にスクロール
    * b：1画面単位で上にスクロール
    * j：1行単位で下にスクロール
    * k：1行単位で上にスクロール
  * lessはmoreの対義語
    * moreというスクロール表示するためのコマンドをより使いやすくしたものがless
    * moreでできることはlessで全てできる