import json

data = {
    "name":"胡超",
    "skill":["Python","Git"],
    "hours_per_week":22,
    "stage":0,
    "is_learning":True,
    "note":None
}

# ------ 1.字符串版 ------
s = json.dumps(data, ensure_ascii=False,indent=2)
print("dumps输出")
print(s)

back = json.loads(s)
print("loads 还原")
print(back)

# ------ 2.文件版 ------
with open("demo.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)

with open("demo.json","r",encoding="utf-8") as f:
    from_file = json.load(f)
print("===从文件读回===")
print(from_file["skill"])

# ------ 3.对比：不加ensure_ascii ------
# 实验A：ensure_ascii 的作用
print("===不加ensure_ascii的对比===")
print(json.dumps(data))  # 中文会被转义

# 实现B：tuple静默变形
data2 = {"point":(1,2),"tags":("a","b")}
s2 = json.dumps(data2)
print("Json字符串",s2)
print("原始类型：",type(data2["point"]))
print("还原类型：",type(json.loads(s2)["point"]))  # tuple变成list了

# 实验C：三种不能转的类型
from datetime import datetime
for name, value in [
    ("set",{1,2,3}),
    ("datetime",datetime.now()),
    ("bytes",b"abc")
]:
    try:
        json.dumps({"v": value})
        print(f"{name}: 成功了")
    except TypeError as e:
        print(f"{name}: {e}")

