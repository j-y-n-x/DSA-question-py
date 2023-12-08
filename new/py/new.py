#to write-a-program-that-takes-a-character-as-input- and-prints-1-0-or-1-according-to-the-following-rules

a=input("enter a num ")
if a.islower():
    print(0)
elif a.isupper():
    print(1)
else:
    print(-1)    