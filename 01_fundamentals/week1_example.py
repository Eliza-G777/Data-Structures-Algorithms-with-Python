"""
Week 1 worked example: School Library Manager

Reference example I studied to learn the Week 1 concepts (not my original work).
My own solutions are in the other files in this folder.

One program that uses every Week 1 concept. Each section is labelled with
the concept it demonstrates, so you can study them one at a time.

    CONCEPT 1  Variables and data types   (int, float, str, bool)
    CONCEPT 2  Conditionals               (if / elif / else)
    CONCEPT 3  Loops                      (for, while, break, continue)
    CONCEPT 4  Functions                  (parameters, return values)
    CONCEPT 5  Lists                      (ordered, changeable)
    CONCEPT 6  Tuples                     (ordered, unchangeable)
    CONCEPT 7  Dictionaries               (key -> value lookup)
    CONCEPT 8  Sets                       (unique items, fast membership)
    CONCEPT 9  Algorithms                 (step-by-step procedures: search, max, count)

How to run:
    python 01_fundamentals/week1_example.py          # runs checks, then a demo
    python 01_fundamentals/week1_example.py menu     # interactive menu
"""

import sys

# ---------------------------------------------------------------------------
# CONCEPT 1: Variables and data types
# ---------------------------------------------------------------------------
LIBRARY_NAME = "CodeCraft School Library"   # str
MAX_BORROW = 3                              # int: how many books one student may hold
LATE_FEE_PER_DAY = 0.50                     # float
is_open = True                              # bool

# ---------------------------------------------------------------------------
# CONCEPT 6: Tuples. Each book's identity (title, author) never changes,
# so a tuple fits. Tuples can also be dictionary keys; lists cannot.
# ---------------------------------------------------------------------------
# CONCEPT 7: Dictionaries. Look up a book by its ID in one step.
books = {
    101: {"info": ("Clean Code", "Robert Martin"), "genre": "programming", "available": True,  "times_borrowed": 4},
    102: {"info": ("Dune", "Frank Herbert"),       "genre": "fiction",     "available": True,  "times_borrowed": 7},
    103: {"info": ("Cosmos", "Carl Sagan"),        "genre": "science",     "available": False, "times_borrowed": 5},
    104: {"info": ("Python Crash Course", "Eric Matthes"), "genre": "programming", "available": True, "times_borrowed": 9},
    105: {"info": ("Things Fall Apart", "Chinua Achebe"),  "genre": "fiction",     "available": True, "times_borrowed": 6},
}

# CONCEPT 5: Lists. An ordered history; order matters and it keeps growing.
borrow_history = []          # list of (student, book_id) tuples

# CONCEPT 7 again: each student maps to the list of book IDs they hold.
borrowed_by = {"Hana": [103]}


# ---------------------------------------------------------------------------
# CONCEPT 4: Functions. Each one does one job and RETURNS a result
# instead of printing it, so other code (and tests) can use the value.
# ---------------------------------------------------------------------------

def get_title(book_id):
    """Return the title of a book, using tuple unpacking."""
    title, author = books[book_id]["info"]      # unpack the tuple
    return title


def describe_book(book_id):
    """Return a one-line description such as 'Dune by Frank Herbert [available]'."""
    title, author = books[book_id]["info"]
    # CONCEPT 2: conditional expression
    status = "available" if books[book_id]["available"] else "checked out"
    return f"{book_id}: {title} by {author} [{status}]"


def borrow_book(student, book_id):
    """
    Try to borrow a book. Returns (success: bool, message: str).
    Demonstrates CONCEPT 2: a chain of if/elif/else checks.
    """
    if not is_open:
        return False, "The library is closed."
    elif book_id not in books:                       # dict membership: O(1)
        return False, f"No book with ID {book_id}."
    elif not books[book_id]["available"]:
        return False, f"'{get_title(book_id)}' is already checked out."
    elif len(borrowed_by.get(student, [])) >= MAX_BORROW:
        return False, f"{student} already has {MAX_BORROW} books."
    else:
        books[book_id]["available"] = False
        books[book_id]["times_borrowed"] += 1
        borrowed_by.setdefault(student, []).append(book_id)   # list append
        borrow_history.append((student, book_id))             # tuple in a list
        return True, f"{student} borrowed '{get_title(book_id)}'."


def return_book(student, book_id, days_late=0):
    """Return a book and compute the late fee (int * float -> float)."""
    if book_id not in borrowed_by.get(student, []):
        return False, f"{student} does not have book {book_id}."
    borrowed_by[student].remove(book_id)
    books[book_id]["available"] = True
    fee = days_late * LATE_FEE_PER_DAY
    if fee > 0:
        return True, f"Returned. Late fee: ${fee:.2f}"
    return True, "Returned on time. Thank you!"


