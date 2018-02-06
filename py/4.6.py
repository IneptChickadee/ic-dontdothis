def computepay(h,r):
    hrs = float(h)
    rate = float(r)
    if hrs >= 40:
        base = 40 * rate
        oth = hrs - 40
        ot = oth * rate * 1.5
        pay = base + ot
    else:
        pay = hrs * rate
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs,rate)
print(p)
