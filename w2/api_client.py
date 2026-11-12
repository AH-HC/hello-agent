import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()  # 读取 .env 文件中的环境变量

def fetch(url,timeout = 5,retries = 3):
    """请求一个 URL，返回 (ok, data, err)
    ok :bool, 是否成功
    data:dict/list,解析后的数据；失败为None
    err:str, 错误信息；成功为 None
    """
    last_err = None

    for i in range(retries):   #生成一个序列：0, 1, 2（不含 3）
        try:
            r = requests.get(url,timeout = timeout)
            r.raise_for_status()  # 如果状态码不是 200，会抛出异常
            return True, r.json(), None
        
        except requests.exceptions.Timeout:
            last_err = "请求超时"
            print(f"第{i+1}次请求超时，等待 {2 ** i}秒后重试...")

        except requests.exceptions.ConnectionError:
            last_err = "网络连接错误"
            print(f"第{i+1}次请求连接错误，等待 {2 ** i}秒后重试...")

        except requests.exceptions.HTTPError as e:
            code = e.response.status_code
            # 4xx 错误，通常是客户端问题，不需要重试,直接返回
            if code < 500:
                return False,None,f"客户端错误 {code}"

            # 5xx 错误，通常是服务端问题，可以重试
            last_err = f"服务端错误 {code}"
            print(f"第{i+1}次请求服务端错误{code}，等待 {2 ** i}秒后重试...")

        except ValueError:
            return False,None,"返回的不是 JSON 数据"

        time.sleep(2 ** i)  # 指数退避

    return False,None,f"{last_err}，重试 {retries} 次后仍然失败"

def main():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        print("检测到 GITHUB_TOKEN")
    else:
        print("未配置 GITHUB_TOKEN（公开接口不需要）")

    cases = [
        ("正常请求", "https://api.github.com/users/AH-HC"),
        ("404 路径错误", "https://api.github.com/users/no-such-user-xyz-999"),
        ("500 服务端错误", "https://httpbin.org/status/500"),
    ]

    for label,url in cases:
        print(f"=== {label} ===")
        ok, data, err = fetch(url)

        if ok:
            print(f"  成功，仓库数：{data.get('public_repos', 'N/A')}")
        else:
            print(f"  失败：{err}")

        print()

if __name__ == "__main__":
    main()
        

