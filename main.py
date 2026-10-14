import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from datetime import datetime

APP_NAME = "English with Nazifa"
DATA_FILE = Path(__file__).with_name("progress.json")

GREEN = "#16866A"
GREEN_DARK = "#106B55"
DARK = "#172B3A"
LIGHT = "#F3F7F6"
WHITE = "#FFFFFF"
MUTED = "#536570"
BORDER = "#DCE7E3"
GOLD = "#E8B44F"
RED = "#B54747"

VOCABULARY = [
    {"word": "Achieve", "meaning": "به دست آوردن، موفق شدن", "example": "You can achieve your dreams.", "level": "Intermediate"},
    {"word": "Brave", "meaning": "شجاع", "example": "She is a brave young woman.", "level": "Beginner"},
    {"word": "Confident", "meaning": "بااعتمادبه‌نفس", "example": "Speak English with confidence.", "level": "Intermediate"},
    {"word": "Discover", "meaning": "کشف کردن", "example": "I want to discover new things.", "level": "Beginner"},
    {"word": "Education", "meaning": "آموزش، تعلیم و تربیه", "example": "Education can change our lives.", "level": "Beginner"},
    {"word": "Encourage", "meaning": "تشویق کردن", "example": "Teachers encourage their students.", "level": "Intermediate"},
    {"word": "Freedom", "meaning": "آزادی", "example": "Everyone deserves freedom.", "level": "Beginner"},
    {"word": "Grateful", "meaning": "سپاسگزار", "example": "I am grateful for your help.", "level": "Intermediate"},
    {"word": "Improve", "meaning": "بهبود بخشیدن، بهتر ساختن", "example": "Practice every day to improve your English.", "level": "Beginner"},
    {"word": "Knowledge", "meaning": "دانش، آگاهی", "example": "Knowledge gives us power.", "level": "Intermediate"},
    {"word": "Opportunity", "meaning": "فرصت", "example": "This course is a great opportunity.", "level": "Intermediate"},
    {"word": "Perseverance", "meaning": "پشتکار، استقامت", "example": "Perseverance helps us reach our goals.", "level": "Advanced"},
    {"word": "Respect", "meaning": "احترام", "example": "We should respect one another.", "level": "Beginner"},
    {"word": "Successful", "meaning": "موفق", "example": "Hard work helps you become successful.", "level": "Intermediate"},
    {"word": "Wisdom", "meaning": "خرد، دانایی", "example": "Wisdom comes from learning and experience.", "level": "Advanced"},
    {"word": "Curious", "meaning": "کنجکاو", "example": "Curious students ask good questions.", "level": "Intermediate"},
    {"word": "Reliable", "meaning": "قابل اعتماد", "example": "A reliable friend keeps promises.", "level": "Advanced"},
    {"word": "Goal", "meaning": "هدف", "example": "My goal is to speak English fluently.", "level": "Beginner"},
    {"word": "Patient", "meaning": "صبور", "example": "Be patient when you learn something new.", "level": "Beginner"},
    {"word": "Inspire", "meaning": "الهام بخشیدن", "example": "Her story can inspire other girls.", "level": "Intermediate"},
]

GRAMMAR_QUESTIONS = [
    {"question": "She _____ to school every day.", "options": ["go", "goes", "going", "gone"], "answer": "goes", "explanation": "در زمان حال ساده، برای he/she/it معمولاً به فعل s یا es اضافه می‌شود."},
    {"question": "They _____ playing football now.", "options": ["is", "am", "are", "be"], "answer": "are", "explanation": "برای فاعل جمع they از are استفاده می‌کنیم."},
    {"question": "I have lived here _____ 2020.", "options": ["for", "since", "at", "from"], "answer": "since", "explanation": "Since برای نقطهٔ شروع زمان به کار می‌رود."},
    {"question": "If I study, I _____ the test.", "options": ["pass", "passed", "will pass", "passing"], "answer": "will pass", "explanation": "در شرطی نوع اول، بخش نتیجه معمولاً با will می‌آید."},
    {"question": "This book is _____ than that one.", "options": ["interesting", "more interesting", "most interesting", "the interesting"], "answer": "more interesting", "explanation": "برای صفت‌های طولانی‌تر از more برای مقایسه استفاده می‌کنیم."},
    {"question": "We _____ dinner before they arrived.", "options": ["finish", "finished", "had finished", "have finish"], "answer": "had finished", "explanation": "Past perfect برای کاری که پیش از کار دیگری در گذشته تمام شده استفاده می‌شود."},
    {"question": "There isn't _____ milk in the fridge.", "options": ["many", "a few", "much", "several"], "answer": "much", "explanation": "Much با اسم‌های غیرقابل‌شمارش مانند milk استفاده می‌شود."},
    {"question": "The letter _____ yesterday.", "options": ["sent", "was sent", "is send", "sending"], "answer": "was sent", "explanation": "این جمله مجهول در گذشتهٔ ساده است: was/were + past participle."},
]

