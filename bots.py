from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from datas import init_db, add_user, add_reservation, get_reservations, get_computer_reservations, finish_reservation_by_user_id
from keyboards import all_menu, admin_menu, Gazak_menu ,Sonlar_menu
from config import API_KEY
from config import admin_id

#----------------------------------------------------------------
storage = MemoryStorage()
# proxy = "http://proxy.server:3128/"
bot = Bot(API_KEY,) #proxy=proxy)
dp = Dispatcher(bot=bot, storage=storage)

#----------------------------------------------------------------
init_db()

class BookingForm(StatesGroup):
    waiting_for_computer_id = State()
    waiting_for_start_time = State()
    waiting_for_end_time = State()

class FinishReservationForm(StatesGroup):
    waiting_for_user_id = State()

#----------------------------------------------------------------
@dp.message_handler(commands=['start'])
async def send_hi(message: types.Message):
    user_id = message.from_user.id
    add_user(user_id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    await message.answer_sticker('CAACAgIAAxkBAAEMmepmr33Ytd331wABh4WQHu9YmXgaRHYAAicOAAIqeghJicew1DRj78g1BA', reply_markup=all_menu)
#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Band qilish👑')
async def handle_band_qilish(message: types.Message):
    await message.answer('Iltimos, kompyuter raqamini kiriting (1-10).')
    await BookingForm.waiting_for_computer_id.set()

#----------------------------------------------------------------
@dp.message_handler(state=BookingForm.waiting_for_computer_id)
async def process_computer_id(message: types.Message, state: FSMContext):
    await state.update_data(computer_id=int(message.text))
    await message.answer('Boshlanish vaqtini (yyyy-mm-dd hh:mm) kiriting.')
    await BookingForm.waiting_for_start_time.set()

#----------------------------------------------------------------
@dp.message_handler(state=BookingForm.waiting_for_start_time)
async def process_start_time(message: types.Message, state: FSMContext):
    await state.update_data(start_time=message.text)
    await message.answer('Tugash vaqtini (yyyy-mm-dd hh:mm) kiriting.')
    await BookingForm.waiting_for_end_time.set()

#----------------------------------------------------------------
@dp.message_handler(state=BookingForm.waiting_for_end_time)
async def process_end_time(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    add_reservation(message.from_user.id, user_data['computer_id'], user_data['start_time'], message.text)
    await state.finish()
    await message.answer('Rezervatsiya muvaffaqiyatli amalga oshirildi.', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Bo\'sh joylarni tekshirish🎯')
async def handle_check_availability(message: types.Message):
    availability_info = 'Bo\'sh joylar:\n'
    for computer_id in range(1, 10):
        reserved = get_computer_reservations(computer_id)
        if reserved:
            availability_info += f"Kompyuter {computer_id}:\n"
            for reservation in reserved:
                availability_info += f" - {reservation[3]}  {reservation[4]}\n"
        else:
            availability_info += f"Kompyuter {computer_id} - Bo'sh\n"
    await message.answer(availability_info, reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.from_user.id == admin_id and message.text == 'Rezervatsiyalar ro\'yxati')
async def handle_admin_reservations(message: types.Message):
    reservations = get_reservations()
    reservation_list = "\n".join([
        f"Kompyuter {res[2]}: {res[3]} to {res[4]} - Foydalanuvchi ID: {res[1]}"
        for res in reservations
    ])
    await message.answer(f'Rezervatsiyalar ro\'yxati:\n{reservation_list}', reply_markup=admin_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Rezervatsiyani yopish' and message.from_user.id == admin_id)
async def handle_finish_reservation_start(message: types.Message):
    await message.answer('Iltimos, foydalanuvchi Telegram ID sini kiriting:')
    await FinishReservationForm.waiting_for_user_id.set()

@dp.message_handler(state=FinishReservationForm.waiting_for_user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    user_id = int(message.text)
    finish_reservation_by_user_id(user_id)
    await state.finish()
    await message.answer('Foydalanuvchi uchun rezervatsiya muvaffaqiyatli tugatildi.', reply_markup=admin_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Gazaklar🫕')
async def send_main_menu(message: types.Message):
    await message.answer('Gazaklar:', reply_markup=Gazak_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Sprite')
async def send_main_menu(message: types.Message):
    await message.answer('Iltimos qaysi kompyuterga ekanligini tanlang(1,10)', reply_markup=Sonlar_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Mountain dew')
async def send_main_menu(message: types.Message):
    await message.answer('Iltimos qaysi kompyuterga ekanligini tanlang(1,10)', reply_markup=Sonlar_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Mountain dew')
async def send_main_menu(message: types.Message):
    await message.answer('Iltimos qaysi kompyuterga ekanligini tanlang(1,10)', reply_markup=Sonlar_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Admin panel')
async def handle_admin_panel(message: types.Message):
    await message.answer('Admin paneliga xush kelibsiz.', reply_markup=admin_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '1️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '2️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '3️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '4️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '5️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '6️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '7️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '8️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '9️⃣')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '🔟')
async def send_main_menu(message: types.Message):
    await message.answer('Muvafaqiyatli qabul qilindi iltimos kuting☺️', reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '◀️Orqaga')
async def send_main_menu(message: types.Message):
    await message.answer(reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Texnik yordam so\'rash⚔️')
async def send_main_menu(message: types.Message):
    await message.answer('Agar yordam kerak bolsa adminga yoki quyidagi raqamlarga telefon qiling:\nAdmin: https://t.me/botir_4eveer\nRaqam:+998 (91) 378 77 76',reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    if message.from_user.id == admin_id:
        await message.answer('Admin paneliga xush kelibsiz.', reply_markup=admin_menu)
    else:
        await message.answer('Siz admin emassiz!')

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == '◀️Back to User menu')
async def send_main_menu(message: types.Message):
    await message.answer(reply_markup=all_menu)

#----------------------------------------------------------------
@dp.message_handler(lambda message: message.text == 'Komputer statistikasini bilish🖥')
async def send_main_menu(message: types.Message):
    await message.answer('Mana komputer statistikasi🖥:')
    await message.answer('MSI Infinite RS 13th:\nCPU: Intel Core i9-13900KF\nGPU: MSI RTX 4090 Surpim Liquid X\nMemory: 32GB DDR5\nStorage: 2TB NVMe SSD', reply_markup=all_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
