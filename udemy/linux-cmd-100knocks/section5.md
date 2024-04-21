## セクション5で学んだことメモ

### 調べる・探すコマンド
* --help
  * linuxコマンドの使い方などを説明する
    * 例：catの使い方がわからないとき
    ```
    rukk@rukk-VirtualBox:~$ cat --help
		使用法: cat [オプション]... [ファイル]...
		ファイル (複数可) の内容を結合して標準出力に出力します。

		ファイルの指定がない場合や FILE が - の場合, 標準入力から読み込みを行います。

		  -A, --show-all       	-vET と同じ
		（以下、省略）
    ```
* man
  * 暗黙的にlsコマンドが実行され`--help`よりも詳しいマニュアルが表示される
    * 例：catの使い方がわからないとき
    ```
		CAT(1)     User Cmmands     CAT(1)
		NAME
			cat - concatenate files and print on the standard output

		SYNOPSIS
			cat [OPTION]... [FILE]...
		（以下、省略）
    ```
* find
  * 指定するディレクトリの中からファイルを探す
    * 例：カレントディレクトリよりも下にある全てのテキストファイルを検索して表示する
    ```
    rukk@rukk-VirtualBox:~$ find . -name "*.txt" -print
		./snap/firefox/common/.mozilla/firefox/slt0ovld.default/SiteSecurityServiceState.txt
		./snap/firefox/common/.mozilla/firefox/slt0ovld.default/AlternateServices.txt
		./snap/firefox/common/.mozilla/firefox/slt0ovld.default/pkcs11.txt
		./.cache/tracker3/files/last-crawl.txt
		./.cache/tracker3/files/first-index.txt

    ```
  * `""`を外すと、`*.txt`がパス名展開（複数のファイルに変換して展開）として処理されるためエラーとなる
    * `find . -name *.txt -print`だと、`-name`オプションの引数は1つしか取らない
    ```
    rukk@rukk-VirtualBox:~$ touch file.txt
		rukk@rukk-VirtualBox:~$ touch file2.txt
		rukk@rukk-VirtualBox:~$ ls
		file.txt   snap      	テンプレート  ドキュメント  ピクチャ  	公開
		file2.txt  ダウンロード  デスクトップ  ビデオ    	ミュージック
		rukk@rukk-VirtualBox:~$ find . -name *.txt -print
		find: paths must precede expression: `file2.txt'
		find: possible unquoted pattern after predicate `-name'?
    ```
    *　対処方法として、ワイルドカードとして認識させるために`""`で囲う
  * `find . -type d`でカレントディレクトリより下にあるファイル種別がディレクトリのものを探す
    * dはディレクトリの意味
    ```
    rukk@rukk-VirtualBox:~$ find . -type d
		.
		./ドキュメント
		./.local
		./.local/share
    ```
    * `-type f`はファイルを、`-type l`hはシンボリックリンクを検索する
  * 指定した名前が格納されているディレクトリを確認したいとき
    * `-a`というandを意味するオプションを追加して条件を足し合わせる（`-a`の省略可能）
    ```
    rukk@rukk-VirtualBox:~$ find . -type d -a -name share
		./.local/share
		./snap/snapd-desktop-integration/83/.local/share
		./snap/firefox/3836/.local/share
		./snap/firefox/2987/.local/share
    ```
  * 欠点
    * ファイルを1つずつ見つけていくプロセスを経て検索を行うので、かなり検索に時間がかかる
      * `time find / name "*.txt"`を実行すると出力までに21秒もかかることがわかった
	  ```
	  rukk@rukk-VirtualBox:~$ time find / name "*.txt"
	  real    0m21.514s
	  user    0m1.584s
	  sys    0m3.407s
	  ```
	  * 起点のディレクトリを順々に下り全てのディレクトリ・ファイルを探す
* locate
  * findよりも検索時間が早い検索コマンド
    * `time locate "*.txt"`を実行するとたった0.09秒で出力されることがわかった
    ```
    rukk@rukk-VirtualBox:~$ time locate "*.txt"
		real    0m0.090s
		user    0m0.000s
		sys    0m0.055s
    ```
    * あらかじめ作ったファイルのデータベースから検索を行うことで高速に検索が可能
      * 注意点：新規作成されたファイルはデータベースに含まれていない
        * 1日経つごとに更新されるが、すぐに更新したい場合はデータベースを更新するコマンドを叩く
        * `sudo updatedb`でデータベースを更新できる
  * and検索とor検索
    * andの場合：`-A`をつける必要がある
      * 例：`locate -A bash doc`
    * orの場合：何もつける必要ない
      * 例：`locate bash doc`
* grep
  * ファイルの中から特定の文字列を含む行だけを検索するコマンド
    * grep：「global regular expression print」の略
      * ファイル全体（global）のうち、正規表現（regular expression）に一致する行を出力（print）
        * 正規表現とは、特定の文字列から始める、または終わる行を検索すること
    * 例：binという文字列が含まれる行を/etc/crontabファイルで検索
    ```
    rukk@rukk-VirtualBox:~$ cat /etc/crontab
		# /etc/crontab: system-wide crontab
		# Unlike any other crontab you don't have to run the `crontab'
		# command to install the new version when you edit this file
		# and files in /etc/cron.d. These files also have username fields,
		# that none of the other crontabs do.
		（以下、省略）
		rukk@rukk-VirtualBox:~$ grep bin /etc/crontab
		SHELL=/bin/sh
		#PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
		25 6    * * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
		47 6    * * 7    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
		52 6    1 * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
		rukk@rukk-VirtualBox:~$
    ```