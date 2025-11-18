#### 1
def kopaytma(a, b):
    """Istalgan son qabul qilib ularni ko'paytmasini qabul qilivchi funksiya"""
    return a * b
print(f"Ko'paytma➡️  {kopaytma(8, 8)}")


#### 2

def royxat_lar(ism,familiya,kusr=None,t_yili=None,t_kuni=None,t_raqami=None):
    return {
        "Ism:":ism,
        "Familiya:":familiya,
        "Kusr:":kusr,
        "Tug'ilgan yili:":t_yili,
        "Tugilgan kuni:":t_kuni,
        "Telefon raqami:":t_raqami,
    }
royxat =royxat_lar('Ali','Aliyev',3,2005,'1-dekabr',990679412)
for R in royxat:
    print(R,royxat[R])

