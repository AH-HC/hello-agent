import json

try:
    with open("demo.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    print("读取成功，数据条数：", len(data))
except FileNotFoundError:
    print("文件不存在，请先运行 day2_json.py 生成 demo.json")
except json.JSONDecodeError as e:
    print("文件格式坏了：", e)
