import random


def get_response(message: str) -> str:
    user_message = message.lower()

    if user_message == 'hello':
        return "What's up"

    if user_message == 'roll':
        return str(random.randint(1, 6))

    if user_message == '!help':
        return "For a greeting please type : Hello" \
               "To roll a dice, please type : Roll"

    return 'Sorry, I didn\'t understand what you said. Try typing \'!help\''
