from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QuizApp")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.label = Label(text=f"Score {self.quiz.score}", pady=20, background=THEME_COLOR, foreground="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.questionText = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        rightImage = PhotoImage(file="images/true.png")
        self.rightButton = Button(image=rightImage, highlightthickness=0, command=self.truePressed)
        self.rightButton.grid(row=2, column=0)

        wrongImage = PhotoImage(file="images/false.png")
        self.wrongButton = Button(image=wrongImage, highlightthickness=0, command=self.falsePressed)
        self.wrongButton.grid(row=2, column=1)

        self.nextQuestion()

        self.window.mainloop()

    def nextQuestion(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questionText, text=q_text)
        else:
            self.canvas.itemconfig(self.questionText, text=f"Questions finished your score was {self.quiz.score}/10")
            self.rightButton.config(state="disabled")
            self.wrongButton.config(state="disabled")


    def truePressed(self):
        self.giveFeedback(self.quiz.check_answer("True"))

    def falsePressed(self):
        self.giveFeedback(self.quiz.check_answer("False"))

    def giveFeedback(self, feedback):
        if feedback:
            self.canvas.config(background="green")
            self.label.config(text=f"Score {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.nextQuestion)
