# To-Do List Application

[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green?style=flat-square)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

A modern, full-stack To-Do List web application built with Flask and Bootstrap. Manage your tasks efficiently with a beautiful, responsive user interface. Features include adding, editing, deleting, and marking tasks as complete with a REST API backend.

## 🚀 Features

✨ **Core Functionality:**
- ✅ Add new tasks with titles and descriptions
- ✅ Edit existing tasks
- ✅ Delete tasks
- ✅ Mark tasks as complete/incomplete
- ✅ View all tasks with timestamps
- ✅ Persistent storage with SQLAlchemy
- ✅ Beautiful responsive web interface
- ✅ REST API endpoints for programmatic access
- ✅ Modal dialogs for better UX
- ✅ Real-time updates

## 📂 Project Structure

```
to-do-list/
├── README.md              # Project documentation
├── LICENSE               # MIT License
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── app.py                # Flask application and API
├── todo.db               # SQLite database (auto-generated)
├── src/                  # Source code directory
│   ├── __init__.py
│   ├── main.py
│   ├── task.py
│   ├── todo_list.py
│   └── utils.py
└── templates/            # Flask HTML templates
    ├── base.html         # Base template with Bootstrap
    └── index.html        # Main todo list page
```

## 📋 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the repository

```bash
git clone https://github.com/CoderXash9/to-do-list.git
cd to-do-list
```

### Step 2: Create a virtual environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## 🏃 Running the Web Application

### Start the Flask Development Server

```bash
python app.py
```

The application will start on `http://localhost:5000`

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## 🎯 Usage

### Web Interface

1. **Add a New Task:**
   - Click the "Add New Task" button
   - Enter task title (required)
   - Enter task description (optional)
   - Click "Add Task"

2. **Complete a Task:**
   - Check the checkbox next to the task
   - The task will be marked as complete

3. **Edit a Task:**
   - Click the "Edit" button on the task
   - Modify the title or description
   - Click "Update Task"

4. **Delete a Task:**
   - Click the "Delete" button on the task
   - Confirm the deletion

### REST API Endpoints

#### Get all todos
```bash
GET /api/todos
```

#### Get a specific todo
```bash
GET /api/todos/<id>
```

#### Create a new todo
```bash
POST /api/todos
Content-Type: application/json

{
  "title": "Task title",
  "description": "Task description"
}
```

#### Update a todo
```bash
PUT /api/todos/<id>
Content-Type: application/json

{
  "title": "Updated title",
  "description": "Updated description",
  "completed": true
}
```

#### Delete a todo
```bash
DELETE /api/todos/<id>
```

## 🛠️ Technology Stack

- **Backend:** Flask 3.0.0
- **Database:** SQLAlchemy with SQLite
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **JavaScript:** Vanilla JS for interactive features
- **Testing:** pytest
- **Code Quality:** black, flake8, mypy

## 📦 Dependencies

See `requirements.txt` for all dependencies. Main packages:
- Flask - Web framework
- Flask-SQLAlchemy - ORM and database toolkit
- click - CLI creation kit
- colorama - Terminal colors

## 🧪 Running Tests

```bash
pytest
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**CoderXash9** - Created this project as a demonstration of a full-stack Python web application.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For support, please open an issue on the [GitHub Issues](https://github.com/CoderXash9/to-do-list/issues) page.

---

**Happy Task Managing!** 📝✨