# ---------------------------------------------------------------------------
# CONCEPT 9: Simple algorithms written by hand (no built-in max/count).
# Each comment shows how many steps it takes for n books. This is the
# idea behind Big O, which you'll study in Week 2.
# ---------------------------------------------------------------------------

def search_by_title(keyword):
    """
    LINEAR SEARCH: check every book one by one.
    Steps: n (one check per book), so this is O(n).
    """
    keyword = keyword.lower()
    matches = []
    for book_id, data in books.items():            # CONCEPT 3: for loop over a dict
        title, author = data["info"]
        if keyword in title.lower():
            matches.append(book_id)
    return matches


def most_borrowed():
    """
    FIND MAXIMUM: remember the best seen so far, compare each item to it.
    Steps: n, so O(n). Returns None for an empty library.
    """
    best_id = None
    best_count = -1
    for book_id, data in books.items():
        if data["times_borrowed"] > best_count:
            best_count = data["times_borrowed"]
            best_id = book_id
    return best_id


def count_by_genre():
    """
    COUNTING with a dictionary: genre -> number of books.
    Steps: n, so O(n).
    """
    counts = {}
    for data in books.values():
        genre = data["genre"]
        counts[genre] = counts.get(genre, 0) + 1
    return counts


def all_genres():
    """CONCEPT 8: Sets remove duplicates automatically."""
    return {data["genre"] for data in books.values()}


def readers_in_common(group_a, group_b):
    """CONCEPT 8: Set operations. Students who appear in both groups."""
    return set(group_a) & set(group_b)


def available_books():
    """List comprehension: a short way to build a list with a loop."""
    return [book_id for book_id, data in books.items() if data["available"]]


# ---------------------------------------------------------------------------
# Self-checks: plain `assert` statements. If one is false, Python stops
# with an AssertionError. In Week 2 you'll move these into pytest.
# ---------------------------------------------------------------------------

def run_checks():
    assert get_title(102) == "Dune"
    assert search_by_title("python") == [104]
    assert search_by_title("zzz") == []
    assert most_borrowed() == 104
    assert count_by_genre() == {"programming": 2, "fiction": 2, "science": 1}
    assert all_genres() == {"programming", "fiction", "science"}
    assert readers_in_common(["Abel", "Hana"], ["Hana", "Liya"]) == {"Hana"}

    ok, _ = borrow_book("Hana", 103)                # already checked out
    assert ok is False
    ok, _ = borrow_book("Hana", 999)                # doesn't exist
    assert ok is False
    print("All checks passed ✔")


# ---------------------------------------------------------------------------
# Demo and menu: CONCEPT 3 (while loop, break, continue) and input handling
# ---------------------------------------------------------------------------

def demo():
    print(f"\n=== {LIBRARY_NAME} demo ===")
    for book_id in books:
        print("  " + describe_book(book_id))

    print()
    for book_id in [101, 102, 103, 104, 105]:       # 103 is taken; 105 hits the limit of 3
        ok, message = borrow_book("Abel", book_id)
        print(("  ✔ " if ok else "  ✘ ") + message)

    print("  " + return_book("Abel", 101, days_late=4)[1])
    print(f"\n  Most borrowed: {get_title(most_borrowed())}")
    print(f"  Books per genre: {count_by_genre()}")
    print(f"  Genres: {sorted(all_genres())}")
    print(f"  Borrow history: {borrow_history}")


def read_int(prompt):
    """Keep asking until the user types a whole number (a while loop with try/except)."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Please enter a number.")


def menu():
    student = input("Your name: ").strip().title() or "Guest"
    while True:
        print("\n1) List books  2) Search  3) Borrow  4) Return  5) Stats  0) Quit")
        choice = input("> ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            for book_id in books:
                print("  " + describe_book(book_id))
        elif choice == "2":
            ids = search_by_title(input("Title keyword: "))
            if not ids:
                print("  No matches.")
                continue                              # skip back to the top of the loop
            for book_id in ids:
                print("  " + describe_book(book_id))
        elif choice == "3":
            print("  " + borrow_book(student, read_int("Book ID: "))[1])
        elif choice == "4":
            book_id = read_int("Book ID: ")
            print("  " + return_book(student, book_id, read_int("Days late: "))[1])
        elif choice == "5":
            print(f"  Most borrowed: {get_title(most_borrowed())}")
            print(f"  Per genre: {count_by_genre()}")
        else:
            print("  Unknown option.")


if __name__ == "__main__":
    run_checks()
    if len(sys.argv) > 1 and sys.argv[1] == "menu":
        menu()
    else:
        demo()
