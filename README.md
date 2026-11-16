# hello-agent

我的 AI Agent 工程师学习路径，阶段 0（编程地基）的练习仓库。

按 27 周路线推进，当前处于 W1–W2：Python 语法、工具链、文件与数据格式。

## 环境要求

- Python 3.12
- 第三方依赖：`requests`、`httpx`、`python-dotenv`
- 安装：`pip install -r requirements.txt`




## 快速开始

```bash
# 1. 创建并激活虚拟环境（Windows）
python -m venv .venv
.venv\Scripts\activate

# 2. 运行第一周的书单管理器
cd w1
python book_manager.py
```

`book_manager.py` 用 `Path(__file__).parent / "books.json"` 定位数据文件，因此在任意目录运行都能读到同目录下的 `books.json`。

## W1 内容（w1/）

| 文件 | 说明 |
|---|---|
| `hello.py` | Day 1：第一个脚本，练习 input 与 f-string |
| `day3_types.py` | Day 3：类型、容器、中文对齐函数 |
| `day4_book_manager.py` | Day 4：书单管理器，函数封装版（内存存储） |
| `day5_class.py` | Day 5：列表推导、字典推导、Book 类 |
| `day7_except.py` | Day 7：try / except / finally 执行顺序实验 |
| `book_manager.py` | Day 6：书单管理器完整版，支持 JSON 持久化 |
| `books.json` | 书单数据文件，由 `book_manager.py` 自动读写 |

### 书单管理器功能

`w1/book_manager.py` 提供六项操作：

- 查看全部书籍（中文对齐表格）
- 添加书籍（书名重复时拒绝写入）
- 按作者筛选
- 标记已读 / 未读
- 删除书籍（删除不存在的书不报错）
- 数据持久化到 `books.json`，重启程序不丢失



## W2 内容（w2/）

| 文件 | 说明 |
|---|---|
| `day1_file.py` | Day 1：文件读写、编码对照、路径验证 |
| `day2_json.py` | Day 2：JSON 四个函数、类型映射实验 |
| `day2_broken.py` | Day 2：坏 JSON 文件处理 |
| `day4_http.py` | Day 4：HTTP 请求与响应解析 |
| `day4_status.py` | Day 4：状态码与超时实验 |
| `day6_async.py` | Day 6：asyncio 协程与并发实验 |
| `batch_file_tool.py` | Day 3：CSV 批量处理工具 |
| `make_test_data.py` | Day 3：生成测试数据 |
| `api_client.py` | Day 5：API 客户端，错误分类与退避重试 |
| `async_fetch.py` | Day 7：并发抓取对比 |

### 三个交付物

**1. `batch_file_tool.py` —— CSV 批量处理**

扫描目录下所有 CSV，统计行数、列数、表头。坏文件不中断处理，记录到 `errors.log`。

```bash
cd w2
python make_test_data.py     # 先生成测试数据
python batch_file_tool.py


## 学习进度

| 周次 | 主题 | 状态 |
|---|---|---|
| W1 | 环境工具链、Python 语法（类型 / 容器 / 函数 / 类）、JSON 持久化 | 已完成 |
| W2 | 文件与数据格式、HTTP 与 API 调用、asyncio 入门 | 进行中 |
| W3 | asyncio 深化、阶段 0 小项目验收 | 未开始 |

## 说明

- 本仓库是学习练习仓库，不追求工程完备性
- 练习代码按周归档，每周独立目录，互不依赖
- 独立作品会另建仓库，不与本仓库混放
