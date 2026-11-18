import asyncio
import time

LIMIT = 2          # 同时最多 2 个任务
TASKS = 6          # 总共 6 个任务

async def one_request(tid,attempt):
 
 """模拟一次请求：0.2 秒，前两次失败"""
 print(f"  任务{tid} 第{attempt}次请求")
 await asyncio.sleep(0.2)
 if(attempt < 3):
  raise asyncio.TimeoutError()


async def worker_inside(sem,tid):
 """错误：sem 在循环内部"""
 for attempt in range(1,4):
  async with sem:                  
   try:
    await one_request(tid,attempt)
    print(f"  任务{tid} 成功")
    return
   except asyncio.TimeoutError:
    pass
   await asyncio.sleep(0.3)             # 退避：此时许可已释放

async def worker_outside(sem, tid):
    """正确：sem 包住整个循环"""
    async with sem:                              # ① 抢许可（只抢一次）
        for attempt in range(1, 4):
            try:
                await one_request(tid, attempt)
                print(f"  任务{tid} 成功")
                return
            except asyncio.TimeoutError:
                await asyncio.sleep(0.3)    # 退避：仍持有许可

async def run(mode):
    print(f"\n{'=' * 40}")
    print(f"模式：{mode}")
    print(f"{'=' * 40}")
    start = time.time()

    sem = asyncio.Semaphore(LIMIT)
    worker = worker_inside if mode == 'inside' else worker_outside

    await asyncio.gather(*[worker(sem,i) for i in range(1,TASKS + 1)])
    print(f"总耗时：{time.time() - start:.2f}s")


async def main():
    await run("inside")
    await run("outside")

if __name__ == "__main__":
   asyncio.run(main())

