# Quote Notebook

## Overview
The Quote Notebook is a simple Flask application that allows users to create, view, and filter quotes. Users can add their favorite quotes along with the author's name, and the application will display them in a user-friendly interface.

## Project Structure
```
quote-notebook
├── app.py
├── templates
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   └── author.html
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── main.js
├── requirements.txt
└── README.md
```

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd quote-notebook
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Features
- Add new quotes with the author's name.
- View a list of all quotes.
- Filter quotes by a specific author.

## Dependencies
- Flask

## License
This project is licensed under the MIT License.