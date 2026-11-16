import asyncio
import time
import httpx
import requests

# 每个请求固定延迟 1 秒，串行约 10 秒，并发约 1-2 秒
URLS = [f"https://httpbin.org/delay/1?i={i}" for i in range(10)]   #列表推导，生成 10 个字符串

def fetch_sync(url):
    """同步请求单个 URL，返回 (成功?, 耗时)"""
    start = time.time()
    try:
        r = requests.get(url,timeout=15)
        r.raise_for_status()
        return True,time.time() - start,None
    except Exception as e:
        return False,time.time() - start,f"{type(e).__name__}:{e}"

def run_sync():                             # 循环调用 10 次  串行地请求 10 个 URL，记录总耗时和成功条数。
    print("=== 串行版（requests）===")
    start = time.time()

    results = []
    for i,url in enumerate(URLS,1):         #同时给出序号和元素，序号从 1 开始。这样输出是 [1/10] 而不是 [0/10]
                                            # enumerate 是个迭代器，每次 next() 返回一个 (索引, 元素) 的元组
        ok , cost ,err = fetch_sync(url)
        results.append(ok)
        status = "成功" if ok else f"失败 [{err}]"
        print(f"  [{i}/{len(URLS)}] {status}  耗时 {cost:.2f}s")

    total = time.time() - start
    print(f"串行总耗时：{total:.2f}s")
    print(f"成功 {sum(results)} / {len(URLS)}")
    return total, results

async def fetch_async(client,url):
    """异步请求单个 URL，返回 (成功?, 耗时)"""
    start = time.time()
    try:
        r = await client.get(url,timeout = 15)   # 共用一个 client：1 次握手，后续复用连接
        r.raise_for_status()
        return True , time.time() -start,None
    except Exception as e:
        return False,time.time() -start,f"{type(e).__name__} : {e}"



    
async def run_async(limit = 5):
    print(f"\n=== 并发版（httpx，最多 {limit} 个同时）===")
    start = time.time()

    #因为一次调用是个 会出现429 频繁调用导致失败
    sem = asyncio.Semaphore(limit)      #= 最多 5 个任务能同时持有许可。第 6 个要排队等

    async def fetch_with_limit(client, url):
        async with sem:                             # 拿许可（没有就排队等）
            return await fetch_async(client, url)

    async with httpx.AsyncClient() as client:                       # 共用一个 client：1 次握手，后续复用连接
        # async with	异步上下文管理器，退出时自动做异步清理
        # httpx.AsyncClient()	创建一个异步 HTTP 客户端实例
        # as client	把实例绑定到 client 这个名字，供下面的代码使用

        tasks = [fetch_with_limit(client,url) for url in URLS]      #创建任务列表   重要：这里只是创建了 10 个协程对象，还没有执行。
        results = await asyncio.gather(*tasks)                      #*tasks 是解包，把列表展开成 10 个独立参数：
        # gather 做两件事：
        # 同时启动所有协程
        # 等全部完成，按传入顺序返回结果列表

    total = time.time() - start
    ok_count = sum(1 for ok, _, _ in results if ok)   #ok是bool类型
    # for ok, _, _ in results	遍历三元组，_ 表示「不关心这一项」
    # if ok	只保留成功的
    # 1 for ...	每个成功项产出 1
    # sum(...)	加起来 = 成功总数

    for i,(ok,cost,err) in enumerate(results , 1):
        status = "成功" if ok else f"失败[{err}]"
        print(f"[{i} / {len(URLS)}] {status} 耗时{cost:.2f}s")

    print(f"并发总耗时：{total:.2f}s")
    print(f"成功 {ok_count} / {len(URLS)}")
    return total ,[ok for ok, _, _ in results]


def main():
    sync_total , sync_results = run_sync()
    async_total , async_results = asyncio.run(run_async(limit = 5))
    print("\n" + "=" *45)
    print("对比结果")
    print("=" * 45)
    print(f"串行耗时：{sync_total:.2f}s")
    print(f"并发耗时：{async_total:.2f}s")

    if async_total > 0:
        print(f"加速比：{sync_total / async_total:.1f}x")

    print(f"成功条数：串行{sum(sync_results)},并发{sum(async_results)}")

    if sum(sync_results) == sum(async_results):
        print("成功条数一致，结果可信")
    else:
        print("警告：成功条数不一致，可能是网络波动")


if __name__ == "__main__":
    main()
