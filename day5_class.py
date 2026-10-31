books = [
    {"title": "三体", "author": "刘慈欣", "year": 2008, "read": True},
    {"title": "活着", "author": "余华", "year": 1993, "read": False},
    {"title": "人类简史", "author": "赫拉利", "year": 2011, "read": False},
]

# 列表推导
# def count(books):
#     count = 0
#     for b in books:             #遍历
#         if not b["read"]:       #筛选
#             count += 1          #收集
#     return count

# 三行代码做了三件事：遍历、筛选、收集。
#这种「从一堆东西里挑出符合条件的，收集起来」的操作，在编程里出现频率极高。Python 给它准备了一个更短的写法.


# 注意顺序：列表推导把「要什么」写在最前面，和中文语序一致——「我要（未读的书），从（books）里，筛（read 为假的）」.
# 用法1：只要某些元素（筛选）
unread = [b for b in books if not b["read"]]
print(len(unread))

for r in unread:
    print(r["title"], r["author"], r["year"])

# 用法2：只要某些字段（提取）
titles = [b["title"] for b in books]
print(titles)

# 用法3：筛选+提取
unread_titles = [b["title"] for b in books if not b["read"]]
print(unread_titles)

# 练习A
def count_unread(books):
    count = 0
    for b in books:
        if not b["read"]:
            count += 1
    return count

def count_unread2(books):
    return len([b for b in books if not b["read"]])

print(count_unread(books))
print(count_unread2(books))

# 列表推导必须有 [ ] 包着。没有方括号会报语法错误。
# result = b for b in books if not b["read"]    # SyntaxError

# 条件和表达式写反
# 表达式位置是「要什么」，if 后面才是「筛什么」。​ 两者别搞混。


# 二.字典推导 + 按作者筛选
# 1、字典推导
# 列表推导生成 list，字典推导生成 dict。结构只多一个冒号：
# {键表达式: 值表达式 for 变量 in 集合 if 条件}

titles_year = {b["title"]:b["year"] for b in books}
print(titles_year)

# 按作者筛选
def filter_by_author(books,author):
    """ 按作者筛选书籍 """
    return [b for b in books if b["author"] == author]

print("请输入cmd 1.按作者筛选 q.退出")
cmd = input("请输入命令：").strip()

if cmd == "q":
    print("退出程序")
elif cmd=="1":
    author = input("请输入作者名字:").strip()
    result = filter_by_author(books,author)
    if result:
        for b in result:
            print(b["title"])
    else:
        print("没有找到该作者的书籍")
else:
    print("无效命令，请重新输入")

# Book类
class Book:
    """ 一本书 """

    # 初始化
    def __init__(self, title, author, year = 2026, read = False):
        self.title = title
        self.author = author
        self.year = year
        self.read = read

    def is_old(self):
        return self.year < 2000

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year, "read": self.read}

# 测试
b1 = Book("第一本书","胡1")
b2 = Book("第二本书","胡2",2025,False)
b3 = Book("第三本书","胡3",1999,True)

print(b1.title,b1.author,b1.year,b1.read)
print(b2.title,b2.author,b2.year,b2.read)
print(b3.title,b3.author,b3.year,b3.read)

print(b1.is_old())
print(b2.is_old())
print(b3.to_dict())




