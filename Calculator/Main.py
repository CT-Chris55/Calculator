from Base import *
from Adv import *

def end():
    while True:
        print("System exiting!")
        break

def redo():
    redo = input("Do you want to make another calculation(Y/N):? ")
    if redo in ('Y','N'):
        if redo == 'Y':
            main.handler()
        else:
            end()

class main():
    def handler():
        print("Welcome to the calculator. Pick a version")
        print("1. Basic")
        print("2. Advanced")
        print("3. Exit")
        choice = input()
        
        if choice not in ('1','2','3'):
            print("Invalid option")
            choice = input()
        elif choice == '1':
            base.calculator()
        elif choice == '2':
            adv.vs()
        elif choice == '3':
            end()

class base():
    def calculator():
        print("1. Addition")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Return")
        
        choice = input("Enter your choice(1/2/3/4/5): ")
        
        if choice in ('1','2','3','4','5'):
            if choice == '5':
                end()
            else:
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                
                if choice == '1':
                    print(num1, "+", num2, "=", add(num1,num2))
                    redo()
                    
                elif choice == '2':
                    print(num1, "-", num2, "=", subtract(num1,num2))
                    redo()
                    
                elif choice == '3':
                    print(num1, "x", num2, "=", multiply(num1,num2))
                    redo()
                    
                elif choice == '4':
                    print(num1, "/", num2, "=", divide(num1,num2)) 
                    redo()
                         
        else:   
            print("Invalid option")
        
class adv():
    def vs():
        print('1. Standard')
        print('2. Trigonometric')
        
        choice = input("Enter your choice(1/2): ")
        
        if choice == '1':
            adv.standard()
        elif choice == '2':
            adv.trig()
        else:
            print('Invalid option')
            adv.vs()
    
    def standard():
        print("1. nth power")
        print("2. sqaure root")
        print("3. cube root")
        print("4. Log")
        print("5. In")
        print('6. Return')
        
        choice = input("Enter your choice(1/2/3/4/5): ")
        
        if choice in ('1','2','3','4','5','6'):
            if choice == '6':
                end()
            elif choice in ('1'):
                num1 = int(input("Enter your first number: "))
                num2 = int(input("Enter your second number: "))
                
                print(num1, "^", num2, "=", np(num1,num2))
                redo()
                    
                
            elif choice in ('2','3','4'): 
                num1 = int(input("Enter your first number: "))   
                
                if choice == '2':
                    print('sqaure root of', num1, "=", sr(num1))
                    redo()
                    
                elif choice == '3':
                    print('cube root of', num1, "=", cr(num1))
                    redo()
             
                elif choice == '4':
                    print("log", num1, "=", log(num1))
                    redo()
                    
                elif choice == '5':
                    print("In", num1, "=", In(num1)) 
                    redo()
                         
        else:   
            print("Invalid option")
        
    def trig():
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        print("4. Sec")
        print("5. Cosec")
        print("6. Cot")
        print('7. Return')
        

main.handler()