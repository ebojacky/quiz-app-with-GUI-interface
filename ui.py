import tkinter
import tkinter.messagebox
import quiz_brain

GREEN_FAINT = "#E9EFC0"
GREEN_LIGHT = "#B4E197"
GREEN_DEEP = "#83BD75"
GREEN_DEEPER = "#4E944F"


class QuizUI:
    def __init__(self, title: str, quiz: quiz_brain.QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.config(bg=GREEN_DEEP,
                           padx=20,
                           pady=20)
        self.score = tkinter.Label(text="Score: 0",
                                   font=("Arial", 20, "italic"),
                                   bg=GREEN_DEEP,
                                   fg=GREEN_FAINT)
        self.score.grid(row=0,
                        column=1)
        self.canvas = tkinter.Canvas(width=400,
                                     height=300,
                                     bg=GREEN_DEEPER,
                                     highlightthickness=0)
        self.canvas.grid(row=1,
                         column=0,
                         columnspan=2,
                         pady=20)
        self.question_text = self.canvas.create_text(200, 150,
                                                     width=380,
                                                     text="Question will display here",
                                                     font=("Arial", 20, "italic"),
                                                     fill=GREEN_LIGHT)

        true_photo = tkinter.PhotoImage(file="./images/TRUE.png")
        false_photo = tkinter.PhotoImage(file="./images/FALSE.png")
        self.true = tkinter.Button(image=true_photo,
                                   highlightthickness=0,
                                   bg=GREEN_DEEP,
                                   command=self.button_true_clicked)
        self.true.grid(row=2,
                       column=0)
        self.false = tkinter.Button(image=false_photo,
                                    highlightthickness=0,
                                    bg=GREEN_DEEP,
                                    command=self.button_false_clicked)
        self.false.grid(row=2,
                        column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz.next_question(), fill=GREEN_LIGHT)

    def button_true_clicked(self):
        self.process_answer("True")

    def button_false_clicked(self):
        self.process_answer("False")

    def process_answer(self, answer):
        is_user_correct = self.quiz.check_answer(answer)
        self.score.config(text=f"Score: {self.quiz.score}")
        if is_user_correct:
            feedback = "Correct!!"
            self.canvas.itemconfig(self.question_text,
                                   text=feedback,
                                   fill="green")
        else:
            feedback = "Wrong!!"
            self.canvas.itemconfig(self.question_text,
                                   text=feedback,
                                   fill="red")
        self.window.after(1000, self.continue_quiz)

    def continue_quiz(self):
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Quiz Over\n"
                                        f"Final Score : {self.quiz.score}"
                                        f"/{self.quiz.total_questions()}",
                                   fill=GREEN_LIGHT)

            self.true.config(state="disabled")
            self.false.config(state="disabled")
