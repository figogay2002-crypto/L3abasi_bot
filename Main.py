import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! أنا بوت المستشار لعباسي 🤖 صيفط ليا أي سؤال.")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        prompt = f"جاوب بالدارجة المغربية البسيطة: {update.message.text}"
        response = model.generate_content(prompt)
        await update.message.reply_text(response.text)
    except:
        await update.message.reply_text("وقع مشكل بسيط، عاود جرب.")

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()
