import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() # 紀錄開始時間
        result = func(*args, **kwargs) # 執行接收函式
        end_time = time.time() # 紀錄結束時間
        # 時間相減就是執行時間
        print(f"{func.__name__} executed {end_time - start_time:.4f} seconds.") 
        return result
    return wrapper

@timer
def function1():
    time.sleep(2)  # 停頓兩秒
    print("Function1 Completed.")
@timer
def function2():
    time.sleep(1)
    print("Function2 Completed")

# 呼叫函數
function1()
function2()