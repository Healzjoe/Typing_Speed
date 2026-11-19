
easy_quotes = [
    "Learning to code takes patience, but every small step you take today makes tomorrow a little bit easier for you.",
    "Success does not come from a single big moment, but from small efforts repeated every day until they become habits.",
    "A good programmer is not someone who never makes mistakes, but someone who learns quickly from every mistake they make.",
    "The best way to learn programming is to build projects, break them, and then figure out how to fix them.",
    "Practice makes progress, and progress builds confidence, so keep writing code every single day even when it feels very slow.",
    "Every expert you admire today was once a complete beginner who refused to give up when the problems became difficult.",
    "Your future is created by what you do today, so take a few minutes now to practice something brand new.",
    "When your code finally works after hours of searching for the problem, the feeling of success makes the effort worthwhile.",
    "Great things take time and patience, so do not be discouraged when progress feels slow, because you are moving forward.",
    "Discipline means choosing what you want most over what you want now, and it is the secret behind every achievement.",
    "Reading error messages carefully is one of the most useful habits a beginner can build, because they point to answers.",
    "Small steps taken every day add up over time, and soon you will have built something you are proud of.",
    "Do not compare your first chapter to someone else's tenth chapter, because everyone starts at the beginning of the story.",
    "A computer will only do exactly what you tell it to do, so clear thinking is the most important skill.",
    "Typing quickly and accurately takes practice, so be patient with yourself and focus on improving a little bit every day.",
]


hard_quotes = [
    "Programming languages are tools, and the real skill lies in understanding how to break complicated problems into smaller, manageable pieces.",
    "A developer who documents their work thoroughly saves colleagues hours of frustration, and often saves themselves months later.",
    "Debugging is a patient investigation: you gather evidence, form a hypothesis, test it, and then repeat until the mystery is solved.",
    "Good software is not written in a single burst of inspiration; it is refined through testing, feedback, and countless small improvements.",
    "Authentication confirms who a person is, while authorization determines what that person is allowed to do inside an application.",
    "Collaboration across different time zones requires clear communication, realistic deadlines, and a genuine respect for everyone's schedule.",
]

# VERY HARD: long paragraphs, uncommon words, numbers, and symbols
very_hard_quotes = [
    "In 2024, over 8.2 million developers worldwide used Python; its extensive libraries (e.g., NumPy, pandas, and Django) enable rapid prototyping, sophisticated data analysis, and scalable web architecture.",
    "Asynchronous programming allows applications to handle thousands of simultaneous requests without blocking; however, improper synchronization frequently introduces elusive, non-deterministic bugs that are exceptionally difficult to reproduce.",
    "Cryptographic hashing transforms arbitrary input into a fixed-length digest; consequently, even a single altered character produces a completely different output, which is why passwords should never be stored as plain text.",
    "Refactoring legacy codebases demands meticulous planning: developers must preserve existing functionality, write comprehensive regression tests, and incrementally replace deprecated components, all while delivering new features on schedule.",
]



# For the difficulty feature (Step 9) later
LEVELS = {
    "Easy": easy_quotes,
    "Hard": hard_quotes,
    "Very Hard": very_hard_quotes,
}