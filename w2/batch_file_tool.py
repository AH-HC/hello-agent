import csv
from pathlib import Path

def inspect_csv(path):
    """统计一个 CSV 文件，返回 (数据行数, 列数, 表头)"""
    # TODO 1：用 utf-8-sig 和 newline="" 打开文件
    #         用 csv.reader 读成 list
    #         返回 (总行数-1, 第一行的长度, 第一行)
    #         注意：空文件要特殊处理，返回 (0, 0, [])
    with open(path,"r",encoding="utf-8-sig",newline="") as f:
            rows = list(csv.reader(f))
    if not rows:
      return 0, 0, []

    return len(rows)-1, len(rows[0]), rows[0]

def main(folder):
    folder = Path(folder)   #相对路径
    if not folder.exists():
        print(f"目录不存在:{folder}")
        return

    good,bad = [],[]   #准备两个收集容器,列表

    for p in sorted(folder.glob("*.csv")):      #找出目录下所有 .csv 结尾的文件，返回一个生成器，sorted(...)->把结果排序
        try:
            nrow,ncol,header = inspect_csv(p)
            good.append((p.name,nrow,ncol,header))
        except Exception as e:
            bad.append((p.name, type(e).__name__, str(e)))


    # TODO 2：打印汇总表
    #   格式建议：
    #   文件名         行数   列数   表头
    #   books.csv       3      3     书名,作者,年份
    #   最后打印：成功 N 个，失败 M 个

    print(f"{'文件名':<15} {'行数':<6} {'列数':<6} {'表头'}")
    for name, nrow, ncol, header in good:
        print(f"{name:<15} {nrow:<6} {ncol:<6} {','.join(header)}")
    print(f"成功 {len(good)} 个，失败 {len(bad)} 个")
    


    # TODO 3：如果有失败文件，写入 errors.log
    #   格式建议：文件名 | 错误类型 | 错误信息
    #   用 encoding="utf-8" 写入
    if bad:
        with open("errors.log","w",encoding="utf-8") as f:
            for name, err_type, err_msg in bad:
                f.write(f"{name} | {err_type} | {err_msg}\n")


if __name__ == "__main__":
    main("data")


    
