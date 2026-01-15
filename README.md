# 🧮 PowerCalculator

A powerful command-line calculator built in Python with advanced features including operator precedence, parentheses support, and calculation history.

## ✨ Features

- ✅ **Basic Operations**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)
- ✅ **Operator Precedence**: Automatically respects mathematical order of operations
- ✅ **Parentheses Support**: Handle complex expressions like `(5 + 3) * 2`
- ✅ **Flexible Input**: Works with or without spaces (`5+3` or `5 + 3`)
- ✅ **Decimal Numbers**: Full support for floating-point calculations
- ✅ **Negative Numbers**: Handle negative values like `-5 + 3`
- ✅ **Calculation History**: Save and view past calculations
- ✅ **Input Validation**: Comprehensive error checking and helpful error messages
- ✅ **Clean Interface**: Clear screen functionality for better user experience

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher (uses `match` statements)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mahira-manico/my_calculator.git
cd my_calculator
```

2. Run the calculator:
```bash
python main.py
```

## 📖 Usage

### Main Menu

When you start the calculator, you'll see:

```
--Welcome to PowerCalculator!--
1. calculator
2. see history
3. remove history
Ctrl + C to quit
```

### Making Calculations

**Simple operations:**
```
5 + 3        → 8
10 * 2       → 20
100 / 4      → 25.0
```

**Without spaces:**
```
5+3          → 8
10*2+5       → 25
```

**Complex expressions:**
```
(5 + 3) * 2  → 16
10 + 2 * 5   → 20  (respects order of operations)
2 ** 3       → 8   (power)
10 // 3      → 3   (floor division)
10 % 3       → 1   (modulo)
```

**Decimal numbers:**
```
5.5 + 3.2    → 8.7
10.5 * 2     → 21.0
```

**Negative numbers:**
```
-5 + 3       → -2
10 + -3      → 7
-10 * -2     → 20
```

### Viewing History

Select option `2` to view all your past calculations:

```
--Calculs history--

5 + 3 = 8
10 * 2 + 5 = 25
(5 + 3) * 2 = 16
```

### Clearing History

Select option `3` and confirm to clear your calculation history.

## 🏗️ Project Structure

```
my_calculator/
│
├── main.py                 # Entry point
├── menu_core.py            # Main menu loop and user interaction
├── functions.py            # Core calculation logic
├── display.py              # Display functions (menu, results, clear screen)
├── history.py              # History management (save, display, delete)
├── verification_errors.py  # Input validation and error checking
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🔧 Technical Details

### Operator Precedence

The calculator respects the standard mathematical order of operations:

1. **Parentheses**: `( )`
2. **Exponentiation**: `**`
3. **Multiplication/Division/Modulo**: `*`, `/`, `//`, `%`
4. **Addition/Subtraction**: `+`, `-`

### Input Parsing

The `parsing()` function intelligently tokenizes input:
- Handles numbers with decimals (`5.5`)
- Recognizes negative numbers (`-5`)
- Supports multi-character operators (`**`, `//`)
- Works with or without spaces

### Error Handling

The calculator validates:
- ✅ Minimum argument count (needs at least 3 elements)
- ✅ Valid operators and numbers
- ✅ Balanced parentheses
- ✅ Division by zero
- ✅ Proper operator placement

## 📝 Examples

### Basic Arithmetic
```python
Input: 15 + 27
Output: result: 42.0

Input: 100 - 58
Output: result: 42.0
```

### Order of Operations
```python
Input: 2 + 3 * 4
Output: result: 14.0  # Not 20

Input: (2 + 3) * 4
Output: result: 20.0
```

### Advanced Calculations
```python
Input: 2 ** 10
Output: result: 1024.0

Input: (10 + 5) * 2 - 3
Output: result: 27.0

Input: 100 / (2 + 3)
Output: result: 20.0
```

## 🛡️ Error Messages

The calculator provides clear error messages:

```
❌ Need at least 3 arguments! 1 given
❌ Error! + is unknown.
❌ Error! Unbalanced parentheses.
❌ Error! Add "*" before '('
❌ Error! 0 cannot divide by zero!
❌ Please enter a number!
```

## 🎯 Features in Detail

### Calculation History

All calculations are automatically saved to `history.txt`:
- Persists between sessions
- Can be viewed anytime via menu option 2
- Can be cleared with confirmation via menu option 3

### Clean Interface

The calculator uses `clear_screen()` to maintain a clean, focused interface:
- Clears between menu selections
- Provides visual separation between operations
- Uses sleep timers for user feedback

### Input Flexibility

The parser handles various input formats:
- `5+3` (no spaces)
- `5 + 3` (with spaces)
- `5  +  3` (irregular spacing)
- `(5+3)*2` (complex expressions)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Mahira Manico**
- GitHub: [@mahira-manico](https://github.com/mahira-manico)

## 🙏 Acknowledgments

Built as a learning project to understand:
- Python fundamentals
- Parsing algorithms
- Error handling
- File I/O operations
- User interface design

---

**Enjoy calculating! 🎉**
