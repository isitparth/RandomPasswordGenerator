import random
pas = int(input("Enter length of the password"))
s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFCHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p="".join(random.sample(s,pas))
print(p)
