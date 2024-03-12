## セクション10で学んだことメモ

### マルチタスク（プロセスとジョブ）
* プロセス
  * メモリ上で実行状態にあるプログラム（ファイル）のこと
    * コマンドの状態はディスクに保存されたファイル
    * シェルからコマンドを実行するとLinuxカーネルはディスクからコマンドのファイルを読み出してメモリに格納する
    * そのメモリに格納された内容に従い、CPUがプログラムを実行
    * ここで、メモリ上で実行状態にあるプログラムのことをプロセスという
      * Linuxカーネルから見た時の処理の単位とも言える

* ジョブ
  * シェルのコマンドラインに入力している1つの行のこと
    * シェルから見た処理の単位とも言える
    * コマンドが1つだけの場合、プロセスとジョブは同じ数（1つ）になる
    * 一方で、パイプラインにより2つ以上のコマンドを組み合わせると、ジョブは1つだが、プロセスはコマンドの数だけ生成する
      * 例）`ls`コマンドの出力結果を`cat`コマンドで行番号をつける
        * ジョブ、つまりコマンドラインでは1行なのでジョブは1つ
        * プロセスの観点では、コマンドが2つある
      * 例）rukk@rukk-VirtualBox:~$ ls / | cat -n | head -n 5
        * ジョブは1つ（コマンドラインが1行）
        * プロセスは3つ

* ps
  * `ps`（Process Status）はプロセスの状態を確認するコマンド
    * PID：プロセスID（システム全体でユニークな値をもつので、PIDを指定することでどのプロセスかを指定可能）
    * TTY：どのターミナルで実行したのかを表す
    * TIME：CPUの利用時間
    * CMD：COMMANDの略
    ```
    rukk@rukk-VirtualBox:~$ ps
	PID TTY      	TIME CMD
   1787 pts/0	00:00:00 bash
  44550 pts/0	00:00:00 ps
    ```
 * BSDオプション
   * ハイフンのつかないオプションのこと、`ps`コマンドで多い（ハイフン付きはUNIXオプションという）
     * `ps`はBSD/UNIXオプション両方もつ
   * 代表的なもの
     * `x`：別のターミナルやデーモンを含めたすべてのプロセスを表示
       ```
       rukk@rukk-VirtualBox:~$ ps x
		PID TTY  	STAT   TIME COMMAND
		774 ?    	Ss 	0:07 /lib/systemd/systemd --user
		790 ?    	S  	0:00 (sd-pam)
		850 ?    	Ssl	0:00 /usr/bin/pipewire
		（省略）
	  20112 ?    	SLl	0:02 /usr/lib/mozc/mozc_server
	  30951 ?    	SNl	0:40 /usr/bin/python3 /usr/bin/update-manager --no-update --no-focus-on-map
	  42798 pts/1	Ss+	0:00 bash
	  44670 ?    	Sl 	0:00 gjs /usr/share/gnome-shell/extensions/ding@rastersoft.com/ding.js -E -P /usr/share
	  44718 pts/0	R+ 	0:00 ps x
       ```
     * `a`：すべてのユーザーのプロセスを表示
     ```
     rukk@rukk-VirtualBox:~$ ps a
		PID TTY  	STAT   TIME COMMAND
		873 tty2 	Ssl+   0:00 /usr/libexec/gdm-wayland-session env GNOME_SHELL_SESSION_MODE=ubuntu /usr/bin/gnom
		883 tty2 	Sl+	0:00 /usr/libexec/gnome-session-binary --session=ubuntu
	   1787 pts/0	Ss 	0:00 bash
	  42798 pts/1	Ss+	0:00 bash
	  44728 pts/0	R+ 	0:00 ps a
     ```
     * `u`：詳細情報も含めてプロセスを表示
     ```
     rukk@rukk-VirtualBox:~$ ps u
		USER     	PID %CPU %MEM	VSZ   RSS TTY  	STAT START   TIME COMMAND
		rukk     	873  0.0  0.1 163612  3840 tty2 	Ssl+  3月08   0:00 /usr/libexec/gdm-wayland-session env GNOME
		rukk     	883  0.0  0.2 224260  4352 tty2 	Sl+   3月08   0:00 /usr/libexec/gnome-session-binary --sessio
		rukk    	1787  0.0  0.1  12428  3200 pts/0	Ss	3月08   0:00 bash
		rukk   	42798  0.0  0.1  12052  3584 pts/1	Ss+   3月10   0:00 bash
		rukk   	44732  0.0  0.1  13720  3328 pts/0	R+   00:15   0:00 ps u
     ```
     * `ua`などオプションを組み合わせることも可能
   * デーモンとは、コンピュータ上で常時起動される特定の処理を行うプロセスのこと
     * 例えば、Webサーバはいつでもリクエスト処理できるようにhttpd（HTTPデーモン）というプロセスを常時動かす

* sleep
  * 指定した秒数で遅延させるコマンド
    * 例：3秒遅延
    ```
    rukk@rukk-VirtualBox:~$ sleep 3
    ```

