import json
import os
import random
import logic
from text import LEVELS

SCORE_FILE = os.path.join(os.path.dirname(__file__), "high_scores.json")

test_seconds = 60
current_level = "Easy"
test_started = False
timer_id = None


def get_random_text():
    return random.choice(LEVELS[current_level])


def score_key(seconds):
    return f"{current_level}-{seconds}"


def load_high_scores():
    try:
        with open(SCORE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def best_score(seconds):
    return load_high_scores().get(score_key(seconds), 0)


def save_high_score(seconds, new_wpm):
    scores = load_high_scores()
    key = score_key(seconds)
    if new_wpm > scores.get(key, 0):
        scores[key] = new_wpm
        with open(SCORE_FILE, "w") as file:
            json.dump(scores, file, indent=4)
    return scores.get(key, 0)


def times_up(timer_label, text_box, wpm_label, my_label, high_score_label, result_box):
    timer_label.config(text="Time's up!")
    typed_text = text_box.get("1.0", "end")
    sample = my_label.cget("text")
    wpm = logic.calculate_wpm(typed_text, test_seconds)
    correct = logic.count_correct_words(typed_text, sample)
    wpm_label.config(text=f"WPM: {wpm} \n Correct words: {correct}")
    best = save_high_score(test_seconds, wpm)
    high_score_label.config(text=f"Best: {best} wpm")
    show_highlight(result_box, typed_text, sample)
    text_box.config(state="disabled")


def count_down(seconds, window, timer_label, text_box, wpm_label, my_label, high_score_label, result_box):
    global timer_id
    timer_label.config(text=f"Time: {seconds}")
    if seconds > 0:
        timer_id = window.after(1000, count_down, seconds - 1, window, timer_label,
                                text_box, wpm_label, my_label, high_score_label, result_box)
    else:
        times_up(timer_label, text_box, wpm_label, my_label, high_score_label, result_box)


def start_timer(event, window, timer_label, text_box, wpm_label, my_label, high_score_label, result_box):
    global test_started
    if not test_started:
        test_started = True
        count_down(test_seconds, window, timer_label, text_box, wpm_label, my_label, high_score_label, result_box)


def start_test(window, text_box, my_label, timer_label, wpm_label):
    global test_started, timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)
        timer_id = None
    test_started = False
    timer_label.config(text=f"Time: {test_seconds}")
    wpm_label.config(text="WPM: 0")
    text_box.config(state="normal")
    text_box.delete("1.0", "end")
    my_label.config(text=get_random_text())
    text_box.focus()


def choose_time(seconds, window, text_box, my_label, timer_label, wpm_label):
    global test_seconds
    test_seconds = seconds
    start_test(window, text_box, my_label, timer_label, wpm_label)


def choose_level(level, window, text_box, my_label, timer_label, wpm_label):
    global current_level
    current_level = level
    start_test(window, text_box, my_label, timer_label, wpm_label)


def show_highlight(result_box, typed_text, sample_text):
    result_box.config(state="normal")
    result_box.delete("1.0", "end")
    for word, is_right in logic.check_words(typed_text, sample_text):
        result_box.insert("end", word + " ", "right" if is_right else "wrong")
    result_box.config(state="disabled")