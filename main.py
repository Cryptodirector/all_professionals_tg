import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, types, F

from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo

from keyboards import back

from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = getenv("APITOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    builder = InlineKeyboardBuilder()
    buttons = [
        types.InlineKeyboardButton(text='Для компаний 🏢', callback_data='company'),
        types.InlineKeyboardButton(text='Реклама 📣', callback_data='advertising'),

    ]

    builder.row(
        types.InlineKeyboardButton(
            text="Регистрация специалистов 👷‍♂️", web_app=WebAppInfo(
                url='https://all-professionals.ru/'
            )
        )
    )
    builder.add(*buttons)
    builder.adjust(1)
    await message.answer_photo(photo=open('img/729103_find jobs _xl-1024-v1-0.png'))
    await message.answer(
        'Привет! Мы компания "ВСЕ ПРОФИ", предлагаем помощь специалистам в поиске работы в области'
        ' строительства с надежными компаниями и конкурентоспособной'
        ' заработной платой, а также помощь компаниям в поиске квалифицированных'
        ' специалистов для выполнения строительных работ.',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == 'company')
async def company(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    buttons = [
        types.InlineKeyboardButton(text='⬅  Назад', callback_data='back')

    ]
    builder.add(*buttons)
    builder.adjust(1)
    await callback.message.edit_text(
        'Мы компания, которая предоставляет услуги'
        ' в поиске квалифицированных специалистов в области строительства.'
        ' С нашей помощью вы можете легко найти действующих профессионалов'
        ' для выполнения различных строительных задач, от ремонта и отделки до крупных проектов.\n'
        'Для предоставления услуг обращаться ⬇\n'
        '@Vseprofff\n'
        '@sls212',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == 'advertising')
async def advertising(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    buttons = [
        types.InlineKeyboardButton(text='⬅  Назад', callback_data='back')

    ]
    builder.add(*buttons)
    builder.adjust(1)
    await callback.message.edit_text(
        'Для рекламы обращаться ⬇:\n'
        '@Vseprofff\n'
        '@sls212',
        reply_markup=builder.as_markup()
    )


@dp.callback_query(F.data == 'back')
async def back_in_menu(callback: types.CallbackQuery):
    await back(callback)


async def main() -> None:
    bot = Bot(
        token=TOKEN,
    )
    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())