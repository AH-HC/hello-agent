# api-inspector 设计笔记

## 1. 这个工具干什么

（用一句话说清。比如：批量检查一组网址能不能访问，告诉你哪些挂了、为什么挂。）

我的答案：我有 10 个接口要天天检查，一个个点太麻烦，想让程序一次全查完.


## 2. 输入是什么

（用户要提供什么？文件格式？有几列？每列什么意思？）

我的答案：
一个 CSV 文件，两列：
- name：接口名，给人看报表时识别
- url：完整网址，程序发请求用

示例：
name,url
github_user,https://api.github.com/users/AH-HC
httpbin_500,https://httpbin.org/status/500





## 3. 输出是什么

（程序跑完，用户能看到什么？）

我的答案： 
两个层次：
【总】屏幕汇总
  总数、成功数、失败数

【分】report.csv 明细，每行一个接口，字段：
  name          接口名
  url           网址
  ok            成功还是失败
  status_code   状态码（200/404/500，超时为空）
  elapsed       耗时（秒）
  error_type    错误类型（超时/连接失败/HTTP错误）
  error_msg     错误详情

为什么要状态码：区分「我的问题（4xx）」和「对方的问题（5xx）」，
两者的处理方式完全不同。



## 4. 一条检查结果用什么装

我的选择：dataclass

理由：字段固定，用 dataclass 能在写代码时检查字段名和类型，
拼错立刻标红，不用等到运行时才 KeyError。

定义：
```python
from dataclasses import dataclass
from typing import Optional

# Optional[int] 的意思是「int 或者 None」，等价于 int | None。

@dataclass
class CheckResult:
    name: str
    url: str
    ok: bool
    status_code: Optional[int]
    elapsed: float
    error_type: Optional[str]
    error_msg: Optional[str]
```


## 5. 文件怎么分

| 文件 | 负责什么 | 不负责什么 |
|---|---|---|
| `main.py` | 主程序调用、串联流程 | 不发请求、不写文件、不做格式化 |
| `inspector.py` | 发送请求，接收结果 | 不打印任何东西、不写文件 |
| `report.py` | 根据结果输出 | 不发请求、不算业务逻辑 |
| `config.py` | 定义常用常量 | 不含任何逻辑（不写函数） |


为什么这样分：
（一句话说明你的划分原则）
一个文件只做一件事。判断标准：改一个功能时，只需要动一个文件。
具体来说：inspector.py 只管「拿到数据」，report.py 只管「展示数据」，
两者通过 CheckResult 传递，互不知道对方怎么实现。


main.py 主程序调用                      不发请求、不写文件、不做格式化
inspector.py 发送请求，接收结果          不打印任何东西、不写文件
report.py 根据结果输出                   不发请求、不算业务逻辑                 
config.py 定义需要常用字段              不含任何逻辑（不写函数，只放常量）

如果以后要加「输出 JSON 格式」，需要改哪些文件： report.py
（这题检验划分是否清晰）


## 6. 功能清单

### 必须做（MVP）

| # | 功能 | 怎么算做完了 |
|---|---|---|
| 1 | 读 CSV 文件 | 能读入 examples/targets.csv，打印出所有 name 和 url |
| 2 | 并发请求 | 5 个网址全部返回结果，`--limit` 改动后耗时明显变化 |
| 3 | 记录结果 | 每条结果含 name/url/ok/status_code/elapsed/error_type |
| 4 | 屏幕输出 | 打印汇总（总数/成功/失败）+ 每个网址一行明细 |
| 5 | 生成 report.csv | 文件生成，Excel 打开中文不乱码，行数 = 目标数 |


### 可选做（时间够再做）

| # | 功能 | 优先级 |
|---|---|---|
| 1 | 命令行参数（--input/--output/--limit/--timeout） | 高 |
| 2 | 429 退避重试 | 中 |
| 3 | 最慢 3 个目标排行 | 中 |
| 4 | errors.log 单独记录失败项 | 低 |
| 5 | 支持 JSON 输出格式 | 低 |



## 7. 数据流

### ① CSV 文件（磁盘上）
长什么样：
name,url
github_user,https://api.github.com/users/AH-HC
httpbin_500,https://httpbin.org/status/500


### ② targets（读进内存后）
长什么样：
[
    {"name": "github_user", "url": "https://api.github.com/users/AH-HC"},
    ...
]


### ③ results（请求完成后）
长什么样：
[
    CheckResult(name="github_user", ok=True, status_code=200, elapsed=0.28, ...),
    CheckResult(name="httpbin_500", ok=False, status_code=500, elapsed=0.31, ...),
]


### ④ 输出（屏幕 + 磁盘）

**屏幕汇总 + 明细**：

```text
=== 巡检完成 ===
目标总数    5
成功        2
失败        3
成功率      40.0%
平均耗时    1.85s

明细：
  github_user      成功  200  0.28s
  github_404       失败  404  0.31s
  httpbin_500      失败  500  0.29s
  httpbin_slow     失败  超时  5.01s
  bad_url          失败  连接失败  0.02s






