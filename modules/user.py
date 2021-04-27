from telegram import User, Chat
from validators import *
from database import create_user, create_chat, create_user_chat

def registerUser(user: User, chat: Chat):
	if not is_registered_user(user):
		create_user({'user_id': user.id, 'username': user.username})

	if not is_registered_chat(chat):
		create_chat({'chat_id': chat.id, 'chatname': chat.title})

	if not is_registered_user_chat(user, chat):
		create_user_chat({'user_id': user.id, 'chat_id': chat.id, 'score': 0})

	return True