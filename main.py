# TODO: Checking if the answer was correct
# TODO: Checking if we're at the end of quiz

# Practice again .. Because practice makes best!
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q_list = list()


def add_questions_to_list():
    for i in question_data:
        i_text = i["text"]
        i_answer = i["answer"]
        new_q = Question(i_text, i_answer)
        q_list.append(new_q)


add_questions_to_list()
quiz = QuizBrain(q_list)

while quiz.still_has_questions():
    quiz.next_q()

    if not quiz.still_has_questions():
        restart_quiz = input("restart_quiz? (y/n): ").lower()
        if restart_quiz == "y":
            quiz.q_number = 0
            quiz.score = 0
        else:

            print(f'''You've completed the quiz.
            Your final score is {quiz.score}.

            ''')








