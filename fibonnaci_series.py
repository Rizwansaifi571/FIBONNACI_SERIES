"""
f(0)=0
f(1)=1
f(2)=f(1)+f(0)
f(n)=f(n-1)+f(n-2)
"""

def fibonnaci_sequence(n):
    if n==0 or n==1:
        return 1
    else:
        return fibonnaci_sequence(n-2)+fibonnaci_sequence(n-1)
n=int(input("Enter The Number : "))
for m in range(0,n):
    print(fibonnaci_sequence(m))