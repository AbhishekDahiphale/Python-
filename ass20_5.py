
def DisplaySchedule(ch):
    ch = ch.upper()
    if(ch == 'A'):
        print("Exam at 7:00 AM ")
    elif(ch == 'B'):
        print("Exam at 8:30 AM ") 
    elif(ch == 'C'):
        print("Exam at 9:20 AM ")
    elif(ch == 'D'):
        print("Exam at 10:30 AM ")
    else:
        print("Enter the Wrong division ")               

def main():
    value = input("Enter the chracter : ")[0]
    
    DisplaySchedule(value)    

if __name__ == "__main__":
    main()