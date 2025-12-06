### 1
with open('pi.txt',"r") as fayl:
    pi = fayl.read()
print(pi)

### 2
with open ('pi_million_digits.txt', "r") as s:
    pi_million = s.read()
print(pi_million)

### 3









### 4









# 5
while True:
    malumot = input("Ma'lumot kiriting (toxtatiw uchun 'toxta' deb yozing): ")

    if malumot.lower() == "toxta":
        print("dastur iwlawdan to'xtadi❌")
        break

    with open("files.txt", "a") as file:
        file.write(malumot + "\n")

    print('Ma\'lumot faylga yozildi!')
