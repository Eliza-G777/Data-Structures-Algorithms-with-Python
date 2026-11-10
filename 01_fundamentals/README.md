# 01 — Fundamentals

## Week 1: Python basics and Git

Write each program yourself. If a tutorial or course helped you, note it in `ATTRIBUTION.md`.

| Day | File | Status |
| --- | --- | --- |
| Ref | `week1_example.py` (worked example, study this first) | ✅ |
| Tue | `number_guessing.py` | ✅ |
| Wed | `calculator.py` | ⬜ |
| Thu | `min_max.py` | ⬜ |
| Thu | `student_records.py` | ⬜ |
| Fri | `beginner_problems.py` | ⬜ |

---

### 1. `number_guessing.py`
The program picks a random number from 1 to 100, and the user keeps guessing until they get it right.

**Must:**
- Say "too high" or "too low" after each guess.
- Count the guesses and show the total at the end.
- Handle input that isn't a number (like `abc`) without crashing.

**Hint:** `random.randint`, a `while` loop, `try`/`except ValueError`.
**Stretch:** let the user choose a difficulty that changes the range or limits the number of guesses.

---

### 2. `calculator.py`
A calculator built from functions.

**Must:**
- Have separate functions: `add`, `subtract`, `multiply`, `divide`.
- Make `divide` handle division by zero gracefully.
- Loop a menu until the user chooses to quit.

**Think about:** why separate functions are better than one big block of code.
**Stretch:** add `power` and `modulo`, and store a history of calculations in a list.

---

### 3. `min_max.py`
Find the largest and smallest number in a list **without** using `min()`, `max()`, or `sort()`.

**Must:**
- Write `find_min(numbers)` and `find_max(numbers)`.
- Handle an empty list (decide what it should return and explain why in a comment).
- Work with negative numbers.

**Think about:** how many times does your loop run for a list of n items? (This sets up Big O in Week 2.)

---

### 4. `student_records.py`
A simple student-record manager.

**Must:**
- Store each student as a dict, for example `{"id": 1, "name": "...", "grade": 11, "scores": [90, 85]}`.
- Add a student, list all students, find a student by ID, and calculate a student's average score.
- Use a menu loop.

**Think about:** should all the students be stored in a list or in a dict keyed by ID? Try one, then write a comment saying why you chose it. (This comes back in the Week 10 project.)

---

### 5. `beginner_problems.py`
Solve 5 problems, each as its own function with a short comment explaining your approach:
1. Reverse a string without slicing (`[::-1]`).
2. Count the vowels in a sentence.
3. Check whether a number is prime.
4. Sum the digits of an integer (e.g. 1234 → 10).
5. FizzBuzz from 1 to 50.

---

## Week 1 Git checklist
- [ ] First commit: README, `.gitignore`, folder structure
- [ ] One commit per finished program, with a clear message (e.g. `Add number guessing game with input validation`)
- [ ] Push to GitHub at least on Friday
- [ ] Fill in `journal/week-01.md`
