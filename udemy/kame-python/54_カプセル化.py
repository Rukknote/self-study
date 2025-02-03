# カプセル化（encapsulation）：外からアクセスできなようにする
def casino_entrance(age, min_age=21):
    # カジノへの入店の役割
    # 役割ごとの責任をレスポンスシビティの責任
    if age < min_age:
        print(f"{min_age}歳未満お断り")
        return
    
    def inner_casinno_entrance():
        # カジノの内容の役割
        print("ようこそカジノへ")
    
    return inner_casinno_entrance()

casino_entrance(18)