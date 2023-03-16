import random
from currency import convert_currency

ball_responses = [
    "It is certain",
    "Without a doubt",
    "You may rely on it",
    "Yes, definitely",
    "It is decidedly so",
    "As I see it, yes",
    "Most likely",
    "Yes",
    "Outlook good",
    "Signs point to yes",
    "Reply hazy, try again",
    "Better not tell you now",
    "Ask again later",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "Outlook not so good",
    "My sources say no",
    "Very doubtful",
    "My reply is no",
    "Yikes...",
    "Please DO NOT!",
    "Who wouldn't",
]

coin_flip = ["Heads", "Tails"]
def get_response(message: str) -> str:
    user_message = message.lower()

    if user_message == '!hello':
        return "What's up"

    if user_message == '!flip':
        return random.choice(coin_flip)

    if user_message == '!roll':
        return str(random.randint(1, 6))

    if user_message == '!8ball':
        return random.choice(ball_responses)

    if user_message.startswith('!convert'):
        try:
            _, amount, base_currency, target_currency = user_message.split(' ')
            result = convert_currency(float(amount), base_currency.upper(), target_currency.upper())
            return f"{amount} {base_currency.upper()} is {result} {target_currency.upper()}"
        except Exception as e:
            print(e)
            return "Sorry, I couldn't convert the currencies. Please try again with the correct format: !convert <amount> <base_currency> <target_currency>"

    if user_message == '!help':
        return "For a greeting please type : !hello" \
               "\nTo roll a dice, please type : !roll" \
               "\nTo use the magic 8 ball, type : !8ball" \
               "\nTo convert currencies, type : !convert <amount> <base_currency> <target_currency>"

    #return 'Sorry, I didn\'t understand what you said. Try typing \'!help\''

