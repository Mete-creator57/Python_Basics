# Quiz Game
# importing library for displaying long text
import textwrap
import shutil
width = shutil.get_terminal_size()
print(f'Columns: {width.columns}')
print(f'Lines: {width.lines}')
print('Each of the correct answers worth 10 points')

# init tuple of questions
questions = (
    "Which of the following is the largest desert on Earth? ",

    "Although it is not the closest planet to the sun, "
    "which planet in our solar system is the hottest?",

    " Which 1995 film made history as the "
    "first feature-length movie to be entirely computer-animated? " ,

     "Based on its weight and ability to exert force"
    " which muscle is the strongest in the human body? ",

     " Which of these foods is known "
        "for its unique chemical properties " 
        "that allow it to never spoil or go bad? ",
    )

# Creating 2d dimensional tuple to hold answers correspond to the questions
options = (
    ('A: Sahara Desert','B: Gobi Desert','C: Antarctica'),
    ('A: Venus','B: Mercury','C: Mars'),
    ('A: Toy Story','B: Antz','C: Tron'),
    ('A: Gluteus maximus','B: Heart','C: Jaw (Masseter)'),
    ('A: White Rice','B: Honey','C: Beef Jerky')


)
answers = ('C', 'A', 'A', 'C', 'B')
guesses = []
score = 0
question_num = 0

# iterating over questions
for question in questions:
    print('----- NEXT QUESTION -----')
    # formatting each question by using textwrap.dedent(iterable) function
    # using .strip() as it's a good practice to delete all remaining blank spaces
    formatted_question = textwrap.dedent(question).strip()
    print(textwrap.fill(formatted_question, width=width.columns))
    
    # iterating over all options for each question
    for option in options[question_num]:
        print(option)
    
    while True:
        guess = input('Enter your answer: ').upper()
        if guess == answers[question_num]:
            print('Correct!')
            guesses.append(guess)
            score += 1
            break
        
        # redundant code (just for practice)
        elif guess.isnumeric() or guess == '' or guess not in 'ABC':
            print('Invalid input. Try again....')
            continue

        else:
            print(f'Incorrect! The correct answer: {answers[question_num]}')
            guesses.append(guess)
            break

    # incrementing question num
    question_num = question_num + 1

print('--- Results --- ')
print('Your guesses:')

# iterating over user's guesses list, starting with index at 1
for i, guess in enumerate(guesses, 1): # starting at index 1
    print(f'\nQuestion number {i}: Your Guess: {guess} for question:\n{questions[i - 1].strip()}')
    print(f'Correct answer: {answers[i - 1]}')

# Printing total score in percentage
final_percentage = score / len(questions)
print(f'Your total score: {final_percentage:.0%}')


    

    