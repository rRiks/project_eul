def is_lcm(a,b):
    if a>b:
        num = a
        den = b
    else:
        num = b
        den = a
    reminder = num % den
    while reminder!=0:
        num = den
        den = reminder
        reminder = num % den
    gcd = den
    lcm_is = a*b/gcd
    return int(lcm_is)
if __name__ == "__main__":
    x = [i for i in range(10, 21)]
    a = x[0]
    b = x[1]
    lcm = is_lcm(a,b)
    for i in range(11,x[-1]):
        lcm = is_lcm(lcm,i)
    ans = lcm*2520
    print(lcm)
