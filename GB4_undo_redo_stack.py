"""GB4 - Undo/Redo for a text editor using two stacks"""


class Editor:
    def __init__(self):
        self.undo_stack = []   # applied changes
        self.redo_stack = []   # undone changes

    def make_change(self, text):
        self.undo_stack.append(text)
        self.redo_stack.clear()          # new change invalidates redo history
        print("Change made:", text)

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        change = self.undo_stack.pop()
        self.redo_stack.append(change)
        print("Undone:", change)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        change = self.redo_stack.pop()
        self.undo_stack.append(change)
        print("Redone:", change)

    def display(self):
        doc = " ".join(self.undo_stack)
        print("Document state:", repr(doc))
        print("Undo stack:", self.undo_stack)
        print("Redo stack:", self.redo_stack)


def main():
    ed = Editor()
    while True:
        print("\n--- Undo/Redo Editor ---")
        print("1.Make change  2.Undo  3.Redo  4.Display  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            ed.make_change(input("Enter text: "))
        elif ch == "2":
            ed.undo()
        elif ch == "3":
            ed.redo()
        elif ch == "4":
            ed.display()
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
