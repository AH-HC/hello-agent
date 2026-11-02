# 五种基本类型
# n = 42              # int     整数
# pi = 3.14           # float   小数
# name = "胡超"        # str     字符串
# ok = True           # bool    布尔
# nothing = None      # NoneType 空值


# print(type(42))
# print(type(3.14))
# print(type("42"))
# print(type(True))
# print(type(None))
# print(type(n))





# int("42")       # 42     字符串 → 整数
# str(42)         # "42"   整数 → 字符串
# float("3.14")   # 3.14   字符串 → 小数
# int(3.9)        # 3      小数 → 整数（截断，不四舍五入）


# f-string
# name = '三体'
# author= '刘慈欣'
# pi = 3.14159265357

# print(name)
# print(f"{name}")
# print(f"{name:>10}|")
# print(f"{name:<10}|")
# print(f"{name:^10}|")

# print(f"{pi:.2f}")
# print(f"{pi:.0f}")
# print(f"{0.856:.1%}")

# books = ["三体","活着","人类简史"]
# for b in books:
#     print(f'{b:<12}|')


# 四种容器
# 1.list(有序，可修改)
# books.append("三体2")
# books.insert(0,"白鹿原")
# books.remove("活着")
# print(len(books))
# for a in books:
#     print(f"{a:<2}|")

# 2.dict
# book = {
#     "title":'三体',
#     "author":"小刘",
#     "year":2008,
#     "read":True
# }

# print(book["title"])
# print(book.get("pages"))
# print(book.get("pages",1))

# 3.tuple（有序，不可修改）
# point = (3,5)
# print(point[0])
# point[0] = 10 Error

# 4.set(自动去重)
# tags = {"ai","python","ai","agent"}
# print(tags)
# print("ai" in tags)

# print(books[0])
# print(books[-1])
# print(books[0:2])
# books.append("122121")
# print(books[2:])
# print(books[::-1])





books = [
    {"title": "三体", "author": "刘慈欣", "year": 2008, "read": True},
    {"title": "活着", "author": "余华", "year": 1993, "read": False},
    {"title": "人类简史", "author": "赫拉利", "year": 2011, "read": False},
]

# print(f"{'书名':<12}{"作者":<12}{"年份":<12}状态")
# for b in books:
#     print(f"{b['title']:<12}{b['author']:<12}{b["year"]:<12}{'已读'if(b["read"]) else '未读'}")


# 对齐方法
def pad(text, width):
    """按显示宽度补空格：中文算 2 列，英文算 1 列"""
    text = str(text)
    w = 0
    for c in text:
        if ord(c) > 127:    # 非 ASCII 字符（中文、日文等）
            w += 2
        else:
            w += 1
    return text + " " * max(0, width - w)


print(f"{pad('书名', 14)}{pad('作者', 12)}{pad('年份', 8)}{pad('状态', 6)}")
print("-" * 40)

for b in books:
    status = "已读" if b["read"] else "未读"
    print(f"{pad(b['title'], 14)}{pad(b['author'], 12)}{pad(b['year'], 8)}{pad(status, 6)}")

unread = 0
for b in books:
    if not b["read"]:
        unread += 1

print(f"\n未读：{unread} 本")