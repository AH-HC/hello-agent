import requests

# 三个状态码实验
urls = [
    ("正常","https://api.github.com/users/AH-HC"),
    ("404 路径不存在", "https://api.github.com/users/this-user-does-not-exist-xyz-123"),
    ("500 服务端错误", "https://httpbin.org/status/500"),
    ("403 无权限", "https://httpbin.org/status/403"),
]

for label, url in urls:
    try:
        r = requests.get(url,timeout = 10)
        print(f"{label:20}->{r.status_code}")
    except requests.exceptions.Timeout:
        print(f"{label:20} → 超时")
    except requests.exceptions.ConnectionError:
        print(f"{label:20} → 连不上")


# 超时实验
try:
    r = requests.get("https://httpbin.org/delay/10",timeout=1)
    print("成功：", r.status_code)
except requests.exceptions.Timeout:
    print("超时了——这就是不设 timeout 会一直等的原因")