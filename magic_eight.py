user = input("What is your question?")
while user != "quit":
    def question():
        question = input("What is your question?")
        return question
    def checks_question(user):
        if "?" not in user:
            print("I’m sorry, I can only answer questions.")
    checks_question(user)
    user = question()
