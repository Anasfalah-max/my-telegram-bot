import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# سيتم جلب التوكن من إعدادات Railway للحماية
TOKEN = os.getenv("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # التأكد أن الرسالة تحتوي على نص
    if update.message.text:
        try:
            # إرسال ملف الـ APK المرفوع في نفس المجلد
            await update.message.reply_document(
                document=open("app-release (6).apk", "rb"),
                caption="تفضل، هذا هو ملف التطبيق الخاص بك ✅"
            )
        except FileNotFoundError:
            await update.message.reply_text("خطأ: الملف غير موجود في السيرفر.")
        except Exception as e:
            print(f"Error: {e}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("البوت يعمل الآن...")
app.run_polling()
