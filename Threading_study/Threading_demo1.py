import threading
import time

def coding():
    for x in range(4):
        print('正在写入代码……%s'%threading.current_thread())
        time.sleep(1)

def drawing():
    for x in range(4):
        print("正在画画……%s"%threading.current_thread())
        time.sleep(1)

def traditionway():
    coding()
    drawing()

def mythread():
    t1 =threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)
    t1.start()
    t2.start()

if __name__ == '__main__':
    # traditionway() #传统方式
    mythread()  # 多线程方式
    # print(threading.enumerate()) #查看当前进程中的线程数