
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ForceReply

from helper import buttons, messages
from plugins import date_info, ratings

# Errors available, don't fork


# START MESSAGE

@bot.on_message(filters.command("start") & filters.private)
def command1(bot, message):
    text = "Use ReplyKeyboard..."
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f7dc9203585394d0595b1.jpg",
                   caption=messages.START_TEXT_CAPTION_TEXT),
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Learn bots section

@bot.on_message(filters.regex("Learn Bots"))
def reply_to_Learn_Bots(bot, message):
    text = messages.LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Restricted Stickers!!

@bot.on_message(filters.sticker)
async def restric_sticker(bot, message):
    bot.send_message(message.chat.id, "oops")


@bot.on_message(filters.regex("Song Download Bot🤖💖"))
def reply_to_utube(bot, message):
    bot.send_message(message.chat.id, "Song Downloader bot!!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/87ce14694a8c1d65cffaf.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/13218e7e5fb04f37d555e.jpg",
                   caption="<b>Step 2\nYou must send the song like this👇👇\n   ️/song Senorita</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3de0355d3fa67676e680.jpg", caption="<b>Step 3</b>")


@bot.on_message((filters.regex("Torrent Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Torrent downloader bot!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/cedb06244d2f74979095f.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/b5956b401cb68cd7b8d2f.jpg", caption="<b>Step 2</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3d2f02b3c7e4ab742bc8.jpg", caption="<b>Step 3</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/17f2f0820c5007b136086.jpg", caption="<b>Step 4</b>")


@bot.on_message((filters.regex("Youtube Video Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Youtube Video Downloader bot!!!")
    message.reply_chat_action("upload_photo")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/81aab8398259866256409.jpg", caption="<b>Step 1</b>")
    message.reply_chat_action("upload_photo")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/e1c08af0c0e5f28053855.jpg", caption="<b>Step 2</b>")
    message.reply_chat_action("upload_photo")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/3fc72cf3f77f4e4c3d28f.jpg", caption="<b>Step 3</b>")# Contact section

@bot.on_message(filters.regex("Contact 📞"))
def reply_to_Contact(bot, message):
    bot.send_message(message.chat.id, messages.CONTACT_TEXT)


# About Developer


# Home

@bot.on_message(filters.regex("Home"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )


# Feedbacks section

@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Credits

@bot.on_message(filters.regex("Credits"))
def reply_to_Credits(bot, message):
    text = messages.CREDITS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


INLINE_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("hello")
        ]
    ]
)


# Finish button and text

@bot.on_message(filters.private)
def reply_to_finish(bot, message):
    if message.text == "Yes, give it":
        bot.send_message(message.chat.id, messages.FINISH_TEXT_YES,
                         reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True,
                                                          one_time_keyboard=False))
    if message.text == "No, no need":
        bot.send_message(message.chat.id, messages.FINISH_TEXT_NON,
                         reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True,
                                                          one_time_keyboard=False))


# Changelog Section

@bot.on_message(filters.regex("Changelog"))
def reply_to_Changelog(bot, message):
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT, disable_web_page_preview=True, reply_markup=reply_markup)


# Assistant Bot Feedback/Report bugs centre

@bot.on_message(filters.regex("Sanila Assistant Bot"))
def reply_to_Assistant(bot, message):
    text = messages.SANILA_ASSISTANT_TEXT
    reply_markup = None
    message.reply(
        text=text, disable_web_page_preview=True,
        reply_markup=reply_markup
    )


# Reporting area - Song Downloader bot

@bot.on_message(filters.regex("Song Downloader Bot"))
def reply_to_Song(bot, message):
    text = messages.SONG_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


# Rating bots

@bot.on_message(filters.regex("Rate Bots"))
def reply_to_rate_bots(bot, message):
    text = ratings.RATINGS_TEXT
    reply_markup = ReplyKeyboardMarkup(ratings.RATINGS_BUTTONS, resize_keyboard=True, one_time_keyboard=False)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Rating bots

@bot.on_message(filters.regex("Assistant Bot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "How many stars would you like to give to Sanila Assistant Bot?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**Neither your ratings nor others ratings can see anyone due to privacy of users.** Your ratings will be **reset** when again "
                     "you came here to rate them but **these ratings will share with admin.**")


@bot.on_message(filters.regex("Torrent Bot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "How many stars would you like to give to Torrent Download Bot?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**Neither your ratings nor others ratings can see anyone due to privacy of users.** Your ratings will be **reset** when again "
                     "you came here to rate them but **these ratings will share with admin.**")


@bot.on_message(filters.regex("Youtube Bot"))
def reply_to_rating_assistant(bot, message):
    bot.send_poll(message.chat.id, "How many stars would you like to give to Youtube Video Download Bot?",
                  ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    bot.send_message(message.chat.id,
                     "**Neither your ratings nor others ratings can see anyone due to privacy of users.** Your ratings will be **reset** when again "
                     "you came here to rate them but **these ratings will share with admin.**")


@bot.on_message(filters.regex("Song Bot"))
async def reply_to_rating_assistant(bot, message):
    await bot.send_poll(message.chat.id, "How many stars would you like to give to Song Download Bot?",
                        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    await bot.send_message(message.chat.id,
                           "**Neither your ratings nor others ratings can see anyone due to privacy of users.** Your ratings will be **reset** when again "
                           "you came here to rate them but **these ratings will share with admin.**")


# Reporting area - Torrent downloader bot

@bot.on_message(filters.regex("Torrent Downloader Bot"))
def reply_to_Torrent(bot, message):
    text = messages.TORRENT_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


# Reporting area - Youtube video downloader bot

@bot.on_message(filters.regex("Youtube Video Downloader Bot"))
def reply_to_Youtube(bot, message):
    text = messages.YOUTUBE_VIDEO_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


PAGE_BUTTONS = [
    [
        InlineKeyboardButton("Send as high priority", callback_data="Send as high priority")
    ]
]


@bot.on_message(filters.private)
def fbb(bot, message):
    reply_markup = ForceReply(), InlineKeyboardMarkup(PAGE_BUTTONS)
    bot.send_message(message.chat.id,
                           f"**<u>Feedback Information</u>**\n\nMessage - `{message.text}`\nFeedback ID - {message.message_id}\nWord count - {message.text.split()}\nPosted by - {message.from_user.first_name}\n"
                           f"User ID - {message.from_user.id}\nUsername - @{message.chat.username}\nLanguage - {message.from_user.language_code}\nChat type - {message.chat.type}\nPosted date - {date_info.POSTED_DATE}\nPosted time - {date_info.POSTED_TIME}\n"
                           f"Date of reply - {date_info.DATE_OF_REPLY}\n\n"
                           f"<i>*Add more feedbacks or click finish to finish this process!</i>",
                           replY_markup=reply_markup, quote=True)
    TOCHE = bot.get_message()
    bot.send_message("me", TOCHE)
    if TOCHE == "Yes, give it":
        bot.send_message(message.chat.id, messages.FINISH_TEXT_YES)
    else:
        bot.send_message(message.chat.id, messages.FINISH_TEXT_NON)


@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "Send as high priority":
        CallbackQuery.send_message(
            messages.FINISH_TEXT_YES
        )
    else:
        CallbackQuery.send_message(
            messages.FINISH_TEXT_NON
        )


print("Not Wroking dont forkkkkk")

bot.run()
