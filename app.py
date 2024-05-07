from model import addition,sub
from multiply import multiplication
from division import divide
def main():
    print("WELCOME")

    user_input = input("Select function  ")

    a = int(input("Enter a  "))
    b = int(input("Enter b  "))

    

    if user_input == "1":
        result = addition(a,b)
    elif user_input == "2":
        result = sub(a,b)
    elif user_input == "3":
        result = multiplication(a,b)    
    elif user_input == "4":
        result = divide(a,b)


    print("Result",   result)    




if __name__== "__main__":
    main()
