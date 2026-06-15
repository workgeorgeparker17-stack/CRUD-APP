# 📱 Python Phone Contacts Manager

A simple, beginner-friendly command-line contacts management application built with Python dictionaries.

---

## 📋 Description

Python Phone Contacts Manager is a console-based application that allows users to manage their phone contacts directly from the terminal. Built using Python's built-in `dict` data structure, this project demonstrates core Python concepts such as functions, loops, conditionals, and user input handling.

This project was created as part of a Python learning journey at **Najot Ta'lim**.

---

## ✨ Features

- ➕ **Add Contact** — Save a new contact with name and phone number
- ✏️ **Update Contact** — Edit an existing contact's phone number
- 🗑️ **Delete Contact** — Remove a contact from the list
- 🔍 **Search Contact** — Find a contact by name
- 📋 **View All Contacts** — Display all saved contacts
- 🚪 **Exit** — Quit the application

---

## 🚀 Getting Started

### Requirements

- Python 3.x

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/contacts-manager.git

# Navigate to the project folder
cd contacts-manager
```

### Run the App

```bash
python contacts.py
```

---

## 🖥️ How to Use

When you run the app, a menu will appear:

```
1. Kontakt qo'shish
2. Kontaktni yangilash
3. Kontaktni o'chirish
4. Kontakt qidirish
5. Barcha kontaktlarni ko'rish
6. Chiqish
```

Simply enter the number of your choice and follow the prompts.

---

## 💡 Example

```python
contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
```

**Adding a contact:**
```
Tanlang: 1
Ism: Jasur
Raqam kiriting: +998901234567
✅ Qo'shildi!
```

**Searching a contact:**
```
Tanlang: 4
Ism: Nodir
📞 Nodir: +998918602711
```

---

## 🧠 What I Learned

- Working with Python `dict` data structure
- Writing reusable functions
- Handling user input with `input()`
- Using `if/else` for validation logic
- Building a simple menu-driven CLI app

---

## 👤 Author

**George** — Python student at Najot Ta'lim, Karshi, Uzbekistan

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
