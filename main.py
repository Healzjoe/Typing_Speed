import tkinter as tk
from tkinter import ttk                                    # NEW: for the dropdown
import ui

# constants
ACTIVE, DIM, BAR = "#e2b714", "#646669", "#2d9d41"

# --- window ---
window = tk.Tk()
window.title("Typing_Speed_Test")
window.minsize(width=600, height=500)
window.config(padx=30, pady=30)

# widgets
label_one = tk.Label(text="My Typing Speed Test", font=("Arial", 20, "bold"))
label_one.pack(pady=30)

my_label = tk.Label(text=ui.get_random_text(), font=("Arial", 10), wraplength=500)
my_label.pack()

text_box = tk.Text(width=60, height=5)
text_box.pack(pady=10)

timer_label = tk.Label(text="Time: 60")
timer_label.pack()

wpm_label = tk.Label(text="WPM: 0")
wpm_label.pack()

high_score_label = tk.Label(text="Best: 0 wpm")
high_score_label.pack()



start_button = tk.Button(
    text="Start/Restart", bg="red", fg="white",
    command=lambda: ui.start_test(window, text_box, my_label, timer_label, wpm_label)
)
start_button.pack()

level_box = ttk.Combobox(window, values=list(ui.LEVELS), state="readonly", width=12)   # NEW
level_box.set(ui.current_level)
level_box.pack(pady=5)

# functions
def refresh_best():
    high_score_label.config(text=f"Best: {ui.best_score(ui.test_seconds)} wpm")


def select_time(seconds):
    for s, btn in time_buttons.items():
        btn.config(fg=ACTIVE if s == seconds else DIM)
    ui.choose_time(seconds, window, text_box, my_label, timer_label, wpm_label)
    refresh_best()


def select_level(event):
    ui.choose_level(level_box.get(), window, text_box, my_label, timer_label, wpm_label)
    refresh_best()


# time selector
time_buttons = {}
time_frame = tk.Frame(window, bg=BAR, padx=10, pady=4)
time_frame.pack(pady=10)

for seconds in (30, 60, 120):
    btn = tk.Button(
        time_frame, text=f"{seconds}s", font=("Consolas", 11, "bold"),
        bg=BAR, fg=ACTIVE if seconds == ui.test_seconds else DIM,
        activebackground=BAR, activeforeground="#d1d0c5",
        bd=0, highlightthickness=0, cursor="hand2",
        command=lambda s=seconds: select_time(s),
    )
    btn.pack(side="left", padx=8)
    time_buttons[seconds] = btn

#  connections
level_box.bind("<<ComboboxSelected>>", select_level)
text_box.bind("<KeyPress>", lambda event: ui.start_timer(
    event, window, timer_label, text_box, wpm_label, my_label, high_score_label))
refresh_best()


result_box = tk.Text(width = 60, height=4, state="disabled")
result_box.pack(pady=5)
result_box.tag_configure("right", foreground="green")
result_box.tag_configure("wrong", foreground="red")

text_box.bind("<KeyPress>", lambda event: ui.start_timer(
    event, window, timer_label, text_box, wpm_label, my_label, high_score_label, result_box))














window.mainloop()