def frg_jmp(x,y,d):
    distance=y-x
    jumps=distance//d #floor division which gives only the integer part of the quotient
    if distance%d!=0:
        jumps+=1
    return jumps

x=10
y=85
d=30
print(f'minimal number of jumps : {frg_jmp(x,y,d)}')