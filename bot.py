import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# API OpenAI 
openai.api_key = "your-openai-api-key"

# token bot telegram
TELEGRAM_API_TOKEN = "your-telegram-bot-token"


def get_response_from_openai(user_message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # مدل GPT-3
            prompt=user_message,
            max_tokens=150,  # طول پاسخ حداکثر
            temperature=0.7  # میزان خلاقیت پاسخ
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"خطا در پردازش درخواست: {e}"


def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text  # پیام ورودی کاربر
    bot_response = get_response_from_openai(user_message)  # دریافت پاسخ از OpenAI
    update.message.reply_text(bot_response)  # ارسال پاسخ به کاربر


def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! چطور می‌توانم به شما کمک کنم؟")


def main():

    updater = Updater(TELEGRAM_API_TOKEN)


    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))


    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))


    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
