# Simple To-Do List App

## Overview
A lightweight, user-friendly application designed to help beginners efficiently manage daily tasks and responsibilities. This app is specifically aimed at students and busy individuals seeking an intuitive solution for better productivity and time management.

## Target Users
- Students juggling multiple classes
- Busy professionals
- Anyone looking for a simple organization system

## Key Features

### 1. Task Creation
- Easy addition of new tasks
- Support for descriptions and due dates
- Straightforward input interface

### 2. Task Management
- One-click completion status toggle
- Simple editing and deletion functionality
- Intuitive controls for quick updates

### 3. Task Visualization
- Clean, minimalist interface
- Color-coding system for different categories (classes, work, personal, family)
- Clear status indicators for better organization and visual clarity

## Educational Value
This project serves as an excellent introduction to web development, offering hands-on experience with:
- CRUD operations
- Backend-frontend interactions
- Database management
- User interface design

The manageable scope makes it ideal for a single student developer while providing valuable practical experience with essential software development skills.

## Similar Projects and Resources
- [Flask To-Do by Patrick Loeber](https://github.com/patrickloeber/flask-todo)
- [Flask To-Do List by Zac Clery](https://github.com/zacclery/Flask-ToDo-List)
- [Flask TODO APP by Mohammed Ashraf](https://github.com/mohammed97ashraf/Flask-TODO-APP)

# To-Do List App Project Roadmap

## Project Setup
- [x] Create project directory  
- [x] Create main Python file (`todo.py`)  
- [x] Create project roadmap document  

## Phase 1: Core Functionality
- [x] Design the command-line menu interface (`show_menu()`)  
- [x] Implement view tasks functionality (`view_tasks()`)  
- [x] Implement add task functionality (`add_task()`)  
- [ ] Implement file reading/writing for task storage *(Currently in-memory only)*

## Phase 2: Task Management
- [x] Implement mark as complete functionality (`mark_complete()`)  
- [x] Implement delete task functionality (`delete_task()`)  
- [ ] Add error handling for file operations *(pending file I/O implementation)*  
- [x] Add input validation (`try/except` for inputs and empty task checks)  
- [x] Test task management features *(Tested via command-line interactions)*