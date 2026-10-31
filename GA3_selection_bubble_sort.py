"""GA3 - Sort employee salaries (Selection sort & Bubble sort), show top 5"""

salaries = [45000.5, 32000.0, 78000.75, 56000.0, 91000.25, 28000.0, 67000.5, 83000.0]


def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def top5(sorted_asc):
    return sorted_asc[::-1][:5]


def main():
    global salaries
    while True:
        print("\n--- Salary Sorting ---")
        print("1.Enter salaries  2.Selection sort  3.Bubble sort  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            salaries = list(map(float, input("Enter salaries (space separated): ").split()))
        elif ch == "2":
            r = selection_sort(salaries)
            print("Ascending:", r)
            print("Top 5 highest:", top5(r))
            print("Time: O(n^2) all cases  Space: O(1)")
        elif ch == "3":
            r = bubble_sort(salaries)
            print("Ascending:", r)
            print("Top 5 highest:", top5(r))
            print("Time: O(n^2) worst/avg, O(n) best  Space: O(1)")
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
