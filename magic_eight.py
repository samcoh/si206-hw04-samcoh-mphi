from random import randrange
user = input("What is your question?")
while user != "quit":
    def question():
        question = input("What is your question?")
        return question
    def checks_question(user):
        if "?" not in user:
            print("I’m sorry, I can only answer questions.")
        else:
            answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again',
            'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
            x = randrange(answers)
            print(answers[x])
    checks_question(user)
    user = question()
