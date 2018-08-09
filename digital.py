Number1 = int(input("Please Enter any Number: "))
Count = 0
while(Number1 > 0):
    Number1 = Number1 // 10
    Count = Count + 1
 
print("\n Number of Digits in a Given Number1 = %d" %Count)
