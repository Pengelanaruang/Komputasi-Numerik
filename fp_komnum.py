from decimal import Decimal, ROUND_HALF_UP

def pembulatan(x): #fungsi pembulatan
    return Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def f(x): #fungsi soal
    return x**3 + 6*x**2 - 19*x - 84

def bagi_dua(xl, xu, xt): #fungsi metode bagi dua
    iterasi = 1
    print("Iterasi\t\tXL\t\tXU\t\tXR\t\tf(XR)\t\tEt(%)")
    
    while True:
        xr = (xl + xu) / 2

        xr_pembulatan = pembulatan(xr)
        fxr_pembulatan = pembulatan(f(xr_pembulatan))

        et = abs((xt - xr_pembulatan) / xt) * 100

        et_pembulatan = pembulatan(et)

        print(f"{iterasi}\t\t{xl:.2f}\t\t{xu:.2f}\t\t{xr_pembulatan}\t\t{fxr_pembulatan}\t\t{et_pembulatan}")

        if et < 1 and et >= 0:
            break

        if f(xl) * f(xr_pembulatan) < 0:
            xu = xr_pembulatan
        else:
            xl = xr_pembulatan

        iterasi += 1

    print("\nAkar X =", f"{xr_pembulatan}")

#input
xl = -4
xu = 3
xt = -3

bagi_dua(xl, xu, xt)
