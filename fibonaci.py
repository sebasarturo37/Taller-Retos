def fibona(a):
    if a==0 or a==1:
        return 1
    return fibona(a-1)+fibona(a-2)

for i in range (0,20):
    print(fibona(i))
