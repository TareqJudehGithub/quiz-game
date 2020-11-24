class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        return len(self.q_list) > self.q_number

    def next_q(self):
        current_q = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_q.text} (True/False) ")
        self.check_answer(user_answer, current_q.answer)
        print("")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Score: {self.score}")
        else:
            print("That's wrong.")
            print(f"Score: {self.score}")
        print(f"The correct answer is: {correct_answer}")
        print("\n")