"""
Handler functions to be dispatched.
"""

from validators import is_registered, is_message_for_bot
from database import create_user
import messages


def start(bot, update):
	m = bot.message
	# print(m.from_user)
	# if not is_message_for_bot(m):
	# 	return

	print({'user_id': m.from_user.id, 'username': m.from_user.username})
	if not is_registered(m.from_user):
		m.reply_text(messages.START_MESSAGE)
		create_user({'user_id': m.from_user.id, 'username': m.from_user.username})
	else:
		m.reply_text(messages.CONTINUE_MESSAGE)


def stop(bot, update):
	# Unsubscribe user from bot
	bot.message.reply_text(messages.STOP_MESSAGE)


def normal_message(bot, update):
	m = bot.message
	chat = m.chat
	chat_id = chat.id
	text = m.text
	reply = m.reply_text
	print(m)
	# Handle non-command text messages