import threading
import time
from queue import Queue

# 创建队列
q = Queue(4)

def queuefor():
    for x in range(4):
        # 将0.1.2.3 写入队列中
        q.put(x)

    for x in range(4):
        # 打印当前队列
        print(q.get(x))

def set_value(que,index):
    while True:
        que.put(index)
        index += 1
        time.sleep(1)

def get_value(que):
    while True:
        print(que.get())

def main():
    # 入队列 出队列
    # queuefor()
    que = Queue(4)
    index = 0
    t1 = threading.Thread(target=set_value,args=[que,index])
    t2 = threading.Thread(target=get_value,args=[que])
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()

