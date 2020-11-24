# TODO: Checking if the answer was correct
# TODO: Checking if we're at the end of quiz

# Practice again .. Because practice makes best!
from question_model import Question
from data import question_data
from quiz_brain import AskTheBrain

q_list = list()

def add_questions_to_list():
    for i in question_data:
        i_text = i["text"]
        i_answer = i["answer"]
        new_q = Question(i_text, i_answer)
        q_list.append(new_q)


add_questions_to_list()

quiz = AskTheBrain(q_list)
quiz.next_q()







