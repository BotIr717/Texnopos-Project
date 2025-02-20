from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

all_menu = ReplyKeyboardMarkup(resize_keyboard=True)
all_menu.add(KeyboardButton('Band qilish👑'))
all_menu.add(KeyboardButton('Bo\'sh joylarni tekshirish🎯'))
all_menu.add(KeyboardButton('Texnik yordam so\'rash⚔️'))
all_menu.add(KeyboardButton('Gazaklar🫕'))
all_menu.add(KeyboardButton('Komputer statistikasini bilish🖥'))

admin_menu = ReplyKeyboardMarkup(resize_keyboard=True)
admin_menu.add(KeyboardButton('Rezervatsiyalar ro\'yxati'))
admin_menu.add(KeyboardButton('Rezervatsiyani yopish'))  
admin_menu.add(KeyboardButton('Admin panel'))
admin_menu.add(KeyboardButton('◀️Back to User menu'))

Gazak_menu = ReplyKeyboardMarkup(resize_keyboard=True)
Gazak_menu.add(KeyboardButton('Sprite'))
Gazak_menu.add(KeyboardButton('Mountain dew'))
Gazak_menu.add(KeyboardButton('lays'))
Gazak_menu.add(KeyboardButton('◀️Orqaga'))

Sonlar_menu = ReplyKeyboardMarkup(resize_keyboard=True)
Sonlar_menu.add(KeyboardButton('1️⃣'))
Sonlar_menu.add(KeyboardButton('2️⃣'))
Sonlar_menu.add(KeyboardButton('3️⃣'))
Sonlar_menu.add(KeyboardButton('4️⃣'))
Sonlar_menu.add(KeyboardButton('5️⃣'))
Sonlar_menu.add(KeyboardButton('6️⃣'))
Sonlar_menu.add(KeyboardButton('7️⃣'))
Sonlar_menu.add(KeyboardButton('8️⃣'))
Sonlar_menu.add(KeyboardButton('9️⃣'))
Sonlar_menu.add(KeyboardButton('🔟'))

User_menu = ReplyKeyboardMarkup(resize_keyboard=True)
User_menu.add(KeyboardButton('◀️Back to User menu'))
