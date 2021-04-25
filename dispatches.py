"""
Handle registration.
"""

from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters

from handlers import start, stop, normal_message, conversation_message

MESSAGE = range(1)

dispatches = [
	CommandHandler('start', start),
	CommandHandler('stop', stop),

	MessageHandler(Filters.text, normal_message),

	ConversationHandler(
		entry_points=[CommandHandler('start', start)],
        states={
            MESSAGE: [MessageHandler(Filters.text, normal_message)],
        },
        fallbacks=[CommandHandler('stop', stop)]
	)
]