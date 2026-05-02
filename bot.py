import os
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Настройки

TELEGRAM_TOKEN = os.environ.get(“TELEGRAM_TOKEN”, “8365752786:AAE8lWS1DywCnp_flLCRKed8oeGFxAT1_ZA”)
GEMINI_API_KEY = os.environ.get(“GEMINI_API_KEY”, “AIzaSyCGdNM8tkOve3J1hlq7QOji8awUxbP19pY”)

# Системный промпт — настрой характер бота здесь

SYSTEM_PROMPT = “Ты полезный помощник. Отвечай кратко и по делу на русском языке.”

# Инициализация Gemini

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(“gemini-1.5-flash”, system_instruction=SYSTEM_PROMPT)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
user_message = update.message.text
print(f”Сообщение от {update.effective_user.first_name}: {user_message}”)

```
try:
    response = model.generate_content(user_message)
    await update.message.reply_text(response.text)
except Exception as e:
    await update.message.reply_text("Произошла ошибка, попробуй ещё раз.")
    print(f"Ошибка: {e}")
```

def main():
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
print(“Бот запущен!”)
app.run_polling()

if **name** == “**main**”:
main()
