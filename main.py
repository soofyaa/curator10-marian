import telebot

bot = telebot.TeleBot("6661874189:AAG-qxe8tpoLs-mBcfLDlNVdThqHUu3L9_E")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "твоя будущая зарплата 100...")


@bot.message_handler(commands=["maney"])
def main(message):
    bot.send_message(message.chat.id, "Хочешь денег будут деньги /nТы стараешься это самое главное")


@bot.message_handler(commands=["filosof"])
def main(message):
    bot.send_message(message.chat.id, "Каждый день, новый день")


@bot.message_handler(commands=["filney"])
def main(message):
    bot.send_message(message.chat.id, "Всё что ты хочешь, имеет цену")


@bot.message_handler(commands=["wealth"])
def main(message):
    bot.send_message(message.chat.id, "Что [ДЕНЬГИ!](https://youtu.be/iZEca2A3tS4?si=PIHnLC4gwlZ3fd3r)",
                     parse_mode="Markdown")


@bot.message_handler(commands=["calmness"])
def main(message):
    bot.send_message(message.chat.id, "На [Расслабоне](https://youtu.be/QZTDZFtbrec?si=NRgsYwedPWFbVmTh",
                     parse_mode="Markdown")


@bot.message_handler(commands=["bye"])
def main(message):
    bot.send_message(message.chat.id, "Мф верим в тебя /nУ тебя всё получится")


bot.infinity_polling()