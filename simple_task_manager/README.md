# python-sqlite3-project/python-sqlite3-project/README.md

# Python SQLite3 Project

This project demonstrates how to use the SQLite3 library in Python to create a simple database with two tables: `Users` and `tags`.

## Project Structure

```
python-sqlite3-project
├── venv                # Virtual environment directory
├── src
│   ├── htuTraining.py  # Main logic for creating the SQLite database and tables
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Setup Instructions

1. **Clone the repository** (if applicable):
   ```
   git clone <repository-url>
   cd python-sqlite3-project
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**:
   Since `sqlite3` is part of the Python standard library, no additional packages are required for this project.

## Running the Code

To create the SQLite database and tables, run the following command:

```
python src/htuTraining.py
```

This will create a database file named `todolist.db` in the project directory with the specified tables.

## Additional Information

- Ensure you have Python installed on your machine (version 3.x is recommended).
- You can modify the `htuTraining.py` file to add more functionality as needed.