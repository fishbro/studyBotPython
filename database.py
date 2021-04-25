import sqlite3

import config


def _create_string(o):
	t = type(o)
	if t == str:
		return '"%s"' % o
	return str(o)


def create_connection():
	return sqlite3.connect('database.db', isolation_level=None)


def initialize_database():
	cursor = create_connection().cursor()

	fields = []
	for field_name in config.user_schema:
		field = config.user_schema[field_name]
		fields.append("%s %s %s" % (field_name, field['type'], field.get('options', '')))

	cursor.execute("CREATE TABLE IF NOT EXISTS user (%s)" % ", ".join(fields))


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


initialize_database()