class QuizBrain:
    def __init__(self,q_list):
       self.question_number=0
       self.question_list=q_list
       self.continues=True
       self.score=0


    def next_question(self):
        if self.question_number<12:

            current_question=self.question_list[self.question_number]
            self.question_number += 1
            user_answer=input(f"Q{self.question_number}. {current_question.text} IS this True or False: ")
            if user_answer==current_question.answer:
                self.score+=1
                print("You got the answer right ")
                print(f"That is correct your current score is {self.score}/{self.question_number}")

            else:
                print(f"That is wrong your current score is {self.score}/{self.question_number}")


        else:
            return 1