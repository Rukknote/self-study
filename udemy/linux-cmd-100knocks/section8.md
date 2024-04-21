## セクション8で学んだことメモ

### 標準入出力の活用（リダイレクトとパイプ）
* 標準入出力（stdio（standard input output））
  * 標準入力（stdin）、標準出力（stdout）、標準エラー出力（stderr）の3つをまとめたもの
  * 標準入力（stdin）
    * プログラムの標準的な入力、キーボードやファイルなどが使われる
  * 標準出力（stdout）
    * プログラムの標準的な出力、ディスプレイやファイルなどが使われる
  * 標準エラー出力（stderr）
    * プログラムのエラーメッセージを出力するためのもの
    * 標準出力と同じく、ディスプレイやファイルなどが使われる
  * メリット
    * コマンドは、あくまでも標準入力から受け取って標準出力に出すことを一般化することでコマンド自体を変更することなく入出力を変更できる
* リダイレクト
  * 標準入出力を切り替えること
    * 例：標準入力をキーボードからファイルに変更、標準出力をディスプレイからファイルに変更
      * `ls`コマンドの実行結果がファイルに格納されている
	  ```
	  rukk@rukk-VirtualBox:~$ ls
	  example.sh  snap      	テンプレート  ドキュメント  ピクチャ  	公開
	  file    	ダウンロード  デスクトップ  ビデオ    	ミュージック
	  rukk@rukk-VirtualBox:~$ ls > ls.txt
	  rukk@rukk-VirtualBox:~$ ls
	  example.sh  ls.txt  ダウンロード  デスクトップ  ビデオ	ミュージック
	  file    	snap	テンプレート  ドキュメント  ピクチャ  公開
	  rukk@rukk-VirtualBox:~$ cat ls.txt
	  example.sh
	  file
	  ls.txt
	  snap
	  ダウンロード
	  テンプレート
	  デスクトップ
	  ドキュメント
	  ビデオ
	  ピクチャ
	  ミュージック
	  公開
	  ```
    * 例：crontabというファイルが`cat`コマンドの入力になる
      * `cat /etc/crontab`と同じ結果になる
	  ```
	  rukk@rukk-VirtualBox:~$ cat < /etc/crontab
	  # /etc/crontab: system-wide crontab
	  # Unlike any other crontab you don't have to run the `crontab'
	  # command to install the new version when you edit this file
	  # and files in /etc/cron.d. These files also have username fields,
	  # that none of the other crontabs do.
	  （以下、省略）
	  ```
  * 標準エラー出力
    * エラー出力を`2>`以降に続くファイルに保存できる（fileがないとき）
    ```
    rukk@rukk-VirtualBox:~$ cat ls.txt file 2> error.txt
	example.sh
	file
	ls.txt
	snap
	ダウンロード
	テンプレート
    （以下、省略）
	rukk@rukk-VirtualBox:~$ cat error.txt
	cat: file: そのようなファイルやディレクトリはありません
    ```
  * リダイレクトの書き方
    * `< file`：標準入力を`file`に変更
    * `> file`：標準出力を`file`に変更
      * 新規のファイル名の時に使用（既存のファイルの場合、上書き保存される）
      ```
      rukk@rukk-VirtualBox:~$ cat ls.txt file2 2> error.txt
      example.sh
      file
      ls.txt
      snap
      ダウンロード
      テンプレート
      （以下、省略）
      rukk@rukk-VirtualBox:~$ cat error.txt
      cat: file2: そのようなファイルやディレクトリはありません
      ```
    * `2> file`：標準エラー出力を`file`に変更
    * `>> file`：標準出力の出力を`file`の末尾に追記
    * `2>> file`：標準エラー出力の出力を`file`の末尾に追記
      * 既存のファイルの場合、末尾に追記する
      ```
      rukk@rukk-VirtualBox:~$ cat ls.txt file 2>> error.txt
      example.sh
      file
      ls.txt
      snap
      ダウンロード
      テンプレート
      （以下、省略）
      rukk@rukk-VirtualBox:~$ cat error.txt
      cat: file2: そのようなファイルやディレクトリはありません
      cat: file2: そのようなファイルやディレクトリはありません
      ```
    * `>file 2>&1`：標準出力と標準エラー出力を`file`に変更
      * `error.txt`に書かれていた内容（標準出力）に新たなエラー（`aaaaa`）を追記した`output.txt`が出力される（標準エラー出力）
    ```
    rukk@rukk-VirtualBox:~$ cat error.txt aaaaa > output.txt 2>&1
    rukk@rukk-VirtualBox:~$ cat output.txt
    cat: file2: そのようなファイルやディレクトリはありません
    cat: file2: そのようなファイルやディレクトリはありません
    cat: aaaaa: そのようなファイルやディレクトリはありません
    ```
  * リダイレクトの活用
    * エラーメッセージだけを確認したい
      * 例：`file`という存在しないファイルに対するエラーを確認する
        * 標準エラー出力を出さない場合、標準出力も出て長くなる
        ```
        rukk@rukk-VirtualBox:~$ cat /etc/crontab fiie
		# /etc/crontab: system-wide crontab
		# Unlike any other crontab you don't have to run the `crontab'
		# command to install the new version when you edit this file
		# and files in /etc/cron.d. These files also have username fields,
		# that none of the other crontabs do.

		SHELL=/bin/sh
		# You can also override PATH, but by default, newer versions inherit it from the environment
		#PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

		# Example of job definition:
		# .---------------- minute (0 - 59)
		# |  .------------- hour (0 - 23)
		# |  |  .---------- day of month (1 - 31)
		# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
		# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
		# |  |  |  |  |
		# *  *  *  *  * user-name command to be executed
		17 *    * * *    root	cd / && run-parts --report /etc/cron.hourly
		25 6    * * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
		47 6    * * 7    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
		52 6    1 * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
		#
		cat: fiie: そのようなファイルやディレクトリはありません
        ```
        * 標準エラー出力のみが出力され、エラーメッセージのみ確認できる
        ```
        rukk@rukk-VirtualBox:~$ cat /etc/crontab file > /dev/null
        cat: file: そのようなファイルやディレクトリはありません
	    ```
	      * `/dev/null`はスペシャルファイルと呼ばれる特殊なファイル
	        * 入力先に指定すると、何もデータを返さない
	        * 出力先に指定すると、書き込まれたデータをすべて破棄する
	      * 上記の性質から、`/dev/null`は以下の用途で用いられる
	        * エラーメッセージのみを表示したい（`> /dev/null`）
	        * エラーメッセージを非表示にしたい（`2> /dev/null`）
* パイプライン
  * あるコマンドの標準出力を標準入力に渡すことで複雑な処理が可能（`|`で繋げる）
    * 行番号付きで出力する（`ls`の出力を`cat`に渡して行番号を出力）
    ```
    ~/Desktop/lesson > ls / | cat -n
     1	Applications
     2	Library
     3	System
     4	Users
     5	Volumes
     6	bin
     7	cores
     8	dev
     9	etc
    10	home
    11	opt
    12	private
    13	sbin
    14	tmp
    15	usr
    16	var
    ```