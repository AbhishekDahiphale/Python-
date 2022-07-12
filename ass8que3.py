import threading
import multiprocessing

def Even(ls,lock):
               lock.acquire()
               sum=0
               for i in ls:
                              if(i%2==0):
                                             sum=sum+i
               print("addition of even :   ",sum)

               lock.release()
def Odd(ls,lock):
               lock.acquire()
               sum=0
               for i in ls:
                              if(i%2!=0):
                                             sum=sum+i
               print("addition of odd :   ",sum)

               lock.release()
def main():
               ls=[]
               lock=multiprocessing.Lock()
               print("enter the size of list")
               no=int(input())
               for i in range(no):
                              ls.append(int(input()))
               evenlist=threading.Thread(target=Even,args=(ls,lock,))
               oddlist=threading.Thread(target=Odd,args=(ls,lock,))
               evenlist.start()
               oddlist.start()
               evenlist.join()
               oddlist.join()



if __name__ == '__main__':
                   main()
    