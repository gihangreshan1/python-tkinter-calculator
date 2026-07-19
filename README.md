# Python Tkinter Calculator

A simple and user-friendly calculator application built with Python's Tkinter library. This calculator provides basic arithmetic operations with a clean graphical user interface.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Percentage Calculation**: Quick percentage calculations
- **Clear Function (AC)**: Clear all input and start fresh
- **Backspace Function (CE)**: Remove the last digit entered
- **Error Handling**: Displays "Error" for invalid expressions
- **Intuitive GUI**: Clean and modern interface with color-coded buttons
- **Non-resizable Window**: Fixed window size for consistent appearance

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Screenshots

<img width="346" height="535" alt="image" src="https://github.com/user-attachments/assets/34872e6a-0641-4a8f-b9c2-c5e58e7dae4e" />

<img width="342" height="530" alt="image" src="https://github.com/user-attachments/assets/867db917-8a02-4459-bfdc-90ebecd8d886" />

<img width="340" height="527" alt="image" src="https://github.com/user-attachments/assets/da99ece8-88a6-4b72-baf9-f3678c83e608" />




## Installation

1. Clone the repository:
```bash
git clone https://github.com/gihangreshan1/python-tkinter-calculator.git
```

2. Navigate to the project directory:
```bash
cd python-tkinter-calculator
```

## Usage

Run the calculator by executing:
```bash
python main.py
```

The calculator window will open with a display area and buttons for numbers and operations.

### Button Guide

- **Number Buttons (0-9)**: Enter digits
- **Operators (+, -, *, /)**: Perform arithmetic operations
- **%**: Calculate percentages
- **AC (Clear All)**: Clear the entire display and reset
- **CE (Clear Entry)**: Remove the last digit (backspace)
- **=**: Calculate and display the result
- **.**: Add decimal point

## How It Works

The calculator uses Python's built-in `eval()` function to evaluate mathematical expressions entered by the user. 

### Key Functions

- `button_click(value)`: Appends the clicked button value to the display
- `clear_display()`: Clears all content from the display
- `backspace()`: Removes the last character from the display
- `calculate()`: Evaluates the expression and displays the result

## UI Design

- **Display**: Large green entry field for clear visibility
- **Buttons**: 
  - **Orange buttons**: AC (Clear All) and CE (Backspace)
  - **Dark buttons**: Numbers and operators
  - **Green display**: High contrast for easy reading
- **Window**: 340x500 pixels, non-resizable for stability

## Example Operations

- `5 + 3` → `8`
- `10 - 4` → `6`
- `7 * 8` → `56`
- `20 / 4` → `5`
- `50 * 20%` → `10`

## Limitations

- Uses `eval()` which can be a security concern for untrusted input (fine for a local calculator)
- No history of previous calculations
- No support for parentheses or advanced operations

## Future Enhancements

- Add support for parentheses and order of operations
- Include history of calculations
- Add keyboard support for number and operation input
- Implement scientific calculator features
- Add themes/dark mode

## License

This project is open source and available for personal and educational use.

## Author

**gihangreshan1**

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes!
