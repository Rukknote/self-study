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
  * 文字列検索
    * /文字列：指定した文字列を検索
    * n：次の検索結果に移動
    * Shift + n：前の検索結果に移動
  * lessはmoreの対義語
    * moreというスクロール表示するためのコマンドをより使いやすくしたものがless
    * moreでできることはlessで全てできる
* テキストファイルとバイナリファイル
  * バイナリファイル
    * 2進数で書かれたファイル、実行中の変換がなく高速に実行可能だが人は読めない（編集不可）
  * テキストファイル
    * 人に読める言葉で書かれたファイル、実行中に変換が必要のため実行速度はバイナリファイルよりも遅い
  * 試しに以下を実行すると文字化けする
  ```
  cat /bin/bash
  ```
    * 以下を実行すると8進数で出力される
    ```
    od /bin/bash
    ```
    * bashなどは変更される機会はないためバイナリファイルとして用意する
* cp
  * ファイル・ディレクトリをコピーするコマンド
    * cp file cpfile
    ```
    cp コピー元 コピー先
    ```
    * 2つのファイルを指定するディレクトリにコピーできる
    ```
    ~/Desktop/lesson > ls
    file  file1 file2
    ~/Desktop/lesson > cp file1 file2 file
    ~/Desktop/lesson > ls file
    file1 file2
    ```
    * ディレクトリをコピーできる
    ```
    ~/Desktop/lesson > ls        
    dir1
    ~/Desktop/lesson > cp -r dir1 dir2
    ~/Desktop/lesson > ls
    dir1 dir2
    ```
* mv
  * ファイル名の変更とファイル名とディレクトリ移動するコマンド
    * ファイル名を変更できる
    ```
    ~/Desktop/lesson > touch file
    ~/Desktop/lesson > mv file renamefile
    ~/Desktop/lesson > ls
    dir1       dir2       renamefile
    ```
    * ファイルを指定したディレクトリに移動
    ```
    ~/Desktop/lesson > ls
    dir1       dir2       renamefile
    ~/Desktop/lesson > mv renamefile dir1
    ~/Desktop/lesson > ls
    dir1 dir2
    ~/Desktop/lesson > ls dir1
    renamefile
    ```
    * ディレクトリを指定したディレクトリに移動
    ```
    ~/Desktop/lesson > ls  
    dir1 dir2
    ~/Desktop/lesson > mv dir1 dir2
    ~/Desktop/lesson > ls dir2 
    dir1
    ```
    * 2つのファイルを1つのディレクトリに移動できる
    ```
    mv file1 file2 dir1
    ```
* ブレース展開
  * ブレースとは{}（中括弧）の意味
  * ファイルを1度に複数作成できる
  ```
  ~/Desktop/lesson > ls    
  dir2
  ~/Desktop/lesson > touch file{1..10}
  ~/Desktop/lesson > ls
  dir2   file1  file10 file2  file3  file4  file5  file6  file7  file8  file9
  ~/Desktop/lesson > echo {1..5}.txt 
  1.txt 2.txt 3.txt 4.txt 5.txt
  ```
* パス名展開
  * ディレクトリにあるファイルを複数指定できる（アスタリスクは任意という意味）
  ```
  ~/Desktop/lesson > ls
  dir2   file1  file10 file2  file3  file4  file5  file6  file7  file8  file9
  ~/Desktop/lesson > echo file*
  file1 file10 file2 file3 file4 file5 file6 file7 file8 file9
  ~/Desktop/lesson > rm file*
  ~/Desktop/lesson > ls
  dir2
  ```
  * ?は任意の文字数を指定できる（例：file10だけを削除）
  ```
  ~/Desktop/lesson > ls
  dir2   file1  file10 file2  file3  file4  file5  file6  file7  file8  file9
  ~/Desktop/lesson > echo file?
  file1 file2 file3 file4 file5 file6 file7 file8 file9
  ~/Desktop/lesson > echo file??
  file10
  ~/Desktop/lesson > rm file??
  ~/Desktop/lesson > ls
  dir2  file1 file2 file3 file4 file5 file6 file7 file8 file9
  ```
