"""GA1 - Library borrowing records
member_counts : books borrowed by each member (list)
book_counts   : times each book was borrowed (dict)
"""

member_counts = [3, 0, 5, 2, 0, 3, 7, 3, 1, 0]
book_counts = {"Python Basics": 12, "Data Structures": 25, "Algorithms": 18,
               "DBMS": 4, "Networks": 9}


def average_borrowed(counts):
    total = 0
    for c in counts:
        total += c
    return total / len(counts)


def highest_lowest(books):
    items = list(books.items())
    hi = lo = items[0]
    for b in items:
        if b[1] > hi[1]:
            hi = b
        if b[1] < lo[1]:
            lo = b
    return hi, lo


def count_zero(counts):
    n = 0
    for c in counts:
        if c == 0:
            n += 1
    return n


def mode_of_counts(counts):
    freq = {}
    for c in counts:
        freq[c] = freq.get(c, 0) + 1
    mode = max(freq, key=freq.get)
    return mode, freq[mode]


def op_average():
    print("Average books borrowed per member:", round(average_borrowed(member_counts), 2))
    print("Time: O(n)  Space: O(1)")


def op_hi_lo():
    hi, lo = highest_lowest(book_counts)
    print("Highest borrowed book:", hi[0], "->", hi[1])
    print("Lowest borrowed book :", lo[0], "->", lo[1])
    print("Time: O(n)  Space: O(1)")


def op_zero():
    print("Members with 0 borrowings:", count_zero(member_counts))
    print("Time: O(n)  Space: O(1)")


def op_mode():
    mode, times = mode_of_counts(member_counts)
    print("Mode of borrow counts:", mode, "(occurs", times, "times)")
    hi, _ = highest_lowest(book_counts)
    print("Most frequently borrowed book:", hi[0], "(", hi[1], "borrows )")
    print("Time: O(n)  Space: O(k), k = distinct counts (O(n) worst case)")


def enter_data():
    global member_counts, book_counts
    member_counts = list(map(int, input("Member borrow counts (space separated): ").split()))
    n = int(input("Number of books: "))
    book_counts = {}
    for _ in range(n):
        name = input("  Book name: ")
        book_counts[name] = int(input("  Times borrowed: "))


def main():
    while True:
        print("\n--- Library Borrowing ---")
        print("1.Average  2.Highest/Lowest book  3.Zero-borrow members  4.Mode")
        print("5.Run all  6.Enter my own data    0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1": op_average()
        elif ch == "2": op_hi_lo()
        elif ch == "3": op_zero()
        elif ch == "4": op_mode()
        elif ch == "5":
            op_average(); op_hi_lo(); op_zero(); op_mode()
        elif ch == "6": enter_data()
        elif ch == "0": break
        else: print("Invalid choice")


if __name__ == "__main__":
    main()
