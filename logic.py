def calculate_wpm(typed_text, seconds=60):
    """Words per minute, counting real words."""
    words = len(typed_text.split())
    minutes = seconds / 60
    return round(words / minutes)

 
def calculate_wpm_by_characters(typed_text, seconds=60):
    """Words per minute, counting 5 characters as 1 word."""
    characters = len(typed_text.strip())
    minutes = seconds / 60
    return round((characters / 5) / minutes)


def count_correct_words(typed_text, sample_text):
    typed_words = typed_text.split()
    sample_words = sample_text.split()

    correct_words = 0

    for sample, typed in zip(sample_words, typed_words):
        if sample == typed:
            correct_words += 1

    return correct_words


def check_words(typed_text, sample_text):
    results = []
    for typed, sample in zip(typed_text.split(), sample_text.split()):
        results.append((typed, typed == sample))
    return results

