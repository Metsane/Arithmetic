import tkinter as tk
from random import randint, choice
from tkinter import messagebox

counter = 0  # Counter to keep track of the number of equations
user_score = 0


def confirm_quit():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        welcome_root.quit()


def welcomeWindow():
    global welcome_root, welcome_label, start_button, quit2
    welcome_root = tk.Tk()
    welcome_root.geometry("400x400")
    welcome_root.title("Welcome to Arithmetic Quiz")
    welcome_root.configure(background="yellow")
    tk.Label(welcome_root, text="\n").pack()

    welcome_label = tk.Label(
        welcome_root,
        text='Welcome to Arithmetic Quiz\n Click "start" to begin',
        font=("Helvetica", 18),
        fg="red",
    )

    welcome_label.pack(pady=50)

    start_button = tk.Button(
        welcome_root,
        text="Start Quiz",
        command=startPoint,
        bg="blue",  # Background color
        fg="white",  # Text color
        font=("Helvetica", 14),  # Font
        relief="raised",  # Border style
        borderwidth=3,
    )
    start_button.pack()
    quit2 = tk.Button(welcome_root, text="Quit", command=confirm_quit)
    quit2.pack(side="bottom", pady=10, padx=10, anchor="se")
    welcome_root.protocol("WM_DELETE_WINDOW", confirm_quit)


def startPoint():
    global welcome_label, start_button, quit2
    # Initialize the main window
    welcome_label.pack_forget()
    start_button.pack_forget()
    quit2.pack_forget()
    # Initialize variables
    global question_var, equation_var, score_var, totalScore, result_var, questionNum
    questionNum = 0
    question_var = tk.StringVar()
    equation_var = tk.StringVar()
    score_var = tk.StringVar(value="Score: 0")
    totalScore = tk.StringVar()
    result_var = tk.StringVar()

    # Create UI components
    create_widgets()

    # Call new_equation to display the first equation
    new_equation()


def create_widgets():
    global equation_label, answer_entry, next_button, result_label, questionNum, question_var, quiter, question_label
    questionNum = 0

    question_var.set("Question: 1")
    question_label = tk.Label(
        welcome_root, textvariable=question_var, font=("Helvetica", 18)
    )
    question_label.pack()

    equation_label = tk.Label(
        welcome_root, textvariable=equation_var, font=("Helvetica", 18)
    )
    equation_label.pack()

    answer_entry = tk.Entry(welcome_root)
    answer_entry.pack()

    next_button = tk.Button(welcome_root, text="Next", command=next_question)
    next_button.pack()

    result_label = tk.Label(
        welcome_root, textvariable=result_var, font=("Helvetica", 14)
    )
    result_label.pack()
    quiter = tk.Button(welcome_root, text="Quit", command=confirm_quit)
    quiter.pack(side="bottom", pady=10, padx=10, anchor="se")


def new_equation():
    global correct_answer, counter, equation_var, answer_entry, questionNum, question_var

    counter += 1
    equation, correct_answer = generate_equation()
    questionNum += 1
    equation_var.set(equation)
    answer_entry.delete(0, tk.END)
    if questionNum == 1:  # Set initial question number
        question_var.set("Question: 1")
    elif questionNum > 11:
        question_var.set()
    else:  # Update question number
        question_var.set(f"Question: {questionNum}")
    if counter == 11:
        show_score()
        counter = 0  # Reset the counter after displaying the score


# Function to generate a random arithmetic equation
def generate_equation():
    global correct_answer
    correct_answer = 0
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    operation = choice(list(operations.keys()))
    if operation in ["+", "-"]:
        num1, num2 = randint(1, 49), randint(1, 49) / 10.0
    elif operation in ["*", "/"]:
        num1, num2 = randint(1, 12), randint(1, 12) / 10.0
    equation = f"{num1} {operation} {num2}"
    correct_answer = operations[operation](num1, num2)
    return equation, round(correct_answer, 2)


# Function to update the score and show new equation
def next_question():
    global correct_answer, result_var, score_var, user_score

    try:
        user_answer = float(answer_entry.get())
        if user_answer == correct_answer:
            user_score += 1
            result_var.set("Correct!")
        else:
            result_var.set(f"incorrect! , the answer is: {correct_answer}")
            print(correct_answer)
    except ValueError:
        result_var.set("Please enter a valid answer.")

    new_equation()


# Function to display the final score
def show_score():
    global score_var, user_score, equation_label, next_button, answer_entry, quiter, finish_label, finishMessage_label, right_button, yes_button, correct_answer, totalScore, outOfMessage_label, finishResult_label

    question_label.pack_forget()
    equation_label.pack_forget()  # Hide operand label
    next_button.pack_forget()  # Hide next button
    answer_entry.pack_forget()
    quiter.pack_forget()
    result_label.pack_forget()
    result = tk.StringVar()
    finishResult = tk.StringVar()
    outOfScore = tk.StringVar()
    outOfScore.set(f"You scored: {user_score} out of {questionNum -1} answers")
    if user_score < 5:
        finishResult.set("You need to practice hard, You can do it.")
    elif user_score > 4 and user_score < 8:
        finishResult.set("Good work, just a little practice and you'll be at the top")
    elif user_score > 7:
        finishResult.set("Congratulations, You did Good!")
    totalScore.set("Congratulations. You have Finished the Game")
    score_var.set(f"Score: {user_score}")
    finishMessage = tk.StringVar()
    finishMessage.set("Do you want to play again?")
    yes_button = tk.Button(welcome_root, text="Yes", command=restart_quiz)
    right_button = tk.Button(welcome_root, text="Quit", command=confirm_quit)
    finish_label = tk.Label(
        welcome_root, textvariable=totalScore, font=("Helvetica", 15), wraplength=380
    )
    finish_label.pack()
    tk.Label(welcome_root, text="").pack()
    finishMessage_label = tk.Label(
        welcome_root, textvariable=outOfScore, font=("Helvetica", 15), wraplength=380
    )
    finishMessage_label.pack()
    tk.Label(welcome_root, text="").pack()
    finishResult_label = tk.Label(
        welcome_root, textvariable=finishResult, font=("Helvetica", 15), wraplength=380
    )
    finishResult_label.pack()
    tk.Label(welcome_root, text="").pack()
    outOfMessage_label = tk.Label(
        welcome_root, textvariable=finishMessage, font=("Helvetica", 15)
    )
    outOfMessage_label.pack()
    tk.Label(welcome_root, text="").pack()
    right_button.pack(side="right", pady=20, padx=10, anchor="se")
    yes_button.pack(side="right", pady=20, padx=20, anchor="se")


def restart_quiz():
    for widget in welcome_root.winfo_children():
        widget.destroy()
    global questionNum, counter, user_score, next_button, answer_entry, answer_entry, finish_label, finishMessage_label, right_button, yes_button, question_label, outOfMessage_label, finishResult_label
    questionNum = 0
    counter = 0
    user_score = 0
    finish_label.pack_forget()
    finishMessage_label.pack_forget()
    right_button.pack_forget()
    yes_button.pack_forget()
    outOfMessage_label.pack_forget()
    finishResult_label.pack_forget()
    create_widgets()
    result_var.set("")
    
    new_equation()


# Start the main loop
welcomeWindow()
welcome_root.mainloop()
