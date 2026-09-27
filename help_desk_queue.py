# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        while current is not None:
            print(f"- {current.value}")
            current = current.next

def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"{name} added to the queue.")
            
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = queue.dequeue()
            if name is not None:
                print(f"{name} was helped.")
            else:
                print("No customers to help.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            name = queue.peek()
            if name is not None:
                print(f"Next customer: {name}")
            else:
                print("No customers waiting.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


#A stack is the right choice for an undo/redo system because it follows
#  the Last-In, First-Out (LIFO) principle. The most recent action a 
# user performs is the first action that should be undone. When an 
# action is undone, it can be moved from the undo stack to the redo 
# stack. If the user chooses redo, the most recently undone action is 
# moved back to the undo stack. This makes two stacks a natural way to 
# manage the history of user actions.
#A queue is better suited for a help desk because it follows the 
# First-In, First-Out (FIFO) principle. Customers should be helped in 
#  same order that they entered the system. The first customer added to
#  the queue is therefore the first customer removed and helped. Using 
# separate front and rear pointers allows customers to be added to the
#  rear while being removed from the front.
#My implementations differ from Python’s built-in lists because I 
# created custom data structures using Node objects and pointers. The 
# Stack class tracks the top node, while the Queue class tracks both 
# the front and rear nodes. Instead of relying on built-in list methods
#  such as append() and pop(), my classes use linked nodes to add, 
# remove, and access values. This demonstrates how stacks and queues 
# work internally and gives direct control over their behavior. The 
# custom implementations also enforce the intended access patterns: 
# LIFO for the stack and FIFO for the queue.
