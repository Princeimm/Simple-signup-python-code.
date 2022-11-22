import time
class reg:
    def sign_up(self):
       f_name=input("First name:")
       L_name=input("Last name :")
       u_name=input("set username:")
       phone=int(input("Phone:"))
       Mail=input("Mail:")
       pass_word=input(("Set password:"))
       c_password=input("Confirm password:")
       if (pass_word == c_password):
           time.sleep(3.0)
           print("Setting.......")
           print("Signup successful.")
       else:
           time.sleep(3.0)
           print("Setting.......")
           print("Password doesn't match !.")
access = reg()
access.sign_up()