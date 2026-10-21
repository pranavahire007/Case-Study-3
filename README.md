# Case-Study-3
# ↩️ Undo and Redo System Using Stack

> A simple Python-based Undo and Redo System developed using the **Stack Data Structure**.

---

## 🎯 Objective

To develop a simple and user-friendly Undo and Redo System using Python and the Stack data structure to manage text changes and allow users to reverse or restore their previous actions efficiently.

---

## 📖 Introduction

The **Undo and Redo System** is a simple application that simulates the basic text editing functionality found in text editors and word processing applications.

The project uses the **Stack data structure**, which follows the Last In, First Out (LIFO) principle. According to this principle, the last operation performed is the first operation to be reversed.

In this project, users can add text, undo the most recent change, redo a previously undone change, display the current text, and clear the text. Two stacks are used to maintain the editing history: an Undo Stack and a Redo Stack.

Whenever a new text change is made, the previous state is saved in the Undo Stack. When the user performs an undo operation, the current state is transferred to the Redo Stack, allowing the change to be restored later.

This project demonstrates the practical application of stacks in text editors and other software applications that support undo and redo functionality.

---

## ✨ Features

| **Feature** | **Description** |
|---|---|
| ✍️ Add Text | Add new text to the editor |
| ↩️ Undo | Reverse the most recent text change |
| ↪️ Redo | Restore a previously undone change |
| 📄 Display Text | View the current text in the editor |
| 🧹 Clear Text | Clear the current text content |
| 🚪 Exit | Exit the application |

---

## 🧩 Data Structure Used

### Stack

A **Stack** is a linear data structure that follows the Last In, First Out (LIFO) principle. The last element inserted into a stack is the first element removed.

This project uses two stacks:

- **Undo Stack:** Stores previous text states so that the most recent change can be reversed.
- **Redo Stack:** Stores text states that have been undone so they can be restored.

**Structure:**

`Undo Stack → Previous Text States`

`Redo Stack → Undone Text States`

### Stack Operations

- **Push:** Adds a new element to the top of the stack.
- **Pop:** Removes and returns the top element from the stack.

When a new text change is made, the previous state is pushed onto the Undo Stack, and the Redo Stack is cleared to maintain a consistent editing history.

---

## 💻 Technology Used

- 🐍 **Python**
- 📚 **Stack Data Structure**
- 📋 **Python Lists**
- 🧱 **Functions and Conditional Statements**
- 🖥️ **Visual Studio Code (VS Code)**

---

## ⚙️ Operations

### ✍️ Add Text

Allows the user to enter new text and append it to the existing content. The previous text state is saved in the Undo Stack.

### ↩️ Undo

Reverses the most recent text change by restoring the previous state from the Undo Stack. The current state is saved in the Redo Stack.

### ↪️ Redo

Restores a previously undone text state by retrieving it from the Redo Stack and saving the current state in the Undo Stack.

### 📄 Display Text

Displays the current text stored in the editor.

### 🧹 Clear Text

Removes all text from the editor while preserving the previous state so that the clearing operation can be undone.

### 🚪 Exit

Terminates the application.

---

## ▶️ How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Create or open the `main.py` file.
5. Open the terminal in VS Code.
6. Run the following command:

```bash
python main.py
```

7. Select an option from the menu to perform the desired operation.

---

## 📌 Learning Outcomes

Through this project, we understand:

- How the **Stack data structure** works.
- The concept of Last In, First Out (LIFO).
- How to perform push and pop operations using Python lists.
- How two stacks can be used to implement undo and redo functionality.
- How to maintain and restore previous states of data.
- How to handle empty stacks using conditional statements.
- How data structures are applied in text editors and other real-world applications.
- How to develop a menu-driven application using Python functions.

---

## 🎓 Conclusion

The **Undo and Redo System** successfully demonstrates the practical implementation of the Stack data structure in Python. By using two stacks to maintain previous and undone text states, the application allows users to add text, reverse recent changes, restore undone changes, and manage text content efficiently.

Through this project, we gain a better understanding of the LIFO principle, stack operations, and the importance of maintaining a history of changes. It also strengthens our knowledge of Python programming, functions, lists, and conditional statements.

Overall, this case study illustrates how stacks can be applied to solve real-world problems and provide useful functionality in text editors, document applications, and other software systems that support undo and redo operations.

---

### 👩‍💻 Developed as a Data Structures and Algorithms Case Study

**Python | Stack | LIFO | Undo and Redo System**
