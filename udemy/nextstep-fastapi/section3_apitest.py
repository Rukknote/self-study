import requests
url = "https://jsonplaceholder.typicode.com/posts"
res = requests.get(url)
print(f"成功したか？：{res.status_code}")
"""
成功したか？：200
"""

#resの中身を確認
print(res.json()[0])
"""
1番目のデータを確認
{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
~/g/self-study/u
"""

#条件付きで抽出可能（idが3のもの）
params = {
    "id": 3
}
res = requests.get(url, params)
print(f"成功したか？：{res.status_code}")
print(res.json())
"""
成功したか？：200
[{'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}]
"""