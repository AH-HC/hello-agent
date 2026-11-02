from pathlib import Path

p = Path("notes.txt")

#1.写入
p.write_text("第一行\n第二行\n",encoding="utf-8") 

# 2.追加
with open(p,"a",encoding="utf-8") as f:
    f.write("第三行\n")

# 3.读取
print(p.read_text(encoding="utf-8"))

# 4.存在性与大小
print("存在：",p.exists())
print("大小：",p.stat().st_size)

# 测试A
# 不写 encoding，用系统默认编码写
with open("hello.txt","w") as f:
    f.write("你好，世界\n")

# 用 utf-8 读同一个文件
try:
    print(Path("hello.txt").read_text(encoding="utf-8"))
except UnicodeDecodeError as e:
    print("读取失败：",e)

# 实验B
Path("mode.txt").write_text("你好1，世界\n",encoding="utf-8")
Path("mode.txt").write_text("你好2，世界\n",encoding="utf-8")
print(Path("mode.txt").read_text(encoding="utf-8"))