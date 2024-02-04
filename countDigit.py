num=int(input("enter the num:"))
def countdigit(num):
    count = 0
    while num != 0:
        num=int(num/10)
        count+=1
        print(num)
    return count

output=countdigit(num)
print(output)