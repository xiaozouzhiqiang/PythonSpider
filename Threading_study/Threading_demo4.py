import threading
import time
import random
# lock的生产者和消费者
gMoney = 1000
gLock = threading.Lock()
gNumber = 0
gTotals = 10
class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gNumber
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gNumber >= gTotals :
                gLock.release()
                break
            gMoney += money
            gNumber += 1
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gLock.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费者消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
                gLock.release()
            else:
                #
                if gNumber >= gTotals:
                    gLock.release()
                    break
                print('%s消费者准备消费%d元钱，剩余%d元钱,不足'%(threading.current_thread(),money,gMoney))
                gLock.release()
                time.sleep(1)

def main():

    for x in range(3):
        t = Consumer(name='消费者线程%d'%x)
        t.start()
    for x in range(5):
        t = Producer(name='生产者线程%d'%x)
        t.start()

if __name__ == '__main__':
    main()



