import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        # Questions and answers
        self.questions = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        ]
        
        self.current_question_index = 0
        self.score = 0

        # Create widgets
        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        # Display the first question
        self.display_question()

    def display_question(self):
        if self.current_question_index < len(self.questions):
            question_text = self.questions[self.current_question_index]["question"]
            self.question_label.config(text=question_text)
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_final_score()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        correct_answer = self.questions[self.current_question_index]["answer"]
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
        self.current_question_index += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.display_question()

    def show_final_score(self):
        messagebox.showinfo("Quiz Over", f"Your final score is {self.score}!")
        self.root.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if _name_ == "_main_":
    main()