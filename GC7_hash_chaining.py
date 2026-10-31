"""GC7 - Hash table, size 10, division method, collision handling by chaining"""

SIZE = 10


class HashTable:
    def __init__(self):
        self.table = [[] for _ in range(SIZE)]   # each slot is a list (chain)

    def hash(self, key):
        return key % SIZE                          # division method

    def insert(self, key, value):
        idx = self.hash(key)
        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value                    # update existing key
                print("Key existed, value updated")
                return
        self.table[idx].append([key, value])
        print("Inserted at index", idx)

    def search(self, key):
        for k, v in self.table[self.hash(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        chain = self.table[self.hash(key)]
        for pair in chain:
            if pair[0] == key:
                chain.remove(pair)
                print("Deleted key", key)
                return
        print("Key not found")

    def display(self):
        for i in range(SIZE):
            print(i, "->", " -> ".join("(%s:%s)" % (k, v) for k, v in self.table[i]) or "empty")


def main():
    ht = HashTable()
    while True:
        print("\n--- Hash Table (Chaining) ---")
        print("1.Insert  2.Search  3.Delete  4.Display  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            ht.insert(int(input("Key (integer): ")), input("Value: "))
        elif ch == "2":
            v = ht.search(int(input("Key to search: ")))
            print("Value:", v) if v is not None else print("Key not found")
        elif ch == "3":
            ht.delete(int(input("Key to delete: ")))
        elif ch == "4":
            ht.display()
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
