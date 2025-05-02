# A dictionary that stores auestions and answers

quiz = {
    "question1": {
        "question": "What is the capital of France ?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany ?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Spain ?",
        "answer": "Madrid"
    },
    "question4": {
        "question": "What is the capital of America ?",
        "answer": "New York"
    },
    "question5": {
        "question": "What is the capital of Egypt ?",
        "answer": "Qaahira"
    },
    "question6": {
        "question": "What is the capital of Morocco ?",
        "answer": "Rabat"
    },
    "question7": {
        "question": "What is the capital of Italy ?",
        "answer": "Rome"
    }
}

score = 0
while True:
    for key, value in quiz.items():
        print(value['question'])
        answer = input("answer? ")
        if answer.lower() == value['answer'].lower():
            score = score + 1
            print("The answer is correct ! You've gained "+ str(score)+ " point " )
        else:
            print("You're answer is wrong, you're score: " + str(score))
            print("The answer is : "+ value['answer'])
    input_exite = input ("Do you want to play again (Y/N): ")
    if input_exite == 'Y' or input_exite == 'y':
        continue
    elif input_exite == 'N' or input_exite == 'n':
        break
    else:
        print("Hint: Enter y or n")
        input_exite = input ("Do you want to play again (Y/N): ")
        score = 0