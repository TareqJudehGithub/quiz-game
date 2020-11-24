class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

# TODO: Asking the question:
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False) ")


class AskTheBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list

    def next_q(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        input(f"Q.{self.q_number}: {current_q.text} (True/False)")