* `ctrl+Z`
  * jobを一時停止でき、`jobs`で停止したコマンドを確認できる
    * 1や2はジョブ番号とよばれる
  ```
  rukk@rukk-VirtualBox:~$ sleep 10
  ^Z
  [1]+  停止              	sleep 10
  rukk@rukk-VirtualBox:~$ less /etc/crontab

  [2]+  停止              	less /etc/crontab
  rukk@rukk-VirtualBox:~$ jobs
  [1]-  停止              	sleep 10
  [2]+  停止              	less /etc/crontab
  ```
  * `-l`オプション（long）でより詳細な情報を表示できる（プロセスidが出力される）
  ```
  rukk@rukk-VirtualBox:~$ jobs -l
  [1]- 46373 停止              	sleep 10
  [2]+ 46381 停止              	less /etc/crontab
  ```

* フォアグランド
  * ユーザーが操作できるような状態
    * 例：停止状態をフォアグランドに変更するために、`%`をつけてjob番号をつける
    ```
    rukk@rukk-VirtualBox:~$ jobs -l
	[1]- 46373 停止              	sleep 10
	[2]+ 46381 停止              	less /etc/crontab
	rukk@rukk-VirtualBox:~$ fg %1
	sleep 10
	rukk@rukk-VirtualBox:~$ jobs -l
	[2]+ 46381 停止              	less /etc/crontab
    ```

* バックグラウンド
  * 裏でコマンドを実行して、ユーザーが操作できるような状態（`%`をつけてjob番号をつける）
    * 例：バックグランドで`sleep`を動かしながら、`jobs`を実行する
  ```
  rukk@rukk-VirtualBox:~$ bg %3
  [3]+ sleep 60 &
  rukk@rukk-VirtualBox:~$ jobs
  [2]+  停止              	less /etc/crontab
  [3]-  実行中           	sleep 60 &
  rukk@rukk-VirtualBox:~$ jobs
  [2]+  停止              	less /etc/crontab
  [3]-  終了              	sleep 60
  ```
  * 最初からバックグラウンドで実行する場合、後ろに`&`をつける
  ```
  rukk@rukk-VirtualBox:~$ sleep 1000 &
  ```

* `ctrl+C`
  * フォアグラウンドのコマンドの実行を終了させる

* kill
  * ジョブを終了させる （バックグラウンドは`kill`が必要、job番号を指定することで終了させられる）
  ```
  rukk@rukk-VirtualBox:~$ sleep 60
  ^Z
  [3]+  停止              	sleep 60
  rukk@rukk-VirtualBox:~$ kill %3

  [3]+  停止              	sleep 60
  rukk@rukk-VirtualBox:~$ jobs
  [2]-  停止              	less /etc/crontab
  [3]+  Terminated          	sleep 60
  ```
  * プロセスidを指定することで終了させることも可能
  ```
  rukk@rukk-VirtualBox:~$ sleep 100 &
  [3] 46488
  rukk@rukk-VirtualBox:~$ kill 46488
  rukk@rukk-VirtualBox:~$ jobs
  [2]+  停止              	less /etc/crontab
  [3]-  Terminated          	sleep 100
  ```
  * `kill`コマンドの本質的な使い方は、シグナルを送信するためのコマンド
    * `l`オプションで`kill`コマンドのほかの使い方が出てくる
    ```
    rukk@rukk-VirtualBox:~$ kill -l
	 1) SIGHUP     2) SIGINT     3) SIGQUIT     4) SIGILL     5) SIGTRAP
	 6) SIGABRT     7) SIGBUS     8) SIGFPE     9) SIGKILL    10) SIGUSR1
	11) SIGSEGV    12) SIGUSR2    13) SIGPIPE    14) SIGALRM    15) SIGTERM
	16) SIGSTKFLT    17) SIGCHLD    18) SIGCONT    19) SIGSTOP    20) SIGTSTP
	21) SIGTTIN    22) SIGTTOU    23) SIGURG    24) SIGXCPU    25) SIGXFSZ
	26) SIGVTALRM    27) SIGPROF    28) SIGWINCH    29) SIGIO    30) SIGPWR
	31) SIGSYS    34) SIGRTMIN    35) SIGRTMIN+1    36) SIGRTMIN+2    37) SIGRTMIN+3
	38) SIGRTMIN+4    39) SIGRTMIN+5    40) SIGRTMIN+6    41) SIGRTMIN+7    42) SIGRTMIN+8
	43) SIGRTMIN+9    44) SIGRTMIN+10    45) SIGRTMIN+11    46) SIGRTMIN+12    47) SIGRTMIN+13
	48) SIGRTMIN+14    49) SIGRTMIN+15    50) SIGRTMAX-14    51) SIGRTMAX-13    52) SIGRTMAX-12
	53) SIGRTMAX-11    54) SIGRTMAX-10    55) SIGRTMAX-9    56) SIGRTMAX-8    57) SIGRTMAX-7
	58) SIGRTMAX-6    59) SIGRTMAX-5    60) SIGRTMAX-4    61) SIGRTMAX-3    62) SIGRTMAX-2
	63) SIGRTMAX-1    64) SIGRTMAX
    ```
    * 終了させるコマンドのとき、暗黙的に`-TERM`が入力されていた（オプションの番号でも可）
    ```
    rukk@rukk-VirtualBox:~$ kill -TERM 46488
    rukk@rukk-VirtualBox:~$ kill -9 46488
    ```