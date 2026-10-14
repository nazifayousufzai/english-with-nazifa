
import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


APP_NAME = "English with Nazifa"
DATA_FILE = Path(__file__).with_name("progress.json")

GREEN = "#16866A"
DARK = "#172B3A"
LIGHT = "#F3F7F6"
WHITE = "#FFFFFF"
GOLD = "#E8B44F"


VOCABULARY = [
    {
        "word": "Achieve",
        "meaning": "به دست آوردن، موفق شدن",
        "example": "You can achieve your dreams.",
        "level": "Intermediate",
    },
    {
        "word": "Brave",
        "meaning": "شجاع",
        "example": "She is a brave young woman.",
        "level": "Beginner",
    },
    {
        "word": "Confident",
        "meaning": "بااعتمادبه‌نفس",
        "example": "Speak English with confidence.",
        "level": "Intermediate",
    },
    {
        "word": "Discover",
        "meaning": "کشف کردن",
        "example": "I want to discover new things.",
        "level": "Beginner",
    },
    {
        "word": "Education",
        "meaning": "آموزش، تعلیم و تربیه",
        "example": "Education can change our lives.",
        "level": "Beginner",
    },
    {
        "word": "Encourage",
        "meaning": "تشویق کردن",
        "example": "Teachers encourage their students.",
        "level": "Intermediate",
    },
    {
        "word": "Freedom",
        "meaning": "آزادی",
        "example": "Everyone deserves freedom.",
        "level": "Beginner",
    },
    {
        "word": "Grateful",
        "meaning": "سپاسگزار",
        "example": "I am grateful for your help.",
        "level": "Intermediate",
    },
    {
        "word": "Improve",
        "meaning": "بهبود بخشیدن، بهتر ساختن",
        "example": "Practice every day to improve your English.",
        "level": "Beginner",
    },
    {
        "word": "Knowledge",
        "meaning": "دانش، آگاهی",
        "example": "Knowledge gives us power.",
        "level": "Intermediate",
    },
    {
        "word": "Opportunity",
        "meaning": "فرصت",
        "example": "This course is a great opportunity.",
        "level": "Intermediate",
    },
    {
        "word": "Perseverance",
        "meaning": "پشتکار، استقامت",
        "example": "Perseverance helps us reach our goals.",
        "level": "Advanced",
    },
    {
        "word": "Respect",
        "meaning": "احترام",
        "example": "We should respect one another.",
        "level": "Beginner",
    },
    {
        "word": "Successful",
        "meaning": "موفق",
        "example": "Hard work helps you become successful.",
        "level": "Intermediate",
    },
    {
        "word": "Wisdom",
        "meaning": "خرد، دانایی",
        "example": "Wisdom comes from learning and experience.",
        "level": "Advanced",
    },
]


def load_progress():
    default = {
        "learned": [],
        "quizzes": 0,
        "correct": 0,
        "answered": 0,
    }

    try:
        if DATA_FILE.exists():
            saved = json.loads(
                DATA_FILE.read_text(encoding="utf-8")
            )

            for key in default:
                if key in saved:
                    default[key] = saved[key]

    except (OSError, json.JSONDecodeError):
        pass

    return default


class EnglishLearningApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(APP_NAME)
        self.geometry("900x650")
        self.minsize(720, 520)
        self.configure(bg=LIGHT)

        self.progress = load_progress()
        self.vocab_index = 0
        self.search_results = list(range(len(VOCABULARY)))
        self.quiz_questions = []
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_answered = False

        self.setup_styles()
        self.show_home()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "TButton",
            font=("Segoe UI", 11),
            padding=9,
        )

        style.configure(
            "Green.TButton",
            background=GREEN,
            foreground=WHITE,
        )

        style.map(
            "Green.TButton",
            background=[("active", "#106B55")],
        )

    def save_progress(self):
        try:
            DATA_FILE.write_text(
                json.dumps(
                    self.progress,
                    ensure_ascii=False,
                    indent=4,
                ),
                encoding="utf-8",
            )
        except OSError as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save progress:\n{error}",
            )

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def make_header(self, subtitle):
        header = tk.Frame(self, bg=DARK, padx=25, pady=18)
        header.pack(fill="x")

        tk.Label(
            header,
            text=APP_NAME,
            font=("Segoe UI", 22, "bold"),
            bg=DARK,
            fg=WHITE,
        ).pack(anchor="w")

        tk.Label(
            header,
            text=subtitle,
            font=("Segoe UI", 11),
            bg=DARK,
            fg="#C8DAD5",
        ).pack(anchor="w", pady=(5, 0))

    def make_button(self, parent, text, command):
        return ttk.Button(
            parent,
            text=text,
            command=command,
            style="Green.TButton",
        )

    def make_card(self, parent, title, description, command):
        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#DCE7E3",
            highlightthickness=1,
            padx=18,
            pady=18,
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 15, "bold"),
            bg=WHITE,
            fg=DARK,
        ).pack(anchor="w")

        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 10),
            bg=WHITE,
            fg="#536570",
            wraplength=260,
            justify="left",
        ).pack(anchor="w", pady=10)

        self.make_button(
            card,
            "Open →",
            command,
        ).pack(anchor="w", pady=(5, 0))

        return card

    def show_home(self):
        self.clear_content()
        self.make_header("Learn English. Build confidence. Reach your dreams.")

        main = tk.Frame(self, bg=LIGHT, padx=25, pady=25)
        main.pack(fill="both", expand=True)

        tk.Label(
            main,
            text="Welcome, English Learner!",
            font=("Segoe UI", 21, "bold"),
            bg=LIGHT,
            fg=DARK,
        ).pack(anchor="w")

        tk.Label(
            main,
            text="Small steps every day lead to big achievements.",
            font=("Segoe UI", 12),
            bg=LIGHT,
            fg="#536570",
        ).pack(anchor="w", pady=(5, 20))

        cards = tk.Frame(main, bg=LIGHT)
        cards.pack(fill="x")

        cards.columnconfigure(0, weight=1)
        cards.columnconfigure(1, weight=1)

        self.make_card(
            cards,
            "📚 Vocabulary",
            "Learn new words, meanings and example sentences.",
            self.show_vocabulary,
        ).grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=8)

        self.make_card(
            cards,
            "✍ English Quiz",
            "Test your vocabulary with multiple-choice questions.",
            self.start_quiz,
        ).grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=8)

        self.make_card(
            cards,
            "📈 My Progress",
            "Review your learned words and quiz results.",
            self.show_progress,
        ).grid(row=1, column=0, sticky="nsew", padx=(0, 8), pady=8)

        self.make_card(
            cards,
            "🔎 Search Words",
            "Find an English word in the vocabulary list.",
            self.show_vocabulary,
        ).grid(row=1, column=1, sticky="nsew", padx=(8, 0), pady=8)

        tk.Label(
            main,
            text=(
                f"Vocabulary available: {len(VOCABULARY)} words"
                f"     |     Words learned: "
                f"{len(self.progress['learned'])}"
            ),
            font=("Segoe UI", 10, "bold"),
            bg=LIGHT,
            fg=GREEN,
        ).pack(anchor="w", pady=18)

    def show_vocabulary(self):
        self.clear_content()
        self.make_header("Vocabulary Learning Center")

        main = tk.Frame(self, bg=LIGHT, padx=25, pady=20)
        main.pack(fill="both", expand=True)

        nav = tk.Frame(main, bg=LIGHT)
        nav.pack(fill="x")

        self.make_button(
            nav, "← Home", self.show_home
        ).pack(side="left")

        self.make_button(
            nav, "My Progress", self.show_progress
        ).pack(side="right")

        tk.Label(
            main,
            text="Search for an English word",
            font=("Segoe UI", 12, "bold"),
            bg=LIGHT,
            fg=DARK,
        ).pack(anchor="w", pady=(20, 5))

        search_row = tk.Frame(main, bg=LIGHT)
        search_row.pack(fill="x")

        self.search_entry = ttk.Entry(
            search_row,
            font=("Segoe UI", 12),
        )
        self.search_entry.pack(
            side="left", fill="x", expand=True, ipady=6
        )

        self.make_button(
            search_row,
            "Search",
            self.search_vocabulary,
        ).pack(side="left", padx=8)

        self.search_entry.bind(
            "<Return>",
            lambda event: self.search_vocabulary(),
        )

        self.word_card = tk.Frame(
            main,
            bg=WHITE,
            padx=25,
            pady=25,
            highlightbackground="#DCE7E3",
            highlightthickness=1,
        )
        self.word_card.pack(fill="both", expand=True, pady=18)

        self.word_label = tk.Label(
            self.word_card,
            text="",
            font=("Segoe UI", 28, "bold"),
            bg=WHITE,
            fg=GREEN,
        )
        self.word_label.pack(pady=(10, 5))

        self.level_label = tk.Label(
            self.word_card,
            text="",
            font=("Segoe UI", 10, "italic"),
            bg=WHITE,
            fg="#657781",
        )
        self.level_label.pack()

        self.meaning_label = tk.Label(
            self.word_card,
            text="",
            font=("Segoe UI", 16),
            bg=WHITE,
            fg=DARK,
        )
        self.meaning_label.pack(pady=15)

        self.example_label = tk.Label(
            self.word_card,
            text="",
            font=("Segoe UI", 12, "italic"),
            bg=WHITE,
            fg="#536570",
            wraplength=650,
        )
        self.example_label.pack(pady=10)

        self.counter_label = tk.Label(
            self.word_card,
            text="",
            font=("Segoe UI", 10),
            bg=WHITE,
            fg=GREEN,
        )
        self.counter_label.pack(pady=10)

        controls = tk.Frame(main, bg=LIGHT)
        controls.pack(fill="x")

        self.make_button(
            controls,
            "← Previous",
            self.previous_word,
        ).pack(side="left")

        self.make_button(
            controls,
            "Mark as Learned ✓",
            self.mark_learned,
        ).pack(side="left", padx=10)

        self.make_button(
            controls,
            "Next Word →",
            self.next_word,
        ).pack(side="right")

        self.display_word()

    def display_word(self):
        if not self.search_results:
            return

        index = self.search_results[self.vocab_index]
        item = VOCABULARY[index]

        self.word_label.config(text=item["word"])
        self.level_label.config(text=f"Level: {item['level']}")
        self.meaning_label.config(text=item["meaning"])
        self.example_label.config(
            text=f'Example: {item["example"]}'
        )

        self.counter_label.config(
            text=(
                f"Word {self.vocab_index + 1} "
                f"of {len(self.search_results)}"
            )
        )

    def search_vocabulary(self):
        query = self.search_entry.get().strip().lower()

        if not query:
            self.search_results = list(range(len(VOCABULARY)))
            self.vocab_index = 0
            self.display_word()
            return

        results = [
            i for i, item in enumerate(VOCABULARY)
            if query in item["word"].lower()
            or query in item["meaning"].lower()
        ]

        if not results:
            messagebox.showinfo(
                "Vocabulary Search",
                "Word not found in our vocabulary list yet.",
            )
            return

        self.search_results = results
        self.vocab_index = 0
        self.display_word()

    def next_word(self):
        if not self.search_results:
            return

        self.vocab_index = (
            self.vocab_index + 1
        ) % len(self.search_results)

        self.display_word()

    def previous_word(self):
        if not self.search_results:
            return

        self.vocab_index = (
            self.vocab_index - 1
        ) % len(self.search_results)

        self.display_word()

    def mark_learned(self):
        index = self.search_results[self.vocab_index]
        word = VOCABULARY[index]["word"]

        if word in self.progress["learned"]:
            messagebox.showinfo(
                "Vocabulary",
                f"You have already learned {word}.",
            )
            return

        self.progress["learned"].append(word)
        self.save_progress()

        messagebox.showinfo(
            "Well Done!",
            f"{word} has been added to your learned words!",
        )

        self.show_vocabulary()

    def start_quiz(self):
        self.clear_content()
        self.make_header("Vocabulary Challenge")

        self.quiz_questions = random.sample(
            VOCABULARY,
            min(10, len(VOCABULARY)),
        )

        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_answered = False

        self.quiz_area = tk.Frame(
            self, bg=LIGHT, padx=30, pady=25
        )
        self.quiz_area.pack(fill="both", expand=True)

        self.make_button(
            self.quiz_area,
            "← Home",
            self.show_home,
        ).pack(anchor="w")

        self.question_label = tk.Label(
            self.quiz_area,
            text="",
            font=("Segoe UI", 18, "bold"),
            bg=LIGHT,
            fg=DARK,
            wraplength=700,
        )
        self.question_label.pack(pady=(35, 20))

        self.options_frame = tk.Frame(
            self.quiz_area, bg=LIGHT
        )
        self.options_frame.pack(fill="x")

        self.feedback_label = tk.Label(
            self.quiz_area,
            text="",
            font=("Segoe UI", 12, "bold"),
            bg=LIGHT,
        )
        self.feedback_label.pack(pady=15)

        self.next_button = self.make_button(
            self.quiz_area,
            "Next Question →",
            self.next_question,
        )
        self.next_button.pack(pady=10)
        self.next_button.config(state="disabled")

        self.show_question()

    def show_question(self):
        if self.quiz_index >= len(self.quiz_questions):
            self.finish_quiz()
            return

        self.quiz_answered = False
        item = self.quiz_questions[self.quiz_index]

        self.question_label.config(
            text=(
                f"Question {self.quiz_index + 1} "
                f"of {len(self.quiz_questions)}\n\n"
                f"What is the meaning of '{item['word']}'?"
            )
        )

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        self.feedback_label.config(text="", fg=DARK)
        self.next_button.config(state="disabled")

        wrong_items = [
            v for v in VOCABULARY
            if v["word"] != item["word"]
        ]

        wrong_options = random.sample(
            wrong_items,
            min(3, len(wrong_items)),
        )

        options = [item] + wrong_options
        random.shuffle(options)

        for option in options:
            button = ttk.Button(
                self.options_frame,
                text=option["meaning"],
                command=lambda selected=option: (
                    self.check_answer(selected)
                ),
            )
            button.pack(fill="x", pady=5, ipady=5)

    def check_answer(self, selected):
        if self.quiz_answered:
            return

        self.quiz_answered = True
        item = self.quiz_questions[self.quiz_index]

        self.progress["answered"] += 1

        if selected["word"] == item["word"]:
            self.quiz_score += 1
            self.progress["correct"] += 1

            self.feedback_label.config(
                text="Correct! Excellent work! ✓",
                fg=GREEN,
            )
        else:
            self.feedback_label.config(
                text=f"Not quite. Correct answer: {item['meaning']}",
                fg="#B54747",
            )

        self.save_progress()
        self.next_button.config(state="normal")

    def next_question(self):
        if not self.quiz_answered:
            return

        self.quiz_index += 1
        self.show_question()

    def finish_quiz(self):
        self.clear_content()
        self.make_header("Quiz Results")

        result = tk.Frame(
            self, bg=LIGHT, padx=30, pady=40
        )
        result.pack(fill="both", expand=True)

        total = len(self.quiz_questions)
        percentage = round(
            self.quiz_score / total * 100
        ) if total else 0

        self.progress["quizzes"] += 1
        self.save_progress()

        tk.Label(
            result,
            text="Quiz Completed!",
            font=("Segoe UI", 25, "bold"),
            bg=LIGHT,
            fg=GREEN,
        ).pack(pady=15)

        tk.Label(
            result,
            text=f"{self.quiz_score} / {total}",
            font=("Segoe UI", 32, "bold"),
            bg=LIGHT,
            fg=DARK,
        ).pack(pady=10)

        tk.Label(
            result,
            text=f"Your score: {percentage}%",
            font=("Segoe UI", 16),
            bg=LIGHT,
            fg=DARK,
        ).pack(pady=5)

        if percentage >= 80:
            message = "Amazing! Keep up the great work!"
        elif percentage >= 50:
            message = "Good effort! Practice a little more."
        else:
            message = "Keep learning. Every attempt helps!"

        tk.Label(
            result,
            text=message,
            font=("Segoe UI", 12),
            bg=LIGHT,
            fg="#536570",
        ).pack(pady=15)

        self.make_button(
            result,
            "Try Again",
            self.start_quiz,
        ).pack(pady=5)

        self.make_button(
            result,
            "Back to Home",
            self.show_home,
        ).pack(pady=5)

    def show_progress(self):
        self.clear_content()
        self.make_header("Your Learning Progress")

        main = tk.Frame(
            self, bg=LIGHT, padx=30, pady=25
        )
        main.pack(fill="both", expand=True)

        self.make_button(
            main,
            "← Home",
            self.show_home,
        ).pack(anchor="w")

        learned = len(self.progress["learned"])
        quizzes = self.progress["quizzes"]
        answered = self.progress["answered"]
        correct = self.progress["correct"]

        accuracy = round(correct / answered * 100) if answered else 0

        stats = [
            ("Words Learned", str(learned)),
            ("Quizzes Completed", str(quizzes)),
            ("Questions Answered", str(answered)),
            ("Quiz Accuracy", f"{accuracy}%"),
        ]

        for title, value in stats:
            card = tk.Frame(
                main,
                bg=WHITE,
                padx=18,
                pady=12,
                highlightbackground="#DCE7E3",
                highlightthickness=1,
            )
            card.pack(fill="x", pady=6)

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 11),
                bg=WHITE,
                fg="#536570",
            ).pack(side="left")

            tk.Label(
                card,
                text=value,
                font=("Segoe UI", 16, "bold"),
                bg=WHITE,
                fg=GREEN,
            ).pack(side="right")

        tk.Label(
            main,
            text="Words You Have Learned",
            font=("Segoe UI", 14, "bold"),
            bg=LIGHT,
            fg=DARK,
        ).pack(anchor="w", pady=(20, 8))

        learned_words = self.progress["learned"]

        if learned_words:
            words_text = ", ".join(learned_words)

            tk.Label(
                main,
                text=words_text,
                font=("Segoe UI", 11),
                bg=LIGHT,
                fg=DARK,
                wraplength=750,
                justify="left",
            ).pack(anchor="w")
        else:
            tk.Label(
                main,
                text="You haven't marked any words as learned yet.",
                font=("Segoe UI", 11),
                bg=LIGHT,
                fg="#536570",
            ).pack(anchor="w")

        self.make_button(
            main,
            "Start a Quiz",
            self.start_quiz,
        ).pack(anchor="w", pady=20)


if __name__ == "__main__":
    app = EnglishLearningApp()
    app.mainloop()
