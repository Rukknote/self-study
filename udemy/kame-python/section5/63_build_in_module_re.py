import re
# Regular Expression(正規表現　通称RegEx)

email = "myemail@gmail.com"
matched = re.search('@\w+\.', email)#@の後ろに1文字以上の文字列と、その後ろに.があるというパターンかどうか
print(matched)
"""
<re.Match object; span=(7, 14), match='@gmail.'>
# span: index 7 ~ 14にマッチした
# match: マッチした文字列
"""

matched = re.search('@\w+\.', "mymail@gmailcom")#マッチしない場合
print(matched)
"""
マッチしない場合　Noneが返る
"""

if matched:
    print("Matched")
else:
    print("Not found")

print(re.search('[abc]', 'a'))
print(re.search('[abc]', 'apple a'))#1つのみマッチしたものを返す

print(re.search('[0-9]', 'fsf4'))#数字のマッチ

# ^　最初の文字
print(re.search('^[0-9]', 'test0'))#^ハット　という最初の文字が数字かどうか→None

# {n} n回リピート
print(re.search('^[0-9]{4}', '2024/01/31'))#最初の文字が数字かどうか4回繰り返す

# {n, m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,3}', '2024/01/31'))#{2, 3}とスペース開けたらアウト

# $ 最後の文字
print(re.search('[0-9]{2}$', '2024/07/31'))

# * 左のパターンを0回以上繰り返す
print(re.search('a*b', 'ab'))#aを0回繰り返すというパターンに対して、aは1回繰り返すのでOK
print(re.search('a*b', 'b'))#aを0回繰り返すというパターンに対して、bのみaは0回繰り返すのでOK
print(re.search('a*b', 'aaabaaa')) # <re.Match object; span=(0, 4), match='aaab'>

# + 左のパターンを1回以上繰り返す
print(re.search('a+b', 'ab'))
print(re.search('a+b', 'a'))#bがないからマッチしない
print(re.search('a+b', 'aaabaaa')) # <re.Match object; span=(0, 4), match='aaab'>

# ? 左のパターンを0回か1回繰り返す
print(re.search('a?b', 'ab'))
print(re.search('a?b', 'a'))#bがないからマッチしない
print(re.search('a?b', 'aaabaaa')) # <re.Match object; span=(2, 4), match='ab'>

# | or
print(re.search('abc|012', 'abc')) #<re.Match object; span=(0, 3), match='abc'>
print(re.search('abc|012', 'ab')) #None

# ()グループ
print(re.search('te(s|x)t', 'text')) #teとxの間が、sまたはxならOK

 # . 任意の1文字
print(re.search('h.t', 'hot')) #hとtの間に文字があればOK

# \ エスケープ
print(re.search('h\.t', 'h.t'))# .はメタキャラクターではないことを示す、<re.Match object; span=(0, 3), match='h.t'>

# \w [a-zA-Z0-9_]すべてのアルファベット、数字およびアンダースコア
print(re.search('h\wt', 'hit')) #hとtの間に1文字あればマッチ
print(re.search('h\wt', 'hiatest')) #複数あればマッチしない
print(re.search('h\wt', 'h.t')) #.はマッチしない


# Challenge1
pattern_dob = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])$"
while True:
    ch1 = input("生年月日を入力してください(yyyy/mm/dd)")
    if re.search(pattern_dob, ch1):
        print(ch1)
    else:
        print("正しいフォーマットではありません")
    break

# Challenge2
pattern_email = "^(\w|\.|-)+@(\w.|\.|-)+\.[a-zA-Z]{2,3}$"
while True:
    email = input("emailを入力してください")
    if re.search(pattern_dob, ch1):
        print(email)
    else:
        print("正しいフォーマットではありません")
    break