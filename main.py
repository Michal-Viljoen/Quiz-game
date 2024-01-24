from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
keep_playin=True

for questions in question_data:
    q_text=questions['text']
    q_answer=questions['answer']
    new_question=Question(q_text,q_answer)
    question_bank.append(new_question)

question=QuizBrain(question_bank)
while keep_playin:
    question.next_question()

    if question.next_question()==0 :
        keep_playin=False
        print("bye")
    elif question.next_question()==1:
        print(" That is the entire game ")
        keep_playin=False