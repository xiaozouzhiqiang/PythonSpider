import threading
# 多进程工作时会遇到同一时间两个线程同时修改一个全局变量的情况，这样会导致数据出现问题
# 所以要添加线程锁机制
VALUE = 0
gLock = threading.Lock()

def add_value():
    global VALUE
    gLock.acquire()
    for x in range(1000000):
        VALUE += 1
    gLock.release()
    print("value%d"%VALUE)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == '__main__':
    main()