READING_TEXT = (
    "Learning a language takes time and regular practice. A student does not need to study "
    "for many hours every day. Twenty focused minutes can be useful when the student reads, "
    "reviews vocabulary, listens carefully, and tries to speak. Mistakes are a normal part of "
    "learning. The important thing is to notice mistakes, learn from them, and continue."
)
WRITING_PROMPTS = [
    "Write 5–7 sentences about your daily routine.",
    "Describe a person who inspires you. Explain why.",
    "Write a short paragraph about why education is important.",
    "Describe one goal you want to achieve this year.",
]
SPEAKING_PROMPTS = [
    "Introduce yourself for one minute.",
    "Talk about your favourite book, subject, or hobby.",
    "Describe a challenge you overcame.",
    "Explain your plans for the next five years.",
]
LISTENING_TIPS = [
    "Read a short English paragraph aloud, then listen to your own recording if possible.",
    "Use an English audio or video file already available on your device. Listen once for the main idea.",
    "Listen a second time and write down five words you recognize.",
    "Repeat one sentence aloud and try to copy its rhythm and pronunciation.",
]

def default_progress():
    return {
        "learned": [],
        "quizzes": 0,
        "correct": 0,
        "answered": 0,
        "quiz_history": [],
        "daily_goal": 10,
        "study_days": [],
        "writing_notes": "",
    }

def load_progress():
    data = default_progress()
    try:
        if DATA_FILE.exists():
            saved = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(saved, dict):
                for key in data:
                    if key in saved:
                        data[key] = saved[key]
    except (OSError, json.JSONDecodeError):
        pass
    # Repair older or malformed progress files without losing recognized data.
    if not isinstance(data.get("learned"), list):
        data["learned"] = []
    for key in ("quizzes", "correct", "answered", "daily_goal"):
        try:
            data[key] = int(data[key])
        except (ValueError, TypeError):
            data[key] = default_progress()[key]
    if not isinstance(data.get("quiz_history"), list):
        data["quiz_history"] = []
    if not isinstance(data.get("study_days"), list):
        data["study_days"] = []
    return data

class EnglishLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_NAME)
        self.geometry("1050x760")
        self.minsize(800, 620)
        self.configure(bg=LIGHT)
        self.progress = load_progress()
        self.vocab_index = 0
        self.search_results = list(range(len(VOCABULARY)))
        self.quiz_questions = []
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_answered = False
        self.quiz_kind = "Vocabulary"
        self.current_options = []
        self.setup_styles()
        self.show_home()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=8)
        style.configure("Green.TButton", font=("Segoe UI", 10, "bold"),
                        background=GREEN, foreground=WHITE, padding=9)
        style.map("Green.TButton", background=[("active", GREEN_DARK), ("disabled", "#AAB8B4")])
        style.configure("TEntry", padding=6, font=("Segoe UI", 11))
        style.configure("TCombobox", padding=5, font=("Segoe UI", 10))
        style.configure("Horizontal.TProgressbar", troughcolor="#E3ECE8",
                        background=GREEN, thickness=12)

    def save_progress(self):
        try:
            DATA_FILE.write_text(json.dumps(self.progress, ensure_ascii=False, indent=2), encoding="utf-8")
        except OSError as error:
            messagebox.showerror("Save Error", f"Could not save progress:\n{error}")

    def record_study_day(self):
        today = datetime.now().strftime("%Y-%m-%d")
        if today not in self.progress["study_days"]:
            self.progress["study_days"].append(today)
            self.save_progress()

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def make_header(self, subtitle):
        header = tk.Frame(self, bg=DARK, padx=24, pady=16)
        header.pack(fill="x")
        tk.Label(header, text=APP_NAME, font=("Segoe UI", 22, "bold"),
                 bg=DARK, fg=WHITE).pack(anchor="w")
        tk.Label(header, text=subtitle, font=("Segoe UI", 10),
                 bg=DARK, fg="#C8DAD5").pack(anchor="w", pady=(4, 0))

    def make_button(self, parent, text, command, style=True):
        return ttk.Button(parent, text=text, command=command,
                          style="Green.TButton" if style else "TButton")

    def make_card(self, parent, title, description, command, row, col):
        card = tk.Frame(parent, bg=WHITE, highlightbackground=BORDER, highlightthickness=1, padx=16, pady=14)
        tk.Label(card, text=title, font=("Segoe UI", 14, "bold"), bg=WHITE, fg=DARK).pack(anchor="w")
        tk.Label(card, text=description, font=("Segoe UI", 10), bg=WHITE, fg=MUTED,
                 wraplength=340, justify="left").pack(anchor="w", pady=8)
        self.make_button(card, "Open →", command).pack(anchor="w", pady=(3, 0))
        card.grid(row=row, column=col, sticky="nsew", padx=7, pady=7)
        return card

    def make_page(self, subtitle, title=None):
        self.clear_content()
        self.make_header(subtitle)
        main = tk.Frame(self, bg=LIGHT, padx=24, pady=20)
        main.pack(fill="both", expand=True)
        if title:
            tk.Label(main, text=title, font=("Segoe UI", 20, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w", pady=(0, 12))
        top = tk.Frame(main, bg=LIGHT)
        top.pack(fill="x", pady=(0, 12))
        self.make_button(top, "← Home", self.show_home, style=False).pack(side="left")
        return main

    def show_home(self):
        self.clear_content()
        self.make_header("Learn English. Build confidence. Reach your dreams.")
        main = tk.Frame(self, bg=LIGHT, padx=24, pady=20)
        main.pack(fill="both", expand=True)
        tk.Label(main, text="Welcome, English Learner!", font=("Segoe UI", 21, "bold"),
                 bg=LIGHT, fg=DARK).pack(anchor="w")
        tk.Label(main, text="Small steps every day lead to big achievements.",
                 font=("Segoe UI", 11), bg=LIGHT, fg=MUTED).pack(anchor="w", pady=(4, 14))

        learned = len(set(self.progress["learned"]))
        total = len(VOCABULARY)
        goal = max(1, self.progress["daily_goal"])
        goal_progress = min(100, round(learned / goal * 100))
        stats = tk.Frame(main, bg=LIGHT)
        stats.pack(fill="x", pady=(0, 8))
        for title, value in [
            ("Words learned", f"{learned}/{total}"),
            ("Quizzes completed", str(self.progress["quizzes"])),
            ("Answer accuracy", f"{round(self.progress['correct']/self.progress['answered']*100) if self.progress['answered'] else 0}%"),
            ("Daily word goal", f"{goal} words"),
        ]:
            tile = tk.Frame(stats, bg=WHITE, highlightbackground=BORDER, highlightthickness=1, padx=12, pady=10)
            tile.pack(side="left", fill="both", expand=True, padx=4)
            tk.Label(tile, text=value, font=("Segoe UI", 17, "bold"), bg=WHITE, fg=GREEN).pack(anchor="w")
            tk.Label(tile, text=title, font=("Segoe UI", 9), bg=WHITE, fg=MUTED).pack(anchor="w")
        tk.Label(main, text="Your vocabulary goal progress", font=("Segoe UI", 10, "bold"),
                 bg=LIGHT, fg=DARK).pack(anchor="w", pady=(5, 2))
        bar = ttk.Progressbar(main, maximum=100, value=goal_progress)
        bar.pack(fill="x", pady=(0, 8))
        tk.Label(main, text=f"{min(learned, goal)} of {goal} words toward your goal",
                 font=("Segoe UI", 9), bg=LIGHT, fg=MUTED).pack(anchor="w", pady=(0, 8))

        cards = tk.Frame(main, bg=LIGHT)
        cards.pack(fill="both", expand=True)
        cards.columnconfigure(0, weight=1)
        cards.columnconfigure(1, weight=1)
        self.make_card(cards, "📚 Vocabulary", "Browse, search, and learn words by level.", self.show_vocabulary, 0, 0)
        self.make_card(cards, "✍ Vocabulary Quiz", "Test your vocabulary with multiple-choice questions.", lambda: self.start_quiz("Vocabulary"), 0, 1)
        self.make_card(cards, "🧠 Grammar Practice", "Practice grammar rules and see explanations.", lambda: self.start_quiz("Grammar"), 1, 0)
        self.make_card(cards, "🌍 Four Skills", "Practice reading, writing, listening, and speaking.", self.show_skills, 1, 1)
        bottom = tk.Frame(main, bg=LIGHT)
        bottom.pack(fill="x", pady=(8, 0))
        self.make_button(bottom, "My Progress & History", self.show_progress, style=False).pack(side="left")
        self.make_button(bottom, "Settings / Daily Goal", self.show_settings, style=False).pack(side="left", padx=8)

    def show_vocabulary(self):
        main = self.make_page("Vocabulary Learning Center", "Vocabulary")
        toolbar = tk.Frame(main, bg=LIGHT)
        toolbar.pack(fill="x")
        tk.Label(toolbar, text="Search", font=("Segoe UI", 10, "bold"), bg=LIGHT, fg=DARK).pack(side="left", padx=(0, 6))
        self.search_entry = ttk.Entry(toolbar)
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=3)
        self.search_entry.bind("<Return>", lambda event: self.search_vocabulary())
        self.make_button(toolbar, "Search", self.search_vocabulary).pack(side="left", padx=6)
        tk.Label(toolbar, text="Level", bg=LIGHT, fg=DARK).pack(side="left", padx=(10, 4))
        self.level_filter = ttk.Combobox(toolbar, state="readonly", width=14,
                                         values=["All levels", "Beginner", "Intermediate", "Advanced"])
        self.level_filter.set("All levels")
        self.level_filter.pack(side="left")
        self.level_filter.bind("<<ComboboxSelected>>", lambda event: self.search_vocabulary())
        self.word_card = tk.Frame(main, bg=WHITE, padx=24, pady=20, highlightbackground=BORDER, highlightthickness=1)
        self.word_card.pack(fill="both", expand=True, pady=14)
        self.word_label = tk.Label(self.word_card, text="", font=("Segoe UI", 28, "bold"), bg=WHITE, fg=GREEN)
        self.word_label.pack(pady=(10, 3))
        self.level_label = tk.Label(self.word_card, text="", font=("Segoe UI", 10, "italic"), bg=WHITE, fg=MUTED)
        self.level_label.pack()
        self.meaning_label = tk.Label(self.word_card, text="", font=("Segoe UI", 16), bg=WHITE, fg=DARK,
                                      wraplength=800, justify="center")
        self.meaning_label.pack(pady=12)
        self.example_label = tk.Label(self.word_card, text="", font=("Segoe UI", 12, "italic"), bg=WHITE, fg=MUTED,
                                      wraplength=800, justify="center")
        self.example_label.pack(pady=8)
        self.counter_label = tk.Label(self.word_card, text="", font=("Segoe UI", 10, "bold"), bg=WHITE, fg=GREEN)
        self.counter_label.pack(pady=8)
        controls = tk.Frame(main, bg=LIGHT)
        controls.pack(fill="x")
        self.make_button(controls, "← Previous", self.previous_word, style=False).pack(side="left")
        self.make_button(controls, "Mark as Learned ✓", self.mark_learned).pack(side="left", padx=8)
        self.make_button(controls, "Next Word →", self.next_word).pack(side="right")
        self.search_results = list(range(len(VOCABULARY)))
        self.vocab_index = 0
        self.display_word()

    def search_vocabulary(self):
        query = self.search_entry.get().strip().lower()
        level = self.level_filter.get()
        results = []
        for i, item in enumerate(VOCABULARY):
            matches_query = not query or query in item["word"].lower() or query in item["meaning"].lower()
            matches_level = level == "All levels" or item["level"] == level
            if matches_query and matches_level:
                results.append(i)
        if not results:
            messagebox.showinfo("Search", "No matching words were found. Try another word or level.")
            return
        self.search_results = results
        self.vocab_index = 0
        self.display_word()

    def display_word(self):
        if not self.search_results:
            return
        item = VOCABULARY[self.search_results[self.vocab_index]]
        self.word_label.config(text=item["word"])
        self.level_label.config(text=f"Level: {item['level']}")
        self.meaning_label.config(text=item["meaning"])
        self.example_label.config(text=f"Example: {item['example']}")
        learned = item["word"] in self.progress["learned"]
        self.counter_label.config(text=f"Word {self.vocab_index + 1} of {len(self.search_results)}"
                                        + ("  •  ✓ Learned" if learned else ""))

    def next_word(self):
        if self.search_results:
            self.vocab_index = (self.vocab_index + 1) % len(self.search_results)
            self.display_word()

    def previous_word(self):
        if self.search_results:
            self.vocab_index = (self.vocab_index - 1) % len(self.search_results)
            self.display_word()

    def mark_learned(self):
        if not self.search_results:
            return
        item = VOCABULARY[self.search_results[self.vocab_index]]
        if item["word"] not in self.progress["learned"]:
            self.progress["learned"].append(item["word"])
            self.record_study_day()
            self.save_progress()
            messagebox.showinfo("Well Done!", f"{item['word']} was added to your learned words.")
        else:
            messagebox.showinfo("Vocabulary", f"You already marked {item['word']} as learned.")
        self.display_word()

    def start_quiz(self, kind="Vocabulary"):
        self.quiz_kind = kind
        source = VOCABULARY if kind == "Vocabulary" else GRAMMAR_QUESTIONS
        self.quiz_questions = random.sample(source, min(10, len(source)))
        self.quiz_index = 0
        self.quiz_score = 0
        self.quiz_answered = False
        self.clear_content()
        self.make_header(f"{kind} Challenge")
        self.quiz_area = tk.Frame(self, bg=LIGHT, padx=28, pady=22)
        self.quiz_area.pack(fill="both", expand=True)
        top = tk.Frame(self.quiz_area, bg=LIGHT)
        top.pack(fill="x")
        self.make_button(top, "← Home", self.show_home, style=False).pack(side="left")
        self.quiz_progress_label = tk.Label(top, text="", font=("Segoe UI", 10, "bold"), bg=LIGHT, fg=GREEN)
        self.quiz_progress_label.pack(side="right")
        self.question_label = tk.Label(self.quiz_area, text="", font=("Segoe UI", 17, "bold"),
                                       bg=LIGHT, fg=DARK, wraplength=850, justify="left")
        self.question_label.pack(anchor="w", pady=(32, 18))
        self.options_frame = tk.Frame(self.quiz_area, bg=LIGHT)
        self.options_frame.pack(fill="x")
        self.feedback_label = tk.Label(self.quiz_area, text="", font=("Segoe UI", 11, "bold"),
                                       bg=LIGHT, fg=DARK, wraplength=850, justify="left")
        self.feedback_label.pack(anchor="w", pady=15)
        self.explanation_label = tk.Label(self.quiz_area, text="", font=("Segoe UI", 10),
                                          bg=LIGHT, fg=MUTED, wraplength=850, justify="left")
        self.explanation_label.pack(anchor="w")
        self.next_button = self.make_button(self.quiz_area, "Next Question →", self.next_question)
        self.next_button.pack(anchor="e", pady=18)
        self.next_button.config(state="disabled")
        self.show_question()

    def show_question(self):
        if self.quiz_index >= len(self.quiz_questions):
            self.finish_quiz()
            return
        self.quiz_answered = False
        self.next_button.config(state="disabled")
        self.feedback_label.config(text="")
        self.explanation_label.config(text="")
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        item = self.quiz_questions[self.quiz_index]
        self.quiz_progress_label.config(text=f"Question {self.quiz_index + 1} / {len(self.quiz_questions)}")
        if self.quiz_kind == "Vocabulary":
            self.question_label.config(text=f"What is the meaning of “{item['word']}”?")
            wrong = random.sample([v for v in VOCABULARY if v["word"] != item["word"]], min(3, len(VOCABULARY)-1))
            options = [item["meaning"]] + [v["meaning"] for v in wrong]
            random.shuffle(options)
            self.current_options = options
            answer = item["meaning"]
        else:
            self.question_label.config(text=item["question"])
            options = item["options"][:]
            random.shuffle(options)
            self.current_options = options
            answer = item["answer"]
        for option in options:
            self.make_button(self.options_frame, option,
                             lambda selected=option: self.check_answer(selected), style=False).pack(fill="x", pady=4)
        self.current_answer = answer
        self.current_explanation = item.get("explanation", "")

    def check_answer(self, selected):
        if self.quiz_answered:
            return
        self.quiz_answered = True
        self.progress["answered"] += 1
        if selected == self.current_answer:
            self.quiz_score += 1
            self.progress["correct"] += 1
            self.feedback_label.config(text="Correct! Excellent work. ✓", fg=GREEN)
        else:
            self.feedback_label.config(text=f"Not quite. Correct answer: {self.current_answer}", fg=RED)
        self.explanation_label.config(text=self.current_explanation)
        self.record_study_day()
        self.save_progress()
        self.next_button.config(state="normal")

    def next_question(self):
        if self.quiz_answered:
            self.quiz_index += 1
            self.show_question()

    def finish_quiz(self):
        self.clear_content()
        self.make_header("Quiz Results")
        result = tk.Frame(self, bg=LIGHT, padx=30, pady=28)
        result.pack(fill="both", expand=True)
        total = len(self.quiz_questions)
        percentage = round(self.quiz_score / total * 100) if total else 0
        self.progress["quizzes"] += 1
        self.progress["quiz_history"].append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": self.quiz_kind,
            "score": self.quiz_score,
            "total": total,
            "percentage": percentage,
        })
        self.progress["quiz_history"] = self.progress["quiz_history"][-50:]
        self.save_progress()
        tk.Label(result, text=f"{self.quiz_kind} Quiz Completed!", font=("Segoe UI", 23, "bold"),
                 bg=LIGHT, fg=GREEN).pack(pady=10)
        tk.Label(result, text=f"{self.quiz_score} / {total}", font=("Segoe UI", 34, "bold"),
                 bg=LIGHT, fg=DARK).pack(pady=5)
        tk.Label(result, text=f"Your score: {percentage}%", font=("Segoe UI", 15),
                 bg=LIGHT, fg=DARK).pack(pady=5)
        tk.Label(result, text=("Amazing! Keep up the great work!" if percentage >= 80 else
                               "Good effort! Review the explanations and try again." if percentage >= 50 else
                               "Keep learning. Every attempt helps!"),
                 font=("Segoe UI", 11), bg=LIGHT, fg=MUTED).pack(pady=10)
        self.make_button(result, "Try Again", lambda: self.start_quiz(self.quiz_kind)).pack(pady=5)
        self.make_button(result, "Back to Home", self.show_home, style=False).pack(pady=5)

    def show_skills(self):
        main = self.make_page("English Skills Studio", "Practice the Four Skills")
        tk.Label(main, text="Choose a skill. These activities work offline; listening audio is supplied by you.",
                 font=("Segoe UI", 10), bg=LIGHT, fg=MUTED).pack(anchor="w", pady=(0, 12))
        grid = tk.Frame(main, bg=LIGHT)
        grid.pack(fill="both", expand=True)
        grid.columnconfigure(0, weight=1)
        grid.columnconfigure(1, weight=1)
        self.make_card(grid, "📖 Reading", "Read a short passage and answer comprehension questions.", self.show_reading, 0, 0)
        self.make_card(grid, "✍ Writing", "Choose a prompt, write a paragraph, and save your draft locally.", self.show_writing, 0, 1)
        self.make_card(grid, "🎧 Listening", "Follow a listening routine using audio files or recordings on your computer.", self.show_listening, 1, 0)
        self.make_card(grid, "🗣 Speaking", "Practice speaking prompts and use a simple self-checklist.", self.show_speaking, 1, 1)

    def show_reading(self):
        main = self.make_page("Reading Practice", "Read and Understand")
        box = tk.Frame(main, bg=WHITE, padx=18, pady=16, highlightbackground=BORDER, highlightthickness=1)
        box.pack(fill="x", pady=8)
        tk.Label(box, text=READING_TEXT, font=("Segoe UI", 12), bg=WHITE, fg=DARK,
                 wraplength=900, justify="left").pack(anchor="w")
        questions = [
            ("What does regular language practice require?", ["Only long study sessions", "Time and regular practice", "No mistakes", "Only grammar"], 1),
            ("According to the passage, mistakes are…", ["a normal part of learning", "a reason to stop", "always bad", "not useful"], 0),
            ("What should students do with mistakes?", ["Ignore them", "Stop studying", "Learn from them", "Avoid speaking"], 2),
        ]
        self.reading_vars = []
        area = tk.Frame(main, bg=LIGHT)
        area.pack(fill="both", expand=True, pady=8)
        for i, (q, opts, correct) in enumerate(questions):
            tk.Label(area, text=f"{i+1}. {q}", font=("Segoe UI", 10, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w", pady=(8, 3))
            var = tk.IntVar(value=-1)
            self.reading_vars.append((var, correct))
            for j, opt in enumerate(opts):
                ttk.Radiobutton(area, text=opt, variable=var, value=j).pack(anchor="w", padx=12)
        self.make_button(main, "Check Reading Answers", self.check_reading).pack(anchor="w", pady=8)

    def check_reading(self):
        if not hasattr(self, "reading_vars"):
            return
        if any(var.get() < 0 for var, _ in self.reading_vars):
            messagebox.showinfo("Reading", "Please answer all three questions first.")
            return
        score = sum(var.get() == correct for var, correct in self.reading_vars)
        self.record_study_day()
        messagebox.showinfo("Reading Result", f"You scored {score}/3.")

    def show_writing(self):
        main = self.make_page("Writing Practice", "Write and Save")
        tk.Label(main, text="Choose a writing prompt:", font=("Segoe UI", 10, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w")
        self.writing_prompt = ttk.Combobox(main, state="readonly", values=WRITING_PROMPTS)
        self.writing_prompt.current(0)
        self.writing_prompt.pack(fill="x", pady=(5, 10))
        tk.Label(main, text="Your paragraph:", font=("Segoe UI", 10, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w")
        self.writing_text = tk.Text(main, height=12, font=("Segoe UI", 11), wrap="word", padx=10, pady=8)
        self.writing_text.pack(fill="both", expand=True, pady=6)
        self.writing_text.insert("1.0", self.progress.get("writing_notes", ""))
        bottom = tk.Frame(main, bg=LIGHT)
        bottom.pack(fill="x")
        self.word_count_label = tk.Label(bottom, text="Words: 0", bg=LIGHT, fg=MUTED)
        self.word_count_label.pack(side="left")
        self.writing_text.bind("<KeyRelease>", self.update_word_count)
        self.make_button(bottom, "Save Draft", self.save_writing).pack(side="right")
        self.update_word_count()

    def update_word_count(self, event=None):
        if hasattr(self, "writing_text") and self.writing_text.winfo_exists():
            text = self.writing_text.get("1.0", "end-1c").strip()
            count = len(text.split()) if text else 0
            self.word_count_label.config(text=f"Words: {count}")

    def save_writing(self):
        self.progress["writing_notes"] = self.writing_text.get("1.0", "end-1c")
        self.record_study_day()
        self.save_progress()
        messagebox.showinfo("Writing", "Your draft has been saved on this computer.")

    def show_listening(self):
        main = self.make_page("Listening Practice", "Build Listening Skills")
        tk.Label(main, text="This section does not download or play audio automatically. Use an audio/video file you already have.",
                 font=("Segoe UI", 10), bg=LIGHT, fg=MUTED, wraplength=900, justify="left").pack(anchor="w", pady=(0, 12))
        for i, tip in enumerate(LISTENING_TIPS, 1):
            card = tk.Frame(main, bg=WHITE, padx=14, pady=12, highlightbackground=BORDER, highlightthickness=1)
            card.pack(fill="x", pady=5)
            tk.Label(card, text=f"Step {i}", font=("Segoe UI", 10, "bold"), bg=WHITE, fg=GREEN).pack(anchor="w")
            tk.Label(card, text=tip, font=("Segoe UI", 10), bg=WHITE, fg=DARK,
                     wraplength=900, justify="left").pack(anchor="w", pady=(4, 0))
        self.make_button(main, "Mark Listening Practice Complete", self.complete_skill).pack(anchor="w", pady=12)

    def show_speaking(self):
        main = self.make_page("Speaking Practice", "Speak with Confidence")
        tk.Label(main, text="Choose one prompt. Speak for 1–2 minutes, then check each item.",
                 font=("Segoe UI", 10), bg=LIGHT, fg=MUTED).pack(anchor="w", pady=(0, 8))
        prompt = random.choice(SPEAKING_PROMPTS)
        prompt_label = tk.Label(main, text=prompt, font=("Segoe UI", 15, "bold"), bg=WHITE, fg=GREEN,
                                padx=18, pady=18, wraplength=850, justify="left")
        prompt_label.pack(fill="x", pady=8)
        self.make_button(main, "New Speaking Prompt", lambda: prompt_label.config(text=random.choice(SPEAKING_PROMPTS)), style=False).pack(anchor="w", pady=5)
        tk.Label(main, text="Self-checklist", font=("Segoe UI", 12, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w", pady=(12, 5))
        checks = ["I spoke in complete sentences.", "I tried to speak clearly.", "I used at least three new words.", "I corrected one mistake."]
        self.speaking_checks = []
        for item in checks:
            var = tk.BooleanVar(value=False)
            self.speaking_checks.append(var)
            ttk.Checkbutton(main, text=item, variable=var).pack(anchor="w", pady=3)
        self.make_button(main, "Finish Speaking Practice", self.complete_skill).pack(anchor="w", pady=12)

    def complete_skill(self):
        self.record_study_day()
        messagebox.showinfo("Practice", "Great work! Your practice day has been recorded.")

    def show_progress(self):
        main = self.make_page("Your Learning Progress", "Progress & Quiz History")
        learned = len(set(self.progress["learned"]))
        answered = self.progress["answered"]
        correct = self.progress["correct"]
        accuracy = round(correct / answered * 100) if answered else 0
        stats = tk.Frame(main, bg=LIGHT)
        stats.pack(fill="x")
        for title, value in [
            ("Words learned", str(learned)),
            ("Quizzes completed", str(self.progress["quizzes"])),
            ("Questions answered", str(answered)),
            ("Accuracy", f"{accuracy}%"),
            ("Study dates", str(len(set(self.progress["study_days"])))),
        ]:
            tile = tk.Frame(stats, bg=WHITE, padx=12, pady=10, highlightbackground=BORDER, highlightthickness=1)
            tile.pack(side="left", fill="both", expand=True, padx=3)
            tk.Label(tile, text=value, font=("Segoe UI", 16, "bold"), bg=WHITE, fg=GREEN).pack(anchor="w")
            tk.Label(tile, text=title, font=("Segoe UI", 9), bg=WHITE, fg=MUTED).pack(anchor="w")
        tk.Label(main, text="Learned words", font=("Segoe UI", 12, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w", pady=(18, 5))
        learned_words = sorted(set(self.progress["learned"]))
        tk.Label(main, text=", ".join(learned_words) if learned_words else "No words marked yet.",
                 font=("Segoe UI", 10), bg=LIGHT, fg=MUTED, wraplength=900, justify="left").pack(anchor="w")
        tk.Label(main, text="Recent quiz results", font=("Segoe UI", 12, "bold"), bg=LIGHT, fg=DARK).pack(anchor="w", pady=(18, 5))
        history_frame = tk.Frame(main, bg=WHITE, highlightbackground=BORDER, highlightthickness=1)
        history_frame.pack(fill="both", expand=True)
        columns = ("date", "type", "score", "percent")
        tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=7)
        for col, title, width in [
            ("date", "Date", 180), ("type", "Quiz Type", 150), ("score", "Score", 100), ("percent", "Percent", 100)
        ]:
            tree.heading(col, text=title)
            tree.column(col, width=width, anchor="center")
        tree.pack(fill="both", expand=True, padx=5, pady=5)
        for entry in reversed(self.progress["quiz_history"][-20:]):
            tree.insert("", "end", values=(entry.get("date", ""), entry.get("type", ""),
                                           f"{entry.get('score', 0)}/{entry.get('total', 0)}",
                                           f"{entry.get('percentage', 0)}%"))
        self.make_button(main, "Start Vocabulary Quiz", lambda: self.start_quiz("Vocabulary")).pack(anchor="w", pady=10)

    def show_settings(self):
        main = self.make_page("App Settings", "Learning Goals")
        tk.Label(main, text="Set your target number of words to learn. Your existing progress will be kept.",
                 font=("Segoe UI", 10), bg=LIGHT, fg=MUTED, wraplength=850, justify="left").pack(anchor="w", pady=(0, 15))
        row = tk.Frame(main, bg=LIGHT)
        row.pack(anchor="w")
        tk.Label(row, text="Daily word goal:", font=("Segoe UI", 11, "bold"), bg=LIGHT, fg=DARK).pack(side="left", padx=(0, 10))
        self.goal_var = tk.StringVar(value=str(self.progress["daily_goal"]))
        goal_entry = ttk.Entry(row, textvariable=self.goal_var, width=8)
        goal_entry.pack(side="left")
        self.make_button(main, "Save Goal", self.save_goal).pack(anchor="w", pady=12)
        tk.Label(main, text="Data is stored locally in progress.json beside main.py. Keep a backup of this file if you want to protect your learning history.",
                 font=("Segoe UI", 10), bg=WHITE, fg=MUTED, padx=14, pady=14,
                 wraplength=850, justify="left").pack(fill="x", pady=12)

    def save_goal(self):
        try:
            goal = int(self.goal_var.get())
            if not 1 <= goal <= len(VOCABULARY):
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Goal", f"Enter a whole number from 1 to {len(VOCABULARY)}.")
            return
        self.progress["daily_goal"] = goal
        self.save_progress()
        messagebox.showinfo("Goal Saved", "Your learning goal has been saved.")
        self.show_home()

if __name__ == "__main__":
    app = EnglishLearningApp()
    app.mainloop()
