contacts = {}
def add_contact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("Qo'shildi!")
    else:
        print("Bu kontakt allaqachon bor")
    
def update_contact(name,new_phone):
        if name in contacts:
            contacts[name] = new_phone
            print("Yangilandi!")
        else:
            print("Kontakt topilmadi!")
            
def delete_contact(name):
    if name in contacts:
        contacts.pop(name)
        print("O'chirildi!")
    else:
        print("Bu kontakt topilmadi")
            
def search_contact(name):
    if name in contacts:
        print(f"Topildi - {name}:{contacts[name]}")
    else:
        print("Topilmadi")
    
def see_contacts():
    if contacts:
        for name,phone in contacts.items():
            print(name,phone)
    else:
        print("Kontaktlar ro'yhati bo'sh!")


while True:
    print("""
          1. Kontakt qo'shish
          2. Kontaktni yangilash  
          3. Kontaktni o'chirish
          4. Kontakt qidirish
          5. Kontaktni ko'rish
          0. Chiqish
          """)
    
    user = int(input("Tanlang: "))
   
    if user == 1:
        ism = input("Ism: ")
        raqam = input("Raqam kiriting: ")
        add_contact(ism,raqam)
    elif user == 2:
        ism = input("Ism: ")
        raqam = input("Raqam kiriting: ")
        update_contact(ism,raqam)
    elif user == 3:
        ism = input("Ism: ")  
        delete_contact(ism)
    elif user == 4:
        ism = input("Ism: ")
        search_contact(ism)
    elif user == 5:
        see_contacts()
    elif user == 6:
        break
