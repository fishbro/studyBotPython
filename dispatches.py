"""
Handle registration.
"""

from telegram.ext import CommandHandler, MessageHandler, Filters

from handlers import start, stop, normal_message

dispatches = [
	CommandHandler('start', start),
	CommandHandler('stop', stop),

	MessageHandler(Filters.text, normal_message),
]