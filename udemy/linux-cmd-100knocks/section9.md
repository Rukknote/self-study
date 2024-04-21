## セクション9で学んだことメモ

### フィルタによるテキスト処理
* wc（word count）
  * 文字数や行数を数えるコマンド
    * 例：行数を数える（`l`（lines）オプションが必要）→23行とわかる
    ```
    rukk@rukk-VirtualBox:~$ wc -l /etc/crontab
    23 /etc/crontab
    ```
    * 例：文字数を数える（`w`（words）オプションが必要）→206文字とわかる
    ```
    rukk@rukk-VirtualBox:~$ wc -w /etc/crontab
    206 /etc/crontab
    ```
  * よく使うケース：ディレクトリ内のファイルやディレクトリの数を数えるとき
    * 例：rootディレクトリにあるディレクトリ数を数える→25個あることがわかる
      * `ls /`の出力に対して行数をカウント
    ```
    rukk@rukk-VirtualBox:~$ ls / | wc -l
    25
    rukk@rukk-VirtualBox:~$ ls /
    bin   cdrom  etc   lib  lib64   lost+found  mnt  proc  run   snap  swapfile  tmp  var
    boot  dev home  lib32  libx32  media    opt  root  sbin  srv   sys    usr
    ```

* sort
  * 指定した順に並び替えるコマンド
    * 例：アルファベット順とその反対（`- r`（reverse）オプション）の順
    ```
    rukk@rukk-VirtualBox:~$ sort word.txt
    akamatsu
    inoue
    mishima
    shinfuji
    rukk@rukk-VirtualBox:~$ sort -r word.txt
    shinfuji
    mishima
    inoue
    akamatsu
    ```
    * 例：数字を順番に並べるときは`- n`（number）オプション）、逆順は`- rn`を使う
    ```
    rukk@rukk-VirtualBox:~$ sort num.txt
    0
    1
    10
    11
    2
    3
    4
    5
    6
    7
    8
    9
    rukk@rukk-VirtualBox:~$ sort -n num.txt
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    rukk@rukk-VirtualBox:~$ sort -rn num.txt
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0
    ```

* uniq
  * 重複する値を取り除くコマンド
    * 例：隣り合う数値で重複があれば取り除く（連続していない行では取り除けない）
    ```
    rukk@rukk-VirtualBox:~$ cat num.txt
    0
    1
    2
    1
    3
    4
    4
    5
    4
    5
    6
    7
    1
    8
    9
    10
    11
    rukk@rukk-VirtualBox:~$ uniq num.txt
    0
    1
    2
    1
    3
    4
    5
    4
    5
    6
    7
    1
    8
    9
    10
    11
    rukk@rukk-VirtualBox:~$
    ```
    * 例：連続していない行でも重複する数値を取り除く場合、`sort`コマンドを使う
    ```
    rukk@rukk-VirtualBox:~$ sort -n num.txt
    0
    1
    1
    1
    2
    3
    4
    4
    4
    5
    5
    6
    7
    8
    9
    10
    11
    rukk@rukk-VirtualBox:~$ sort -n num.txt | uniq
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    ```
    * 例：uniqの`-c`オプションで重複回数をカウントする（右の列が要素）
    ```

    rukk@rukk-VirtualBox:~$ sort -n num.txt | uniq -c
    1
    1 0
    3 1
    1 2
    1 3
    3 4
    2 5
    1 6
    1 7
    1 8
    1 9
    1 10
    1 11
    ```
    * 例：重複回数をカウントし、重複回数の多い順にする
    ```
    rukk@rukk-VirtualBox:~$ sort -n num.txt | uniq -c | sort -nr
    3 4
    3 1
    2 5
    1 9
    1 8
    1 7
    1 6
    1 3
    1 2
    1 11
    1 10
    1 0
    1
    ```

* head
  * 指定した値の先頭の数だけ出力するコマンド
    * 例：先頭3つだけ出力する（デフォルトは10）
    ```
    rukk@rukk-VirtualBox:~$ sort -n num.txt | uniq -c | sort -nr | head -n 3
    3 4
    3 1
    2 5
    ```

* tail
  * 指定した値の末尾の数だけ出力するコマンド
    * 例：末尾3つだけ出力する（デフォルトは10）
    ```
    rukk@rukk-VirtualBox:~$ sort -n num.txt | uniq -c | sort -nr | tail -n 3
    1 10
    1 0
    1 
    ```
  * `-f`オプションをつけることで、ファイルの変更を監視できる
    * 例：別のタブで実行したfileへの変更を出力する
    ```
    rukk@rukk-VirtualBox:~$ tail -f logfile
    bin
    boot
    cdrom
    dev
    ```