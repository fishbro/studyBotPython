from database import get_user_chat_fields, modify_score

def carmaIncrease(to_id, chat_id):
	user_score = get_user_chat_fields(to_id, chat_id, ['score'])
	score = user_score['score'] + 1
	modify_score(to_id, chat_id, score)

	return score
