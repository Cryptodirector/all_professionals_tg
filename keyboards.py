from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo


async def back(
        callback: types.CallbackQuery,

):
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
    await callback.message.edit_text(
        'Привет! Мы компания "ВСЕ ПРОФИ", предлагаем помощь специалистам в поиске работы в области'
        ' строительства с надежными компаниями и конкурентоспособной'
        ' заработной платой, а также помощь компаниям в поиске квалифицированных'
        ' специалистов для выполнения строительных работ.',
        reply_markup=builder.as_markup()
    )