from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ضع التوكن الخاص بك بين العلامات ""
TOKEN = "8730257834:AAEfqzPO-_RHjpbD0j_jlWLztvRbdcuqyqk"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        try:
            # يرسل الملف لأي شخص يرسل أي رسالة
            await update.message.reply_document(
                document=open("app-release (6).apk", "rb"),
                caption="تفضل، هذا هو الملف الجاهز ✅"
            )
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("البوت يعمل الآن...")
    app.run_polling()
