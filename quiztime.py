import csv
import random

questions = []
wrong_questions = []  # List to store wrong questions and correct answers

with open('forestsquestions.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        questions.append(row)

num_questions = int(input("\nHow many questions do you want to be quizzed on? "))

score = 0
question_number = 0

for _ in range(num_questions):
    if not questions:
        print("No more questions available.")
        break

    question_number += 1

    selected_question = random.choice(questions)
    question = selected_question['Question']
    options = [selected_question['A'], selected_question['B'], selected_question['C'], selected_question['D']]
    correct_option = selected_question['Correct']

    random.shuffle(options)

    correct_index = options.index(selected_question[correct_option])

    print(f"\nQuestion {question_number}/{num_questions}: {question}")
    print("Options:")
    for i, option in enumerate(options):
        print(f"({chr(65 + i)}) {option}")

    user_answer = input("\nYour answer (A, B, C, or D): ").upper()

    if user_answer == chr(65 + correct_index):
        print("Correct! :)")
        score += 1
    else:
        print(f"Wrong. The correct option is ({chr(65 + correct_index)}) : {selected_question[correct_option]}")
        # Store the wrong question and correct answer
        wrong_questions.append((question, selected_question[correct_option]))

    questions.remove(selected_question)

print(f"\nYou got {score}/{num_questions} questions right.\n")

# Print all the wrong questions and their correct answers
if wrong_questions:
    print("Wrong Questions and Correct Answers:")
    for idx, (wrong_question, correct_answer) in enumerate(wrong_questions, start=1):
        print(f"{idx}. Question: {wrong_question}")
        print(f"   Correct Answer: {correct_answer}")
else:
    print("You got all the questions right! Well done!")
