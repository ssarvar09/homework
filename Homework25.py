class user:
    def __init__(self,username,fullname,email,age,p_number):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.age = age
        self.p_number = p_number
    def f1(self):
        return f"FoydLnuvch:{self.username},  ism_familiyasi:{self.fullname},  emaili:{self.email},  yoshi:{self.age},  telefon raqami:{self.p_number}"
s1 = user ("sarvar2009","Sarvar Quryazov", "sarvar2009@gmail.com",16,990679412)
print(s1.f1())