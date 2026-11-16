# hello-agent

我的 AI Agent 工程师学习路径，阶段 0（编程地基）的练习仓库。

按 27 周路线推进，当前处于 W3：小项目交付与阶段 0 验收。

## 环境要求

- Python 3.12
- 第三方依赖：`requests`、`httpx`、`python-dotenv`
- 安装：`pip install -r requirements.txt`

## 目录结构

```
hello-agent/
├── README.md
├── requirements.txt
├── .gitignore
├── .venv/                    虚拟环境，全项目共用
├── w1/                       第一周：Python 语法与工具链
│   ├── hello.py
│   ├── day3_types.py
│   ├── day4_book_manager.py
│   ├── day5_class.py
│   ├── day7_except.py
│   ├── book_manager.py       本周核心作品
│   └── books.json
├── w2/                       第二周：文件与数据格式、HTTP、asyncio
│   ├── day1_file.py
│   ├── day2_json.py
│   ├── day2_broken.py
│   ├── day4_http.py
│   ├── day4_status.py
│   ├── day6_async.py
│   ├── batch_file_tool.py    CSV 批量处理
│   ├── make_test_data.py
│   ├── api_client.py         API 客户端
│   ├── async_fetch.py        并发抓取
│   ├── data/                 测试用 CSV
│   └── .env.example          环境变量模板
└── learning-progress/        学习日志与复盘
    └── daily-log-2026-11-01.md
```

按周分目录，周内文件平铺。文件名保留 `day` 前缀，便于对应学习清单。

## 快速开始

```bash
# 1. 创建并激活虚拟环境（Windows）
python -m venv .venv
.venv\Scripts\activate

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行第一周的书单管理器
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
python make_test_data.py
python batch_file_tool.py
```

**2. `api_client.py` —— API 客户端**

封装 `fetch()` 函数，区分超时 / 连接失败 / 4xx / 5xx。5xx 自动退避重试，4xx 立即返回。

```bash
cd w2
python api_client.py
```

密钥通过 `.env` 管理，模板见 `.env.example`。

**3. `async_fetch.py` —— 并发抓取**

对同一批 URL 分别用 `requests` 串行和 `httpx` 并发请求，对比总耗时。

```bash
cd w2
python async_fetch.py
```

实测加速比约 12 倍。目标服务限流时会返回 429，脚本用 `Semaphore` 控制并发数。

### 踩过的坑

| 问题 | 原因 |
|---|---|
| 文件生成到项目根目录 | VS Code 运行按钮的工作目录是项目根，不是 .py 所在目录 |
| 中文变成 `\u80e1\u8d85` | `json.dumps` 少了 `ensure_ascii=False` |
| CSV 每行之间多空行 | `open` 少了 `newline=""` |
| Excel 打开 CSV 乱码 | 用了 `utf-8` 而不是 `utf-8-sig` |
| 并发没生效 | `requests` 是同步库，必须换 `httpx.AsyncClient` |

## 学习进度

| 周次 | 主题 | 状态 |
|---|---|---|
| W1 | 环境工具链、Python 语法（类型 / 容器 / 函数 / 类）、JSON 持久化 | 已完成 |
| W2 | 文件与数据格式、HTTP 与 API 调用、asyncio 并发 | 已完成 |
| W3 | 小项目交付（api-inspector）、代码规范、阶段 0 验收 | 进行中 |

## 说明

- 本仓库是学习练习仓库，不追求工程完备性
- 练习代码按周归档，每周独立目录，互不依赖
- 独立作品会另建仓库，不与本仓库混放
