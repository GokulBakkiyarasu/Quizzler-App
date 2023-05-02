from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.text = None
        self.window = Tk()
        self.window.title("QUZZILER")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.current_score_label = Label(text="Score: 0", fg="White", bg=THEME_COLOR)
        self.current_score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)

        self.question = self.canvas.create_text(150, 125, text="Some text", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.current_score_label.config(text=f"Score: {self.quiz.score}")
            self.text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=self.text)
        else:
            self.canvas.itemconfig(self.question, text="You have reached the end of the Quiz Game!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
