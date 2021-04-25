import sqlite3

import config
from config import tables


def _create_string(o):
	t = type(o)
	if t == str:
		return '"%s"' % o
	return str(o)


def create_connection():
	return sqlite3.connect('database.db', isolation_level=None)


def initialize_database():
	cursor = create_connection().cursor()

	for table in tables:
		fields = []
		for field_name in table['schema']:
			field = table['schema'][field_name]
			fields.append("%s %s %s" % (field_name, field['type'], field.get('options', '')))

		cursor.execute("CREATE TABLE IF NOT EXISTS %s (%s)" % (table['name'], ", ".join(fields)))


def get_user(id):
	return create_connection().cursor().execute("SELECT * FROM user WHERE user_id=%d" % id).fetchone()


def create_user(fields: dict):
	keys = list(fields)
	return create_connection().cursor().execute(
		'INSERT INTO user (%s) VALUES (%s)' % (
			",".join(field_name for field_name in keys),
			",".join(_create_string(fields[field_name]) for field_name in keys)
		)
	)

def create_chat(fields: dict):
	keys = list(fields)
	return create_connection().cursor().execute(
		'INSERT INTO chat (%s) VALUES (%s)' % (
			",".join(field_name for field_name in keys),
			",".join(_create_string(fields[field_name]) for field_name in keys)
		)
	)

def create_user_chat(fields: dict):
	keys = list(fields)
	return create_connection().cursor().execute(
		'INSERT INTO user_chat (%s) VALUES (%s)' % (
			",".join(field_name for field_name in keys),
			",".join(_create_string(fields[field_name]) for field_name in keys)
		)
	)


initialize_database()