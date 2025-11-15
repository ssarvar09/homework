# def foydalanuvch(ism,familiya,yili,yawaw_joyi,email,raqami):
#     return {
#         'ism':ism,
#         'familiya':familiya,
#         'yili':yili,
#         'yawaw_joyi':yawaw_joyi,
#         'email':email,
#         'raqami':raqami
#     }
#
# h = foydalanuvch('sarvar','quryazov',2009,'Urganch','quryazovsarvarbek17@gmail.com',990679412)
# for k,v in h.items():
#     print(k,v)
#
#
# ### 2
#
# s=[]
# while True:
#     print('maluotlarni kiriting')
#     ism =input('ism kiriting!:')
#     familiya =input('familiya kiriting😊:')
#     yili =input("tug'ilgan yil kiriting:")
#     yawaw_joyi =input("yashash joyingizni kiriting:")
#     email =input("email kiriting:")
#     raqami =input('telefon raqami:')
#     s.append(foydalanuvch(ism,familiya,yili,yawaw_joyi,email,raqami))
#     print(s)
#
#     k = input("yana malumot qoshasizmi?(ha\yoq):")
#     if k.lower() != 'ha':
#      break
#
# print("Mana ro'yhat😊")
# for h in s:
#     print(h)


### 3
def katta_son(a,b,c):
    return max(a,b,c)
k = katta_son(2,3,4)
print(k)


### 4
def r (r):
    import math
    return {
        "radius":r,
        "diameter": 2 * r,
        "perimeter": 2 * math.pi * r,
        "yuza": math.pi * r**2
    }
radius= r(40)
for k,v in radius.items():
    print(k,v)


### 5

