from curses.ascii import isdigit, islower, isupper
from itertools import count
import os
from re import S
import string
from this import s
import threading
import multiprocessing

def Capital(s,lock):
               lock.acquire()
               count=0
               print("id: {} name: {}".format(os.getpid(),threading.current_thread().name))
               for i in s:
                              if isupper(i):
                                             count=count+1
               print("count of capital :   ",count)

               lock.release()
def Small(s,lock):
               lock.acquire()
               count=0
               print("id: {} name: {}".format(os.getpid(),threading.current_thread().name))

               for i in s:
                              if islower(i):
                                             count=count+1
               print("count of small :   ",count)

               lock.release()

def Digit(s,lock):
               lock.acquire()
               count=0
               print("id: {} name: {}".format(os.getpid(),threading.current_thread().name))

               for i in s:
                              if isdigit(i):
                                             count=count+1
               print("count of digit :   ",count)

               lock.release()
def main():
               ls=[]
               lock=multiprocessing.Lock()
               print("enter the string")
               s=str(input())
               small=threading.Thread(target=Small,args=(s,lock,),name="small")
               capital=threading.Thread(target=Capital,args=(s,lock,),name="capital")
               digit=threading.Thread(target=Digit,args=(s,lock,),name="digit")
               small.start()
               capital.start()
               digit.start()

               small.join()
               capital.join()
               digit.join()


if __name__ == '__main__':
                   main()
    