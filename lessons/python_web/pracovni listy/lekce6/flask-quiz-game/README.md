# Flask Quiz Game

## Overview
The Flask Quiz Game is a web-based quiz application built using the Flask framework. It allows users to test their knowledge on various topics through an interactive quiz format. The application features a user-friendly interface, dynamic question loading, and a scoring system to provide feedback on performance.

## Features
- Interactive quiz gameplay
- Dynamic question loading from a JSON file
- User score tracking and feedback
- Responsive design for various devices

## Project Structure
```
flask-quiz-game
├── app.py                # Entry point of the application
├── static                # Static files (CSS, JS, images)
│   ├── css
│   │   └── style.css     # Styles for the application
│   ├── js
│   │   └── game.js       # JavaScript for game logic
│   └── images
│       └── logo.svg      # Logo image
├── templates             # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Landing page
│   ├── game.html         # Game interface
│   ├── question.html      # Individual question rendering
│   └── results.html      # Results display
├── models                # Data models
│   ├── __init__.py       # Initialize models package
│   ├── quiz.py           # Quiz logic
│   └── user.py           # User data handling
├── routes                # Application routes
│   ├── __init__.py       # Initialize routes package
│   ├── main.py           # Main application routes
│   └── game.py           # Game-related routes
├── data                  # Data files
│   └── questions.json     # Quiz questions in JSON format
├── config.py             # Configuration settings
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-quiz-game
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/` to start the quiz game.

## Gameplay
- Start the game from the landing page.
- Answer the questions presented one by one.
- At the end of the quiz, view your score and feedback based on your performance.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.