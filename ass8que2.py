import threading
import multiprocessing

def Even_Factor(num,lock):
               lock.acquire()
               addition=0
               for i in range(1,(int(num/2)+1),1):
                              if num%i==0:
                                             if(i%2==0):
                                                            addition=addition+i    
                                                            print(i) 
               print("addition of even factor:",addition)          
               lock.release()
def Odd_factor(num,lock):
               lock.acquire()
               addition=0
               for i in range(1,(int(num/2)+1),1):
                              if num%i==0:
                                             if(i%2!=0):
                                                            addition=addition+i
                                                            print(i)
               print("addition of odd factor:",addition)          

               lock.release()

def main():
               lock=multiprocessing.Lock()
               print("enter the number")
               num=int(input())
               thread1=threading.Thread(target=Even_Factor,args=(num,lock,),name="Even_factor")
               thread2=threading.Thread(target=Odd_factor,args=(num,lock,),name="Odd_factor")
               thread1.start()
               thread2.start()
               thread1.join()
               thread2.join()
               print("exit from main")



if __name__ == '__main__':
                   main()
    