## TODO 1: Ask questions, 2: Check answer, 3: Check if end of quiz
## TODO attributes: question number, question list
## TODO method: next question


class quiz():
    def __init__(self, question_data):
        self.question_number = 0
        self.question_list = question_data
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q{self.question_number + 1}. True or False: {current_question.text}: ")
        if answer == current_question.answer:
            self.score += 1
        print(f"Your score is {self.score}/{self.question_number + 1}")
        print("\n")
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
