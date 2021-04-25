"""
Settings and configuration for your bot.
"""

from userconfig import TOKEN

# Bot's API Token granted by the @BotFather
api_token = TOKEN

# This field will be auto-populated
username = None

# A list of user IDs who can manage the bot
admins = []

user_schema = {
	'user_id': {
		'type': 'INTEGER',
		'options': 'PRIMARY KEY'
	},
    'username': {
        'type': 'TEXT'
    }
}

chat_schema = {
	'chat_id': {
		'type': 'INTEGER',
		'options': 'PRIMARY KEY'
	},
    'chatname': {
        'type': 'TEXT'
    }
}

user_chat_schema = {
	'id': {
		'type': 'INTEGER',
		'options': 'PRIMARY KEY AUTOINCREMENT'
	},
	'user_id': {
		'type': 'INTEGER',
	},
	'chat_id':{
		'type': 'INTEGER',
	},
    'score': {
        'type': 'INTEGER',
    }
}

tables = [
	{
		'name': 'user', 
		'schema': user_schema
	},
	{
		'name': 'chat', 
		'schema': chat_schema
	},
	{
		'name': 'user_chat', 
		'schema': user_chat_schema
	}
]