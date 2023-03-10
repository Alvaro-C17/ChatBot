import random

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

def get_response(message: str) -> str:
    user_message = message.lower()

    if user_message == 'hello':
        return "What's up"

    if user_message == 'roll':
        return str(random.randint(1, 6))

    if user_message == '!8ball':
        return random.choice(ball_responses)

    if user_message == '!help':
        return "For a greeting please type : Hello" \
               "\nTo roll a dice, please type : Roll" \
               "\nTo use the magic 8 ball, type : !8ball"

    return 'Sorry, I didn\'t understand what you said. Try typing \'!help\''
