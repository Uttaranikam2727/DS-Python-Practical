"""GB5 - Real-time event processing using a Queue (FIFO)"""


class EventQueue:
    def __init__(self):
        self.queue = []

    def add_event(self, event):
        self.queue.append(event)                 # enqueue at rear
        print("Event added:", event)

    def process_next(self):
        if not self.queue:
            print("No pending events")
            return
        event = self.queue.pop(0)                # dequeue from front
        print("Processed event:", event)

    def display(self):
        if not self.queue:
            print("No pending events")
        else:
            print("Pending events (front -> rear):")
            for i, e in enumerate(self.queue, 1):
                print(" ", i, e)

    def cancel(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print("Event cancelled:", event)
        else:
            print("Event not found (already processed or never added)")


def main():
    q = EventQueue()
    while True:
        print("\n--- Event Queue ---")
        print("1.Add event  2.Process next  3.Display pending  4.Cancel event  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            q.add_event(input("Event name: "))
        elif ch == "2":
            q.process_next()
        elif ch == "3":
            q.display()
        elif ch == "4":
            q.cancel(input("Event to cancel: "))
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
