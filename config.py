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