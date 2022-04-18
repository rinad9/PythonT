from QuizQuestions import question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# how to represent this quiz?

# there are two parts to a question 
# 1. the prompts (actual question)
# 2. the answers

# both need to be tracked

# a. by building a CLASS called "quiz quistions"

# now building array of questions:

Questions = [
    question(question_prompts[0], "a"),
    question(question_prompts[1], "c"),
    question(question_prompts[2], "b")
]

# function to run the real test (takes one parameter that is a list of questions)
def run_test(Questions):
    # loop thru all questions
    # and get answer and check if its right
    # and keep track of the score
    score =0
    for question in Questions:
        # ask and store responce in score
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nyou got " + str(score) + "/" + str(len(Questions)) + " correct")


run_test(Questions)

