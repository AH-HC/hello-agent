# 核心目标:	理解一句话：程序在等待网络返回时，可以先去干别的活
# 主题: 协程、await、asyncio.gather

# 1.串行
# time.sleep(sec)     t = time.time()    time.time() - t   
import time
import asyncio

def work(name,sec):
    print(f"{name} 开始")
    time.sleep(sec)      #模拟耗时操作
    print(f"{name} 结束")
    return name

def main_sync():
    t = time.time()     #记录起点
    work("A",2)
    work("B",2)
    work("C",2)
    print(f"串行总耗时：{time.time() - t:.2f}s")




# 2.并行   
#  await asyncio.sleep(sec)      await asyncio.gather()
async def work_async(name,sec):
    print(f"{name} 开始")
    await asyncio.sleep(sec)     #await = 「这里要等一个结果，等的时候把控制权让出去，结果好了再回来继续。」
    print(f"{name} 结束")
    return name

async def main_async():
    t = time.time()
    results = await asyncio.gather(     #把多个协程同时启动，等全部完成后，按传入顺序返回所有结果。
        work_async("A", 2),
        work_async("B", 2),
        work_async("C", 2),
    )
    print(f"并发总耗时：{time.time() - t:.2f}s")
    print(f"返回值：{results}")

# 3.破坏并发
async def work_bad(name,sec):
    print(f"{name} 开始")
    time.sleep(sec)             #换成同步的 sleep
    print(f"{name} 结束")
    return name

async def main_bad():
    t = time.time()
    await asyncio.gather(
        work_bad("A", 2),
        work_bad("B", 2),
        work_bad("C", 2),
    )
    print(f"总耗时：{time.time() - t:.2f}s")

# 3 中的代码为什么会失效并发  
# await asyncio.sleep(2)	挂起当前任务，把控制权交回事件循环，循环去执行其他任务
# time.sleep(2)	阻塞整个线程，事件循环也被卡住，谁都没法运行


# 4.忘记await会发生什么
async def main_forgot():
    result = work_async("A", 2)
    print("result 的类型：", type(result))
    print("result 的值：", result)
# 返回值是 coroutine 对象，不是 "A"
# 有一条警告：never awaited
# 这就是「调用协程函数不会执行」的证据。​ 你只是创建了一个协程对象，没有把它交给事件循环。

# 问题：什么是否不能用异步
# 异步不是万能的。它只对「等待 IO」有效。






if __name__ == "__main__":
    print("=" * 45)
    print("实验 1：串行（预期 6 秒）")
    print("=" * 45)
    main_sync()

    print()
    print("=" * 45)
    print("实验 2：并发（预期 2 秒）")
    print("=" * 45)
    asyncio.run(main_async())

    print()
    print("=" * 45)
    print("实验 3：time.sleep 破坏并发（预期退回 6 秒）")
    print("=" * 45)
    asyncio.run(main_bad())

    print()
    print("=" * 45)
    print("实验 4：忘记 await（预期 coroutine 对象）")
    print("=" * 45)
    asyncio.run(main_forgot())
