# 学习 try except finally
def divide(a,b):
    try:
        print("1.try 开始")
        result = a / b
        print(f"2.计算成功{result}")
        return result
    except ZeroDivisionError:
        print("2.接入错误，除数不能为0")
        return None
    finally:
        print("3.无论如何都会执行")

print('正常情况')
divide(10,2)

print('\n异常情况')
divide(10,0)