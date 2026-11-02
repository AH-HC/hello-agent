import json

FILE = "books.json"

# 标记已读 / 未读
def mark_read(books, title, read = True):
    for b in books:
        if b["title"] == title:
            b["read"] = read
            return True
    return False

# 删除书籍
def delete_book(books,title):
    for b in books:
        if b["title"] == title:
            books.remove(b)
            return True
    return False

# 对齐
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

# 列出所有书籍
def list_all(books): 
    print(f"{pad('书名',12)}{pad('作者',12)}{pad('年份',12)}状态")
    print("-" * 50)
    for b in books:
        if(b["read"]):
            status = "已读"
        else:
            status = "未读"
        print(f"{pad(b["title"],12)}{pad(b["author"],12)}{pad(b["year"],12)}{status}")

# 添加书籍
def add_book(books, title, author, year=2026, read=False):
    """添加一本书。成功返回 True，书名已存在返回 False"""
    for b in books:
        if b["title"] == title:
            return False

    books.append({
        "title": title,
        "author": author,
        "year": year,
        "read": read,
    })
    return True


# 按作者筛选
def filter_by_author(books,author):
    """ 按作者筛选书籍 """
    return [b for b in books if b["author"] == author]

# 保存书单
def save_books(books):
    """保存书单到文件"""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)

# 读取书单
def load_books():
    """读取书单，文件不存在时返回空列表"""
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

books = load_books()

# 菜单
while True:
    print("\n=== 书单管理器 ===")
    print("1. 查看全部   2. 添加   3. 按作者筛选")
    print("4. 标记已读   5. 删除   6. 退出")

    cmd = input("请输入命令：").strip()

    if cmd == "6":
        print("退出程序")
        break

    elif cmd == "1":
        list_all(books)

    elif cmd == "2":
        title = input("书名：").strip()
        if not title:
            print("书名不能为空")
            continue

        author = input("作者：").strip()
        year = input("年份（回车用默认 2026）：").strip()
        read_in = input("已读？(y/n)：").strip().lower()

        if year:
            ok = add_book(books, title, author, int(year), read_in == "y")
        else:
            ok = add_book(books, title, author, read=read_in == "y")

        if ok:
            save_books(books)
            print(f"已添加《{title}》")
        else:
            print(f"《{title}》已存在，未添加")
    elif cmd == "3":
        author = input("作者名：").strip()
        result = filter_by_author(books, author)
        if result:
            list_all(result)
        else:
            print(f"没有找到作者「{author}」的书")
    elif cmd == "4":
        title = input("要标记的书名：").strip()
        mark = input("标记为已读？(y=已读 / n=未读)：").strip().lower()
        if mark_read(books, title, mark == "y"):
            save_books(books)
            print(f"已更新《{title}》的状态")
        else:
            print(f"没有找到《{title}》")
    elif cmd == "5":
        title = input("要删除的书名：").strip()
        if delete_book(books, title):
            save_books(books)
            print(f"已删除《{title}》")
        else:
            print(f"没有找到《{title}》")

    else:
        print("无效命令，请重新输入")


