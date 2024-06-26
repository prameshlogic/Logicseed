# def cal():
    
#     while True:
#         num1=int(input("Enter a number: "))
#         num2=int(input("Enter second number: "))
        
#         print('''Chosse operation:
#             * = multiplication
#             + = sum
#             - = subtraction
#             / = Division
#             exit = exit from the program''')
#         choice = input("Enter your choice: ")
        
#         if choice=='+':
#             ad = num1+num2
#             print(ad)
            
#         elif choice=='-':
#             sub = num1-num2
#             print(sub)
            
#         elif choice=='*':
#             mu = num1*num2
#             print(mu)
        
#         elif choice=='/':
#             d = num1/num2
#             print(d)
#         elif choice=="exit":
#             break  
#         else:
#             print("Unknown choice")
            
# cal()



while True:
    a=(input("Enter your operation: "))
    variable ={a}
    if a=='e':
        break
    elif "=" in a:
 
        b = a
        v=['a','b','c','d','e','f','g','h']
        c=b[::-1]
        c=b.replace("=",v,"")
        print(c)
        
    else:
        b=eval(a)
        print(b)
        continue  
    
