name=str(input("enter the string:"))
def func(name):
    ans=""
    list=["a","e","i","o","u"]
    for x in name:
        if x in list:
            pass
        else:
            ans+=x
    return ans


print(func(name))