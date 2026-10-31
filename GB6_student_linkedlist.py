"""GB6 - Student Record Management using a Singly Linked List"""


class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        if self.search(roll):
            print("Roll number already exists")
            return
        new = Node(roll, name, marks)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        print("Student added")

    def delete(self, roll):
        cur, prev = self.head, None
        while cur and cur.roll != roll:
            prev, cur = cur, cur.next
        if cur is None:
            print("Student not found")
            return
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next
        print("Student deleted")

    def update(self, roll, name, marks):
        node = self.search(roll)
        if node is None:
            print("Student not found")
            return
        node.name, node.marks = name, marks
        print("Student updated")

    def search(self, roll):
        cur = self.head
        while cur:
            if cur.roll == roll:
                return cur
            cur = cur.next
        return None

    def sort(self, by="marks", descending=False):
        """Bubble sort on the nodes' data"""
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            cur = self.head
            while cur.next:
                a = getattr(cur, by)
                b = getattr(cur.next, by)
                if (a < b) if descending else (a > b):
                    cur.roll, cur.next.roll = cur.next.roll, cur.roll
                    cur.name, cur.next.name = cur.next.name, cur.name
                    cur.marks, cur.next.marks = cur.next.marks, cur.marks
                    swapped = True
                cur = cur.next

    def display(self):
        if self.head is None:
            print("No records")
            return
        print("%-8s %-15s %s" % ("Roll", "Name", "Marks"))
        cur = self.head
        while cur:
            print("%-8s %-15s %s" % (cur.roll, cur.name, cur.marks))
            cur = cur.next


def main():
    sl = StudentList()
    while True:
        print("\n--- Student Records (Linked List) ---")
        print("1.Add 2.Delete 3.Update 4.Search 5.Sort & display 6.Display 0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            sl.add(int(input("Roll: ")), input("Name: "), float(input("Marks: ")))
        elif ch == "2":
            sl.delete(int(input("Roll to delete: ")))
        elif ch == "3":
            sl.update(int(input("Roll to update: ")), input("New name: "), float(input("New marks: ")))
        elif ch == "4":
            n = sl.search(int(input("Roll to search: ")))
            print("Found:", n.roll, n.name, n.marks) if n else print("Not found")
        elif ch == "5":
            by = "marks" if input("Sort by (1) marks (2) roll: ").strip() == "1" else "roll"
            desc = input("Order (1) ascending (2) descending: ").strip() == "2"
            sl.sort(by, desc)
            sl.display()
        elif ch == "6":
            sl.display()
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
