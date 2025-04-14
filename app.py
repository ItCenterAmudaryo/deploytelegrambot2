import aiogram.types
from aiogram import  Bot,Dispatcher,Router,F
from aiogram.filters import Command
from aiogram.types import  Message
from asyncio import run
from aiogram.types import  ReplyKeyboardMarkup#Reply
from  aiogram.utils.keyboard import ReplyKeyboardBuilder #Reply
from aiogram.types import  InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from  aiogram.types import  CallbackQuery
from aiogram.methods.edit_message_text import EditMessageText
from  os import  getenv
from dotenv import load_dotenv
import  sys
import  logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import  ParseMode
load_dotenv()
tokenim=getenv("BOT_TOKEN")
def get_inline()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="uz O'zbekiston",callback_data="uz")
    inline.button(text="kz Qozog'iston", callback_data="kz")
    inline.button(text="kg Qirg'iz", callback_data="kg")
    inline.button(text="tm Turmaniston", callback_data="tm")
    inline.button(text="ru Rossiya", callback_data="ru")
    inline.button(text="tjk Tojikiston", callback_data="tjk")

    # inline.button(text="Yo'q",callback_data="Yo'q")
    # inline.button(text="Yo'q", callback_data="Yo'q")
    inline.adjust(3)
    return  inline.as_markup()
def get_ha_yoq() -> ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    kb.button(text="Ha")
    kb.button(text="Yo'q")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
def tozalash()->InlineKeyboardMarkup:
    inline=InlineKeyboardBuilder()
    inline.button(text="Ha", callback_data="ha")
    inline.button(text="Yo'q",callback_data="yoq")
    return inline.as_markup()
dd=Dispatcher()

from  aiogram.client.default import DefaultBotProperties
global tanlov



# @dd.startup()
my_router=Router()
dd.include_router(my_router)
@my_router.startup()
async def bot_ishlaganda(bot:Bot):
     await  bot.send_message(chat_id=getenv("MY_ID"),\
                           text="Bot ishladi")

@my_router.shutdown()
async def bot_toxtaganda(bot: Bot):
    await  bot.send_message(chat_id=getenv("MY_ID"), \
                            text="Bot Toxtadi")
# @dd.message(Command('start'))
@my_router.message(Command('start'))
#Router yordamida xabar berish
async  def start_bosilganda(m:Message):
    await m.answer("Xush kelibsiz ",)
    await m.answer("Biror bir davlatni tanlang?:",reply_markup=get_inline())
from aiogram.handlers import CallbackQueryHandler
@my_router.callback_query(F.data == "uz")
async def uz_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan\
O'zbekistonni tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov="O'zbekiston"

@my_router.callback_query(F.data == "kz")
async def kz_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan Qozog'istonni tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov = "Qozog'iston"
@my_router.callback_query(F.data == "kg")
async def kg_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan\
 Qizg'izni tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov = "Qirg'iz"
@my_router.callback_query(F.data == "tm")
async def tm_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan\
Turkmanistonni tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov = "Turkmaniston"
@my_router.callback_query(F.data == "ru")
async def ru_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan\
Rossiyani tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov = "Rossiya"
@my_router.callback_query(F.data == "tjk")
async def tjk_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Siz haqiqatdan\
Tojikistonni tanladingizmi?")
        await call.message.edit_reply_markup(reply_markup=tozalash())
        global tanlov
        tanlov = "Tojikiston"
@my_router.callback_query(F.data=="ha")
async  def ha_tanlanganda(call:CallbackQuery):
    # await call.message.edit_reply_markup(reply_markup=tozalash())
    await call.message.delete_reply_markup()
    await call.message.delete()
    global  tanlov
    matn=str(tanlov)
    await call.message.answer(f"{matn}ni tanladingiz!",)
    r=getenv("ADMINS")

    await  call.bot.send_message(chat_id=getenv("ADMINS1"),\
      text=f"{call.from_user.full_name} {matn}ni tanladi")

@my_router.callback_query(F.data == "yoq")
async def ha_tanlanganda(call:CallbackQuery):
        await  call.message.edit_text("Biror bir davlatni tanlang?:")
        await call.message.edit_reply_markup(reply_markup=get_inline())


@my_router.message(F.text.lower()=="ha")
async  def ha_tanlanganda(m:Message):
    await m.answer("Oooo buyuk vatanparvar?!",\
 reply_markup=aiogram.types.ReplyKeyboardRemove())
@my_router.message(F.text.lower()=="yo'q")
async  def yoq_tanlanganda(m:Message):
    await m.answer("Grean karta o'ynang?!",\
 reply_markup=aiogram.types.ReplyKeyboardRemove())
@my_router.message()
async  def xabar_kelganda(m:Message,bot:Bot):
    await m.copy_to(chat_id=m.from_user.id)#Kim xabar yozsa shunga qaytadi

    await  m.copy_to(chat_id="692239005")#Shu Idga xabar borad

    await bot.send_message(chat_id="692239005",\
          text=f"{m.from_user.full_name} \
sizning botingizga  '{m.text}'  deb yozdi",)

async def main():
     botim=Bot(token=tokenim,\
default=DefaultBotProperties(parse_mode=ParseMode.HTML))
     # dd.startup.register(bot_ishlaganda)
     await  dd.start_polling(botim)
if __name__=="__main__":
   logging.basicConfig(level=logging.INFO,\
format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"\
,handlers=[
           logging.FileHandler("bot.log"),
           logging.StreamHandler(sys.stdout)
       ])
   run(main())