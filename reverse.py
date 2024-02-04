num=int(input("enter the num:"))
def reverseDigit(num):
    reverse= 0
    while num != 0:
        reverse=(reverse*10) + (num%10)
        num = int(num / 10)

    return reverse
print(reverseDigit(num))