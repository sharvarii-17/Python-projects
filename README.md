# Python-projects

## Guessing Game
A simple Python GUI application using Tkinter where the user tries to guess a randomly generated number.
This project implements a guessing game where the player is prompted to guess a number between 1 and 100. After each guess, the program provides feedback on whether the guess is too high or too low. The game continues until the player correctly guesses the number.

### Features
- Generates a random number between 1 and 100 for the player to guess.
- Provides feedback on each guess (too high, too low, or correct).
- Counts the number of attempts made by the player.
- Disables the guess button once the correct number is guessed.
- Handles invalid inputs gracefully.


## Transportation Network Visualization
This Python script demonstrates how to use NetworkX and Matplotlib to visualize the shortest path in a graph using Dijkstra's algorithm. The script generates a graph based on the given connections and calculates the shortest path, along with additional information such as distance, time taken, and fare.

### Features
- Graph Representation: The transportation network is represented as a graph, where places are nodes and connections between places are edges.
- Shortest Path Calculation: Dijkstra's algorithm is employed to find the shortest path between a specified start place and destination.
- Visualization: Matplotlib is used to create a visual representation of the transportation network, highlighting the shortest path.
- Information Display: The script provides information about the selected path, including distance, time, and fare.

### Usage
- Define the graph connections and fare per kilometer in the script.
- Run the script and follow the prompts to enter the start and destination places.
- The script will display a graphical representation of the shortest path, along with information about the journey.


## Text Summarization with Cosine Similarity and PageRank
This Python script demonstrates text summarization using cosine similarity and the PageRank algorithm from the NetworkX library. It extracts important sentences from a text file to generate a concise summary.

### Features
- Text Summarization: The script reads a text file, processes its content, and generates a summary by selecting the most relevant sentences.
- Cosine Similarity: Sentence similarity is calculated using cosine distance to identify relationships between sentences.
- PageRank Algorithm: The PageRank algorithm is employed to rank sentences based on their importance in the context of the entire text.


## Simple Calculator with tkinter
This Python script creates a basic calculator GUI using the tkinter library. Users can perform arithmetic operations and evaluate expressions by clicking the corresponding buttons on the graphical interface

### Features
- Addition, subtraction, multiplication, and division operations.
- Parentheses support for complex expressions.
- Clear button to reset the calculation field.
- Error handling for invalid expressions.

### Usage
- Run the Python script
- The calculator window will appear with buttons for numbers, arithmetic operators, parentheses, equal sign (=), and clear (C).
- Click the buttons to enter numbers and perform calculations.
- Press the equal (=) button to evaluate the expression.
- Use the clear (C) button to reset the calculation field.


## Notepad Application
A simple Notepad application built using Python and Tkinter. This application allows you to create, open, edit, and save text files. It also includes basic text editing features such as cut, copy, paste, and find text.

### Features
- Create new text files.
- Open existing text files.
- Save text files.
- Basic text editing functions: cut, copy, paste, and clear.
- Find text within the document.
- Display information about the application.

### Prerequisites
To run this project, you need to have Python installed on your machine. Additionally, the tkinter module, which is included in the standard Python distribution, is required.

### Usage
- New File: Create a new text file.
- Open File: Open an existing text file.
- Save File: Save the current text file.
- Exit: Exit the application.
- Cut: Cut the selected text.
- Copy: Copy the selected text.
- Paste: Paste the copied/cut text.
- Clear: Clear the entire text.
- Find: Find specific text in the document.
- About: Display information about the application.
