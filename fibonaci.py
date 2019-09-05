#developed by: Sebastián D. Arturo - Juan Sebastián Erazo
#ingeniería de sistemas 10 A
#Electiva profesional III - Frameworks

def fibona(a):
    if a==0 or a==1:
        return 1
    return fibona(a-1)+fibona(a-2)

for i in range (0,20):
    print(fibona(i))
