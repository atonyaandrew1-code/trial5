from datetime import datetime

class BankAccount:
    def __init__(self,owner,number,balance):
        self.owner = owner
        self.number =number
        self.__balance =balance

    def deposit(self,amount):
        self.__balance +=amount
        print(f"Deposited:{amount}")

    def get_balance(self):
        return self.__balance

    def print_receipt(self):
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        print("-"*20)
        print("Bank reciept")
        print(f" Date:{dt_string}")
        print("-"*20)
        print(f"Account Number:{self.number}")
        print(f"Account Owner: {self.owner}")
        print(f"Total Balance: {self.__balance}")
        print("_"*20)

    def save_data(self):
        with open("Bank deposit record.txt","a")as file:
            file.write(f"Name:{self.owner}|Acc number:{self.number}|Current Balance:{self.__balance}| Date:{datetime.now()} \n")
            print("Successfully saved")
acc = BankAccount(input("enter your name: "),input("account no: "),int(input("enter initial balance: ")))
acc.deposit(int(input("How much do you want to deposit? ")))
acc.print_receipt()
acc.save_data()

class Student:
    def __init__(self,name,regNumber,year):
        self.name =name
        self.regNumber = regNumber
        self.year = year
        self.marks =[]
    def input_marks(self):
        print(f"Inputing marks for{self.name}:")
        for i in range(1,6):
            score= float(input(f"unit{i}mark:"))
            self.marks.append(score)
   
    def get_average(self):
        if len(self.marks) ==0:return 0
        return sum(self.marks)/len(self.marks)

    def get_grade(self):
        average = self.get_average()
        if not self.marks:
            return "No marks entered"
        if average >=70:return "A"
        if average >=60: return "B"
        if average >= 50: return "C"
        if average >=40: return "D"
        else: return "E"
    def save_data(self):
        with open("student record.txt","a")as file:
            file.write(f"name:{self.name}|marks:{self.marks}|Average:{self.get_average():.2f}|Grade:{self.get_grade()}\n")
            print("Successfully saved to student_record.txt")


student = Student(input("Enter your name: "),input("regNUmber: "),input("year of study"))
student.input_marks()
print(f"Student: {student.name}")
print(f"Average Score: {student.get_average():2f}")
print(f"Final grade: {student.get_grade()}")
student.save_data()



   