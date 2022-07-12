from concurrent.futures import thread
import threading
import multiprocessing

def even(lock):
               lock.acquire()
               count=0
               i=1
               print("even:  ",end=" ")
               while(count<10):
                              if(i%2==0):
                                             print(i,end="     ")
                                             i=i+1
                                             count=count+1
                              else:
                                             i=i+1
               print("\n")
               lock.release()
def odd(lock):
               lock.acquire()
               count=0
               i=1
               print("odd:  ",end=" ")
               while(count<10):
                              if(i%2!=0):
                                             print(i,end="     ")
                                             i=i+1
                                             count=count+1
                              else:
                                             i=i+1
               print("\n")
               lock.release()

def main():
               lock=multiprocessing.Lock()
               thread1=threading.Thread(target=even,args=(lock,),name="Even")
               thread2=threading.Thread(target=odd,args=(lock,),name="Odd")
               thread1.start()
               thread2.start()
               thread1.join()
               thread2.join()



if __name__ == '__main__':
                   main()
    