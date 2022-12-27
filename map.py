#syntax
# map(operation we have to perform, on whom we have to perform)
l=[1,2,3,4]
def addition(x):
    return x+5

result=map(addition,l)
print(list(result))


l=list(map(int,input().split(","))) #--> very imp
print(l)
