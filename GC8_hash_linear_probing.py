"""GC8 - Hash table, fixed size, division method, linear probing"""

SIZE = 10
EMPTY = None
DELETED = "DELETED"      # tombstone so searches don't stop early


class HashTable:
    def __init__(self):
        self.table = [EMPTY] * SIZE

    def hash(self, key):
        return key % SIZE

    def insert(self, key):
        if self.search(key) != -1:          # check whole probe chain first
            print("Key already present")
            return
        idx = self.hash(key)
        for i in range(SIZE):
            pos = (idx + i) % SIZE
            if self.table[pos] is EMPTY or self.table[pos] == DELETED:
                self.table[pos] = key
                print("Inserted at index", pos)
                return
        print("Table is full")

    def search(self, key):
        idx = self.hash(key)
        for i in range(SIZE):
            pos = (idx + i) % SIZE
            if self.table[pos] is EMPTY:
                return -1
            if self.table[pos] == key:
                return pos
        return -1

    def delete(self, key):
        pos = self.search(key)
        if pos == -1:
            print("Key not found")
        else:
            self.table[pos] = DELETED
            print("Deleted key", key, "from index", pos)

    def display(self):
        for i, v in enumerate(self.table):
            print(i, "->", "empty" if v is EMPTY else v)


def main():
    ht = HashTable()
    while True:
        print("\n--- Hash Table (Linear Probing) ---")
        print("1.Insert  2.Search  3.Delete  4.Display  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            ht.insert(int(input("Key (integer): ")))
        elif ch == "2":
            p = ht.search(int(input("Key to search: ")))
            print("Found at index", p) if p != -1 else print("Key not found")
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
