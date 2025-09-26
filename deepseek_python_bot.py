import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ['8215604550:AAFLQSOd-dWgSnPTyfu493C1j1exQ6m-moQ']  # Will set in Railway

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎉 Bot is running 24/7! Send me an image or video.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text("📷 Image received! (Sticker feature coming soon)")
    elif update.message.video:
        await update.message.reply_text("🎥 Video received! (GIF feature coming soon)")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.PHOTO | filters.VIDEO, handle_message))
    
    print("🤖 Bot running 24/7 on Railway...")
    application.run_polling()

if __name__ == "__main__":
    main()