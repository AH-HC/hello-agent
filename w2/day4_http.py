import requests

url = "https://api.github.com/users/AH-HC"
r = requests.get(url,timeout=5)  # timeout=5 表示最多等待 5 秒

print("状态码：", r.status_code)
print("内容类型：", r.headers["Content-Type"])
print("响应体前100 字符：")
print(r.text[:100])  # r.text 是 str 类型，r.content 是 bytes 类型
print()

data = r.json()  # r.json() 是 dict 类型，r.text 是 str 类型
print("仓库数：",data["public_repos"])
print("注册时间：", data["created_at"])
print("主页：",data["html_url"])




