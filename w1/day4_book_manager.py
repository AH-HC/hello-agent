# 预计学习 分支，循环，函数
books = [
    {"title": "三体", "author": "刘慈欣", "year": 2008, "read": True},
    {"title": "活着", "author": "余华", "year": 1993, "read": False},
    {"title": "活着", "author": "余华", "year": 1993, "read": False},
    {"title": "活着", "author": "余华", "year": 1993, "read": False},
]



# 函数
def pad(text, width):
    """ 对齐：中文算2列，英文算1列 """
    text = str(text)
    w = 0
    for c in text:
        if ord(c) > 127:
            w += 2
        else:
            w += 1
    return text + " " * max(0,width - w)

def list_all(books):
    """ 列出所有书籍 """
    print(f"{pad('书名',12)}{pad('作者',12)}{pad('年份',12)}状态")
    print("-" * 50)
    for b in books:
        if(b["read"]):
            status = "已读"
        else:
            status = "未读"
        print(f"{pad(b["title"],12)}{pad(b["author"],12)}{pad(b["year"],12)}{status}")

# 统计未读
def count_unread(books):
    """ 统计未读书记数量"""
    count = 0
    for b in books:
        if b["read"] == False:
            count += 1
    return count

# 添加书籍
def add_book(books):
    """ 添加书籍 """
    title = input("请输入书名：")
    author = input("请输入作者：")
    year = int(input("请输入年份："))
    read_input = input("是否已读（y/n）：")
    read = True if read_input.lower() == 'y' else False
    books.append({"title": title, "author": author, "year": year, "read": read})
    print(f"已添加书籍：{title} by {author} ({year}) - {'已读' if read else '未读'}") 

# while循环

while True:
    print("\n=== 书单管理器 ===")
    print("1. 查看书单 2.添加 3.统计未读 4.退出" )
    cmd = input("请输入命令：").strip()
    if cmd == '4':
        print("退出程序")
        break
    elif cmd == '1':
        list_all(books)
    elif cmd == '2':
        add_book(books)
    elif cmd == '3':
        count_unread(books)
    else:
        print("无效命令，请重新输入")

result = count_unread(books)
print(result)
print(type(result))

