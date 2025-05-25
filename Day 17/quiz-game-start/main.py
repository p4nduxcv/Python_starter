from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_Question = QuestionModel(question_text,question_answer)
    question_bank.append(new_Question)

new_QuizBrain = QuizBrain(question_bank)

while new_QuizBrain.still_has_question():
    new_QuizBrain.next_question()

print(f"You Have Completed the Quiz Final Score: {new_QuizBrain.score}")