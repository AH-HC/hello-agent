import csv
from pathlib import Path

folder = Path("data")            #路径对象     "data" 是相对路径，folder 只是一个「指针」，指向一个可能存在、也可能不存在的位置。
folder.mkdir(exist_ok=True)      #mkdir = make directory，创建目录。exist_ok=True 的意思是：如果目录已经存在，不报错，直接跳过



# 正常文件 1：书单
with open(folder / "books.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["书名", "作者", "价格"])
    w.writerow(["人类简史", "尤瓦尔", "2014"])
    w.writerow(["思考快与慢", "卡尼曼", "2012"])
    w.writerow(["代码大全", "麦克康奈尔", "2006"])

# 正常文件 2：销售
with open (folder / "sales.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["产品", "数量", "单价"])
    w.writerow(["键盘", "10", "299"])
    w.writerow(["鼠标", "25", "89"])

# 正常文件 3：用户
with open(folder / "users.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "城市"])
    w.writerow(["张三", "北京"])
    w.writerow(["李四", "上海"])
    w.writerow(["王五", "广州"])
    w.writerow(["赵六", "深圳"])

# 坏文件：故意用 GBK 编码写，用 utf-8 读就会报错
with open(folder / "bad_gbk.csv", "w", encoding="gbk", newline="") as f:
    w = csv.writer(f)
    w.writerow(["姓名", "年龄"])
    w.writerow(["钱七", "28"])

print("测试数据已生成")
