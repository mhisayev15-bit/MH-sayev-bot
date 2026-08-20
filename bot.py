import logging
from google import genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TELEGRAM_TOKEN = "8966463643:AAFBWDwCsC3uK4Rp3UWYjisrEaNW5SEi5CY"
GEMINI_API_KEY = "AQ.Ab8RN6I5txyNs8RU7PlKONWGK1IPi0GPrb2o9og8k5QU_y0CHw"
MY_ID = 8190618044

client = genai.Client(api_key=GEMINI_API_KEY)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salam! Mən süni intellekt botuyam. Sualınızı yazın!")

async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=user_text,
        )
        await update.message.reply_text(response.text)
    except Exception as e:
        print("DƏQİQ XƏTA:", e)
        await update.message.reply_text(f"Xəta kodu: {e}")
if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), ai_reply))
    
    print("Bot işə düşdü...")
    app.run_polling(drop_pending_updates=True)