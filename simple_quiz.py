def new_quiz():

    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in Options[questions_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1
    
    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        print((answer), "is the correct answer")
        return 0
              
def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")
    print("Answer: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

    if score >= 50:
        print("You Passed")
    else:
        print("You Failed")

questions = {
    "What is the process by which plants make their own food?: ": "A",
    "How many teeth does adult human have?: ": "B",
    "What is the largest planent in our solar system?: ": "C",
    "What force keeps us on the ground?: ": "A",
    "What is the smallest unit of life?: ": "D",
}  

Options = [["A. Photosynthesis", "B. Mechanization", "C. Fertilization", "D. Chlorophyl"],
           ["A. 30", "B. 32", "C. 24", "D. 36"],
           ["A. Mecury", "B. Earth", "C. Jupiter", "D. Uranus"],
           ["A. Gravity", "B. Friction", "C. Mechanical Force", "D. Thermodynamics"],
           ["A. Blood", "B. Organ", "C. System", "D. Cell"],]
new_quiz()