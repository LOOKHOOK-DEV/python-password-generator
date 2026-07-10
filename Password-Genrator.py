import random

Characters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz1234567890!@#$%^&*()?_.,<>/'
Char_List=list(Characters)
random.shuffle(Char_List)
Password="".join(Char_List)
print(f"Your password is:{Password}")