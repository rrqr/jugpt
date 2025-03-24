import telebot
import google.generativeai as genai

# -------------- إعدادات API --------------
TELEGRAM_BOT_TOKEN = "7845646320:AAHkK99Z8aSg2DxMHoHcFqLrc31tCuiOWKg"
GEMINI_API_KEY = "AIzaSyDIWsykvfhTOn48CQZ4RMcNj4feNbTTQ9o"

# تهيئة Telebot و Gemini API
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

# اختيار النموذج المناسب
model = genai.GenerativeModel("gemini-1.5-flash")  # استخدم النموذج المتاح لك


# -------------- الرد على الرسائل --------------
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🤖 أهلاً بك! أرسل أي سؤال وسأجيبك باستخدام Junai GPT ver 1.0")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "❌ حدث خطأ، حاول مرة أخرى لاحقًا.")
        print(f"Error: {e}")  # لتصحيح الأخطاء إذا حدثت

# تشغيل البوت
print("✅ البوت يعمل الآن...")
bot.polling()
