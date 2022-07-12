import threading
import multiprocessing

def forward(lock):
               lock.acquire()
               for i in range(1,51,1):
                              print(i,end="     ")
               lock.release()
               print("\n")
def reverse(lock):
               lock.acquire()
               print("\n")
               for i in range(50,0,-1):
                              print(i,end="     ")
               lock.release()

def main():
               lock=multiprocessing.Lock()
               thread1=threading.Thread(target=forward,args=(lock,),name="thread1")
               thread2=threading.Thread(target=reverse,args=(lock,),name="thread2")
               thread1.start()
               thread2.start()

               thread1.join()
               thread2.join()


if __name__ == '__main__':
                   main()
    