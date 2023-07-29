import threading
import time
import random
# Condition下的生成者和消费者
gMoney = 1000
gCondtion = threading.Condition()
gNumber = 0
gTotals = 10
class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gNumber
        while True:
            money = random.randint(100,1000)
            gCondtion.acquire()
            if gNumber >= gTotals :
                gCondtion.release()
                break
            gMoney += money
            gNumber += 1
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gCondtion.notify_all()
            gCondtion.release()
            time.sleep(1)

class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        while True:
            money = random.randint(100,1000)
            gCondtion.acquire()
            while gMoney < money:
                if gNumber >= gTotals:
                    gCondtion.release()
                    return
                print('%s准备消费%d元钱，剩余%d元钱，不足'% (threading.current_thread(),money,gMoney))
                gCondtion.wait()
            gMoney -= money
            print('%s消费者消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gCondtion.release()
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

