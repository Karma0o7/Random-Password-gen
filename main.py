# Modules
import random

def main():
    passlen = int(input("Enter the length of password: "))
    s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s,passlen ))
    print (p)

if __name__ == "__main__":
    main()
