import asyncio
import time

async def ok_task(n):
    await asyncio.sleep(0.5)
    print(f" 任务{n} 完成")
    return n

async def bad_task():
    await asyncio.sleep(0.3)
    # raise ：主动抛出异常
    # raise 是「扔」，except 是「接」。​ 没有 except 接，异常会一路往上，最后让程序崩溃
    raise ValueError("我故意失败")

# 1.gather 默认行为
async def exp1():
    print("=== 实验一：gather 默认行为===")
    start = time.time()
    try:
        results = await asyncio.gather(
            ok_task(1),
            bad_task(),
            ok_task(2)
        )
        print("结果：",results)

    except ValueError as e:
        print(f"整批被中断：{e}")

    print(f"耗时：{time.time() - start:.2f}s")

# 实验 2：return_exceptions
# return_exceptions=True：gather 的参数
async def exp2():
    print("\n=== 实验 2：return_exceptions=True ===")
    start = time.time()
    results = await asyncio.gather(
        ok_task(1),
        bad_task(),
        ok_task(2),
        return_exceptions=True
    )
    print(f"耗时：{time.time() - start:.2f}s")
    print("结果列表：")
    for item in results:
        # isinstance：判断对象类型
        # 内置函数，作用是「判断这个对象是不是某种类型」
        # 关键特性：支持继承
        if isinstance(item, Exception):
            print(f"  失败：{type(item).__name__}: {item}")
        else:
            print(f"  成功：{item}")


# 实验 3：wait_for 超时
async def slow_task():
    print("慢任务开始")
    await asyncio.sleep(3)
    print("慢任务完成")
    return "完成了"

async def exp3():
    print("\n=== 实验 3：wait_for 超时控制 ===")
    start = time.time()
    try:
        results = await asyncio.wait_for(slow_task(),timeout=1)
        print("结果：", results)
    except asyncio.TimeoutError:
        print("超时了，任务被取消")
    print(f"耗时：{time.time() - start:.2f}s")

# 实验 4：create_task 的时机
# 这就是并发的本质：不是让每个任务变快，是让它们的等待时间重叠。
async def exp4():
    print("\n=== 实验 4：create_task vs 直接 await ===")
    start = time.time()

    print("创建两个任务（还没await）")
    # 包装成 Task，注册到事件循环
    # create_task 是「登记」，await 是「开始」
    t1 = asyncio.create_task(ok_task(1))
    t2 = asyncio.create_task(ok_task(2))
    print(f"t1 是否完成：{t1.done()}")

    r1 = await t1
    r2 = await t2
    print(f"结果：{r1}, {r2}")
    print(f"耗时：{time.time() - start:.2f}s")

async def exp4_serial():
    print("\n=== 对照：直接 await（串行）===")
    start = time.time()
    r1 = await ok_task(1)
    r2 = await ok_task(2)
    print(f"结果：{r1}, {r2}")
    print(f"耗时：{time.time() - start:.2f}s")

async def main():
    # await exp1()
    # await exp2()
    # await exp3()
    await exp4()
    await exp4_serial()

if __name__ == "__main__":
    asyncio.run(main())


# create_task 管「什么时候启动」，wait_for 管「最多等多久」，return_exceptions 管「失败了怎么办」，Semaphore 管「同时跑几个」。
