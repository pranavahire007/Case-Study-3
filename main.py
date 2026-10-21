
# Undo and Redo System Using Stack

text = ""
undo_stack = []
redo_stack = []


def add_text():
    global text

    new_text = input("Enter text to add: ")

    undo_stack.append(text)
    text += new_text
    redo_stack.clear()

    print("Text added successfully!")


def undo():
    global text

    if not undo_stack:
        print("Nothing to undo.")
    else:
        redo_stack.append(text)
        text = undo_stack.pop()
        print("Undo successful!")


def redo():
    global text

    if not redo_stack:
        print("Nothing to redo.")
    else:
        undo_stack.append(text)
        text = redo_stack.pop()
        print("Redo successful!")


def display_text():
    print("\nCurrent Text:")
    print("-" * 30)
    print(text if text else "(Empty)")
    print("-" * 30)


def clear_text():
    global text

    if not text:
        print("The editor is already empty.")
    else:
        undo_stack.append(text)
        text = ""
        redo_stack.clear()
        print("Text cleared successfully!")


while True:
    print("\n===== Undo and Redo System =====")
    print("1. Add Text")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Text")
    print("5. Clear Text")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_text()

    elif choice == "2":
        undo()

    elif choice == "3":
        redo()

    elif choice == "4":
        display_text()

    elif choice == "5":
        clear_text()

    elif choice == "6":
        print("Thank you for using Undo and Redo System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
