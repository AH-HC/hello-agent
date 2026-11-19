# api-inspector

批量检查一组 API 端点的可用性，输出状态码、耗时与错误分类。

## 安装

```bash
pip install httpx
```

## 用法

```bash
# 最简用法
python main.py

# 指定输入和并发数
python main.py -i examples/targets.csv -l 3

# 查看所有参数
python main.py --help
```

输出示例：

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
```

同时生成 `report.csv`，包含每个目标的完整结果。

## 输入格式

CSV 文件，两列：

| 列名 | 说明 |
|---|---|
| `name` | 接口名，用于在报表中识别 |
| `url` | 完整的 HTTP/HTTPS 地址 |

示例见 `examples/targets.csv`。

## 参数说明

| 参数 | 默认值 | 说明 |
|---|---|---|
| `-i, --input` | `examples/targets.csv` | 输入 CSV 路径 |
| `-o, --output` | `report.csv` | 输出 CSV 路径 |
| `-l, --limit` | `5` | 最大并发数 |
| `-t, --timeout` | `5.0` | 单个请求超时（秒） |
