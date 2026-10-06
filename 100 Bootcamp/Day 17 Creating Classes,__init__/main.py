from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for entry in question_data:
    # for klucz in entry:
    #     print(klucz)
    #     print(entry[klucz])
    #     #print(entry[value])

    question = Question(entry["question"], entry["correct_answer"])

    question_bank.append(question)

print(question_bank[0].text)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions(): #Bez nawiasów still_has_questions to obiekt funkcji, a obiekty funkcji w Pythonie są zawsze truthy (prawdziwe), więc pętla while wykonuje się w nieskończoność. Pętla nie sprawdza faktycznie warunku — zawsze zakłada że jest True
    quiz.next_question()

print(f"Youve completed the quiz \nYour final score was {quiz.score}/{quiz.question_number}")