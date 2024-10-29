import string
import re

###########################################################        
def login():
    print('login')

###########################################################        
def register_login_validation():
    # a set of letters of the English upper and lower and numbers
    pattern = r"^[a-zA-Z0-9]+$"
    # numbers for sumbol
    pattern_num = r"\d+"
    while True:
        login = input("Введите логин:")
        # cheking for number of charactersr
        if len(login) <= 3: 
            print("логин должен состоять не менее чем из 4 символов") 
        # cheking for matching of characters
        elif bool(re.match(pattern, login)) == False:
            print("логин должеть содержать символы английского алфавита")
        # cheking for numbers alone
        elif bool(re.match(pattern_num, login)):
            print("логин не может состоять только из цифр")
        else:
            return login
            
###########################################################        
def register_password_validation():
    sumbol = r"[a-zA-Z\d!@$^&*(),.?%]"
    while True:
        # cheking for number of characters
        password = input("Введите пароль:")
        if len(password) <= 5: 
            print("Пароль должен состоять не менее чем из 6 символов")      
        elif bool(re.match(sumbol, password)) == False:
            print("Пароль не может содержать данные символы")
        else:
            pass1 = password  
            pass2 = input("Повторите пароль:")
            if pass1 == pass2:
                print("вы успешно зарегистрированны!")
                return pass2
            else:
                print("Пароли не совпадают")  

###########################################################        
def register():
    while True:
        print('Придумайте логин и пароль')
        login = register_login_validation()  
        password = register_password_validation()
        break

###########################################################        
# Start user choice login and register
def start(): 
    while True:
        commands = {"l": login, "r": register,}
        command = input("Вы можете 'войти' = l или 'зарегистрироваться'= r\n")
        commands[command]()
###########################################################        
start()