Python File Handling System

A simple Python-based File Handling System that performs common file management operations through a command-line interface (CLI).

This project demonstrates practical use of Python's "pathlib" and "os" modules for working with files and folders.

Features

The project provides the following operations:

Main Operations

-  Create a new file
-  Read file content
-  Update an existing file
-  Delete a file

Update Operations

- Rename an existing file
- Read file content
- Create a new file
- Overwrite existing file content
- Append new content to an existing file

 Technologies Used

- Python 3
- "pathlib"
- "os"

 Project Structure

Python-File-Handling-System/
│
├── file_handling.py
└── README.md

 How to Run

1. Clone the repository

git clone https://github.com/your-username/Python-File-Handling-System.git

2. Navigate to the project directory

cd Python-File-Handling-System

3. Run the Python program

python file_handling.py

How It Works

When the program starts, it provides four main options:

Press 1 for creating a file.
Press 2 for reading a file.
Press 3 for updating a file.
Press 4 for deleting a file.

Create a File

The user enters the file name and content. The program checks whether the file already exists before creating it.

Read a File

The user provides the file name, and the program reads and displays its content.

Update a File

The update operation provides multiple options:

1. Change the file name
2. Read the file
3. Create a new file
4. Overwrite the file content
5. Append content to the file

Delete a File

The program checks whether the specified file exists and then deletes it.

 Concepts Practiced

This project helped practice the following Python concepts:

- Functions
- Conditional statements
- Exception handling
- User input
- File handling
- Reading and writing files
- File and directory paths
- "Path.exists()"
- "Path.is_file()"
- "Path.rename()"
- "Path.rglob()"
- "os.remove()"
- Context managers using "with open()"

 Purpose

The main purpose of this project is to understand how Python interacts with the file system and to practice implementing CRUD-style file operations using Python.

 Future Improvements

Possible future enhancements include:

- Add a graphical user interface (GUI)
- Add file type filtering
- Add folder creation and deletion
- Add file search functionality
- Add file copy and move operations
- Add better input validation
- Add a logging system

👩‍💻 Author

Reena Shah

B.Tech — Artificial Intelligence & Data Science

---

 If you find this project useful, consider giving the repository a star!
