# 🎯 Habit Tracker

A simple web application to track your daily habits.

## ✨ Features

- ➕ Add new habits
- 📋 View all habits
- ✅ Mark habits as done
- ↩️ Undo completed habits
- ✏️ Edit habit names
- 🗑️ Delete habits

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, CSS (Jinja2 templates)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Flask

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker
   ```

2. Install Flask:
   ```bash
   pip install flask
   ```

3. Run the app:
   ```bash
   python app.py
   ```

4. Open in browser:
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
habit-tracker/
├── app.py              # Main Flask app
├── static/
│   └── style.css       # Styling
├── templates/
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── add.html        # Add habit form
│   └── edit.html       # Edit habit form
└── habit.db            # Database (auto-generated)
```

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
