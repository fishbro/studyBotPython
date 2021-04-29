"""
Handle registration.
"""

from telegram.ext import CommandHandler, MessageHandler, Filters
from handlers import start, stop, normal_message, plus_message

dispatches = [
    CommandHandler("start", start),
    CommandHandler("stop", stop),
    MessageHandler(Filters.text & Filters.reply & Filters.regex(r"\+(.*)"), plus_message),
    MessageHandler(Filters.text, normal_message),
]
