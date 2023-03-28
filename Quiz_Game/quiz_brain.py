class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q{self.question_number}: {current_question.Text} (True/False)?: ")
        correct_ans = current_question.Answer
        self.check_answer(correct_ans, user_ans)

    def check_answer(self, correct_ans, user_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Yeay! You got it right.")
            self.score += 1
        else:
            print("That's a wrong answer!")
            print(f"The correct answer is {correct_ans}.")
        print(f"Your score is {self.score}/{self.question_number}.")
        print()



