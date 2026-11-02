# hello-agent

我的 AI Agent 工程师学习路径，阶段 0（编程地基）的练习仓库。

按 27 周路线推进，当前处于 W1–W2：Python 语法、工具链、文件与数据格式。

## 环境要求

- Python 3.12
- 无需第三方依赖，全部使用标准库

## 快速开始

```bash
# 1. 创建并激活虚拟环境（Windows）
python -m venv .venv
.venv\Scripts\activate

# 2. 运行书单管理器
python book_manager.py
```

## 文件说明

| 文件 | 说明 |
|---|---|
| `hello.py` | Day 1：第一个脚本，练习 input 与 f-string |
| `day3_types.py` | Day 3：类型、容器、中文对齐函数 |
| `day4_book_manager.py` | Day 4：书单管理器，函数封装版（内存存储） |
| `day5_class.py` | Day 5：列表推导、字典推导、Book 类 |
| `book_manager.py` | Day 6：书单管理器完整版，支持 JSON 持久化 |
| `books.json` | 书单数据文件，由 `book_manager.py` 自动读写 |
| `day7_except.py` | Day 7：try / except / finally 执行顺序实验 |

## 书单管理器功能

`book_manager.py` 提供六项操作：

- 查看全部书籍（中文对齐表格）
- 添加书籍（书名重复时拒绝写入）
- 按作者筛选
- 标记已读 / 未读
- 删除书籍（删除不存在的书不报错）
- 数据持久化到 `books.json`，重启程序不丢失

## 学习进度

| 周次 | 主题 | 状态 |
|---|---|---|
| W1 | 环境工具链、Python 语法（类型 / 容器 / 函数 / 类）、JSON 持久化 | 已完成 |
| W2 | 文件与数据格式、HTTP 与 API 调用、asyncio 入门 | 进行中 |
| W3 | asyncio 深化、阶段 0 小项目验收 | 未开始 |
