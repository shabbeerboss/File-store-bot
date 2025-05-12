from telegram.ext import Updater, CommandHandler

# Your bot token
TOKEN = "7907546896:AAGA00zinIvSHBtYgAXTWbOwe58_9JNfWMg"

# Mapping of start parameters to Telegram file_ids
file_mapping = {
    "file1": "BQACAgUAAxkBAAIBGmV1...",  # Replace with real file_id
    "file2": "CAACAgUAAxkBAAIBHGV1...",  # Replace with real file_id
    "file3": "DQACAgUAAxkBAAIBIGV1..."   # Replace with real file_id
}

def start(update, context):
    args = context.args
    if args:
        param = args[0]
    n file_mapping:
            file_id = file_mapping[param]
            context.bot.send_document(chat_id=update.effective_chat.id, document=file_id)
     
            updsage.re