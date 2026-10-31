"""GA2 - Linear and Binary search on customer account IDs"""

ids = [1005, 1023, 1002, 1100, 1050, 1017]


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    """arr must be sorted"""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    global ids
    while True:
        print("\n--- Customer ID Search ---")
        print("1.Enter IDs  2.Show IDs  3.Linear search  4.Binary search  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            ids = list(map(int, input("Enter IDs (space separated): ").split()))
        elif ch == "2":
            print("IDs:", ids)
        elif ch == "3":
            key = int(input("ID to search: "))
            pos = linear_search(ids, key)
            print("Found at index", pos if pos != -1 else "-> NOT found")
            print("Time: O(n)  Space: O(1)")
        elif ch == "4":
            key = int(input("ID to search: "))
            s = sorted(ids)
            print("Sorted list:", s)
            pos = binary_search(s, key)
            print("Found at index" if pos != -1 else "NOT found", pos if pos != -1 else "")
            print("Time: O(log n) (after sorting O(n log n))  Space: O(1)")
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