* 記号を文字として使う
  * 「~」をホームディレクトリではなく文字として使う場合「\（バックスラッシュ）」または「''」、「""」をつける
  ```
  ~/Desktop/lesson > echo ~ 
  /Users/rukk
  ~/Desktop/lesson > echo \~
  ~
  ~/Desktop/lesson > echo '~'
  ~
  ~/Desktop/lesson > echo "~"
  ~
  ```
    * \：右1文字を展開しない
    * ''：この中のすべての文字を展開しない
    * ""：この中では「!」「$」「`」だけを展開
* リンク
  * ファイルに別名をつける機能
  * ハードリンク
    * ファイルの実体に名前をつける（ディレクトリにはつけられないので実用的ではない）
    ```
    ~/Desktop/lesson > cat file1
    test%                                                                                            
    ~/Desktop/lesson > ln file1 cp_file1
    ~/Desktop/lesson > ls
    cp_file1 dir2     file1
    ~/Desktop/lesson > cat cp_file1 
    test%
    ```
    * 1つの実体にファイル名が1つや2つあるものがある（-rw-r--r--  2 rukkは、2つある）
    ```
    ~/Desktop/lesson > ls -l
    total 16
    -rw-r--r--  2 rukk  staff   4  2 19 23:51 cp_file1
    drwxr-xr-x  3 rukk  staff  96  2 19 22:00 dir2
    -rw-r--r--  2 rukk  staff   4  2 19 23:51 file1
    ```
    * rmはファイルやディレクトリではなくハードリンクを削除するコマンド
      * ハードリンク（cp_file1）を削除すると、file1のハードリンクのカウントが2→1へ減っている
      * ファイルの実体に紐付くハードリンクがなくなった時点で、実体もなくなる
      ```
      ~/Desktop/lesson > rm cp_file1
      ~/Desktop/lesson > ls -l
      total 8
      drwxr-xr-x  3 rukk  staff  96  2 19 22:00 dir2
      -rw-r--r--  1 rukk  staff   4  2 19 23:51 file1
      ```
  * シンボリックリンク
    * 名前に名前を結びつける
      * 実体に紐づいている名前と名前を紐づけられるので、シンボリックリンクを削除しても実体に影響はない
      * 長いパス（~/dir1/dir2）に別名「file」という名前で呼び出せるようにすればパス指定が楽になる
    * シンボリックリンクは実体がなくても作れる（名前と名前を紐づけるため）
    * `ln -s`でシンボリックを作成し、`ls -F`で作成されていることを確認
      * `ls -l`でハードリンクカウント数は1のままで、名前が紐づけられていることがわかる
      * `rm`で削除するとシンボリックリンクのみ削除され、ハードリンクのカウントに影響ない
      ```
      ~/Desktop/lesson > ls
      dir2  file1
      ~/Desktop/lesson > ln -s file1 file1link
      ~/Desktop/lesson > ls -F
      dir2/      file1      file1link@
      ~/Desktop/lesson > ls -l
      total 8
      drwxr-xr-x  3 rukk  staff  96  2 19 22:00 dir2
      -rw-r--r--  1 rukk  staff   4  2 19 23:51 file1
      lrwxr-xr-x  1 rukk  staff   5  2 21 19:15 file1link -> file1
      ~/Desktop/lesson > rm file1link 
      ~/Desktop/lesson > ls -l
      total 8
      drwxr-xr-x  3 rukk  staff  96  2 19 22:00 dir2
      -rw-r--r--  1 rukk  staff   4  2 19 23:51 file1
      ```
    * 活用例
      * 深い階層に作成したcp_fileのディレクトリに「testdata」と名前を紐づけて、短い名前で実行できる
      ```
      ~/Desktop/lesson > mkdir -p dir1/dir2/dir3
      ~/Desktop/lesson > subl file
      ~/Desktop/lesson > cp file dir1/dir2/dir3/cp_file
      ~/Desktop/lesson > cat dir1/dir2/dir3/cp_file 
      test%
      ~/Desktop/lesson > ln -s dir1/dir2/dir3/cp_file testdata
      ~/Desktop/lesson > ls -F
      testdata@ dir1/    file
      ~/Desktop/lesson > cat testdata                         
      test%  
      ```
      * ファイルを移動させても元のディレクトリをシンボリックリンクにすることで指定できる
      ```
      ~/Desktop/lesson > mkdir hoge
      ~/Desktop/lesson > ls
      dir1 file hoge
      ~/Desktop/lesson > mv dir1/dir2/dir3/cp_file hoge
      ~/Desktop/lesson > ls hoge 
      cp_file
      ~/Desktop/lesson > ls dir1/dir2/dir3 
      ~/Desktop/lesson > ls                   
      dir1 file hoge
      ~/Desktop/lesson > ln -s ~/Desktop/lesson/hoge/cp_file dir1/dir2/dir3/cp_file
      ~/Desktop/lesson > cat dir1/dir2/dir3/cp_file 
      test% 
      ```
      * シンボリックリンクは絶対パスの指定が良い
        * 相対パスで書いた場合、シンボリックリンクからの相対パスとして考えられるため
        ```
        ~/Desktop/lesson > ls -l dir1/dir2/dir3/        
        total 0
        lrwxr-xr-x  1 rukk  staff  39  2 21 21:33 cp_file -> /Users/rukk/Desktop/lesson/hoge/cp_file
        ```