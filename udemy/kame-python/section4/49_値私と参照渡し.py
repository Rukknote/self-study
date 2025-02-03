def add_nums(a, b):
    # one/twoと同じID　→　Pythonは基本的に参照渡し
    print(f"a ID:{id(a)}")
    print(f"b ID:{id(b)}")
    return a + b

one = 1
two = 2

print(f"one ID:{id(one)}")
print(f"two ID:{id(two)}")
print(add_nums(one, two))
print(f"add_nums ID:{id(add_nums(one, two))}")

def add_fruit(fruits, fruit):
    print(f"変更前のID:{id(fruits)}")
    fruits.append(fruit)
    print(f"変更後のID:{id(fruits)}")
    return fruits

myfruits = ["apple", "banana", "peach"]
myfruit = "lemon"
print(f"呼び出し前のmyfruits:{myfruits}")
add_fruit(myfruits, myfruit)
print(f"呼び出し後のmyfruits:{myfruits}") #mutable（変更可能）な場合、関数の中でリストが更新される可能性がある