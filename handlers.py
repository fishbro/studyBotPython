"""
Handler functions to be dispatched.
"""

from validators import is_registered_user, is_message_for_bot
from modules.user import registerUser
import messages
from modules.carma import carmaIncrease


def start(bot, update):
	registerUser(bot.message.from_user, bot.message.chat)
	m = bot.message

	m.reply_text(messages.CONTINUE_MESSAGE % m.from_user.username)


def stop(bot, update):
	# Unsubscribe user from bot
	bot.message.reply_text(messages.STOP_MESSAGE)


def normal_message(bot, update):
	registerUser(bot.message.from_user, bot.message.chat)
	m = bot.message

	print('normal')

	# chat = m.chat
	# chat_id = chat.id
	# text = m.text
	# reply = m.reply_text
	# print(m)
	# # Handle non-command text messages

def plus_message(bot, update):
	registerUser(bot.message.from_user, bot.message.chat)
	m = bot.message
	from_id = m.reply_to_message.from_user.id
	to_id = m.from_user.id
	chat_id = m.chat.id

	if from_id == to_id:
		bot.message.reply_text(messages.PLUS_ERROR_YURSELF)
		return False

	new_score = carmaIncrease(to_id, chat_id)
	bot.message.reply_text(messages.PLUS_MESSAGE % (m.from_user.username, m.reply_to_message.from_user.username, new_score))

	# chat = m.chat
	# chat_id = chat.id
	# text = m.text
	# reply = m.reply_text
	# print(m)
	# # Handle non-command text messages