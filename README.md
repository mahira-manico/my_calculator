# 🧮 PowerCalculator

A powerful command-line calculator built in Python with advanced features including operator precedence, parentheses support, colorful interface, and calculation history.

## ✨ Features

- ✅ **Basic Operations**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)
- ✅ **Operator Precedence**: Automatically respects mathematical order of operations
- ✅ **Parentheses Support**: Handle complex expressions like `(5 + 3) * 2` and nested parentheses `((5+3)*2)`
- ✅ **Flexible Input**: Works with or without spaces (`5+3` or `5 + 3`)
- ✅ **Decimal Numbers**: Full support for floating-point calculations
- ✅ **Negative Numbers**: Handle negative values like `-5 + 3`
- ✅ **Calculation History**: Save and view past calculations with persistent storage
- ✅ **Input Validation**: Comprehensive error checking and helpful error messages
- ✅ **Colorful Interface**: Enhanced user experience with colored terminal output
- ✅ **Clean Interface**: Clear screen functionality for better user experience

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher (uses `match` statements)
- `colored` library for terminal colors

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mahira-manico/my_calculator.git
cd my_calculator
```

2. Install dependencies:
```bash
pip install colored
```

3. Run the calculator:
```bash
python main.py
```

## 📖 Usage

### Main Menu

When you start the calculator, you'll see a colorful menu:

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

**Complex expressions with parentheses:**
```
(5 + 3) * 2         → 16
10 + 2 * 5          → 20  (respects order of operations)
(10 + 5) * 2 - 3    → 27
100 / (2 + 3)       → 20.0
```

**Nested parentheses:**
```
((5 + 3) * 2)       → 16
(5 + (3 * 2))       → 11
((2 + 3) * (4 + 1)) → 25
```

**Power and modulo operations:**
```
2 ** 3       → 8    (power)
10 // 3      → 3    (floor division)
10 % 3       → 1    (modulo)
5 ** 2 + 3   → 28   (25 + 3)
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

**Mixed complex expressions:**
```
(5 + 3) * (2 - 1)        → 8
-5 * (3 + 2)             → -25
10.5 / (2 + 0.5) ** 2    → 1.68
```

### Viewing History

Select option `2` to view all your past calculations in a colorful format:

```
--Calculs history--

5 + 3 = 8
10 * 2 + 5 = 25
(5 + 3) * 2 = 16
((2 + 3) * 4) = 20
```

Type `menu` to return to the main menu.

### Clearing History

Select option `3` and you'll be prompted for confirmation:

```
Remove history? (y/n)
```

- Type `y` to clear all history
- Type `n` to cancel and keep your history

## 🏗️ Project Structure

```
my_calculator/
│
├── main.py                 # Entry point
├── menu_core.py            # Main menu loop and user interaction
├── functions.py            # Core calculation logic (calculator, parsing, parentheses)
├── display.py              # Display functions (menu, results, clear screen) with colors
├── history.py              # History management (save, display, delete) with colors
├── verification_errors.py  # Input validation and error checking
├── history.txt             # Persistent calculation history storage
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🔧 Technical Details

### Operator Precedence

The calculator respects the standard mathematical order of operations:

1. **Parentheses**: `( )` - Evaluated first, innermost to outermost for nested parentheses
2. **Exponentiation**: `**`
3. **Multiplication/Division/Modulo**: `*`, `/`, `//`, `%` (left to right)
4. **Addition/Subtraction**: `+`, `-` (left to right)

### Input Parsing Algorithm

The `parsing()` function intelligently tokenizes input character by character:
- **Numbers**: Recognizes integers and decimals (`5`, `5.5`)
- **Negative Numbers**: Detects negative signs at the start or after operators (`-5`, `3+-2`)
- **Multi-character Operators**: Identifies `**` and `//` before single-character operators
- **Parentheses**: Preserves parentheses for evaluation
- **Space Handling**: Automatically removes all spaces for consistent parsing
- **Error Detection**: Identifies invalid characters

**Example parsing:**
```python
Input:  "(5.5 + -3) * 2"
Output: ["(", "5.5", "+", "-3", ")", "*", "2"]
```

### Parentheses Evaluation

The `parentheses()` function uses an iterative algorithm:
1. Finds the **innermost** parentheses (last `(` before first `)`)
2. Evaluates the expression inside
3. Replaces the entire parentheses group with the result
4. Repeats until no parentheses remain

**Example with nested parentheses:**
```python
Expression: "((5+3)*2)"

Step 1: Find innermost → (5+3)
        Calculate: 5+3 = 8
        Replace: "(8*2)"

Step 2: Find next → (8*2)
        Calculate: 8*2 = 16
        Replace: "16"

Result: 16
```

### Error Handling

The calculator validates:
- ✅ **Minimum argument count**: Needs at least 3 elements (number operator number)
- ✅ **Valid tokens**: All elements must be numbers or valid operators
- ✅ **Balanced parentheses**: Equal number of `(` and `)`
- ✅ **Division by zero**: Prevents `/`, `//`, and `%` by zero
- ✅ **Implicit multiplication**: Requires `*` before parentheses (e.g., `5(3+2)` requires `5*(3+2)`)
- ✅ **Empty input**: Rejects empty operations
- ✅ **Invalid characters**: Identifies unknown symbols

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
Output: result: 14.0  # Not 20 (multiplication first)

Input: (2 + 3) * 4
Output: result: 20.0  # Parentheses force addition first
```

### Advanced Calculations
```python
Input: 2 ** 10
Output: result: 1024.0

Input: (10 + 5) * 2 - 3
Output: result: 27.0

Input: 100 / (2 + 3)
Output: result: 20.0

Input: ((5 + 3) * 2) + 1
Output: result: 17.0
```

### Edge Cases
```python
Input: -5 * -3
Output: result: 15.0

Input: 10 + -5
Output: result: 5.0

Input: (5)
Output: result: 5.0

Input: 0.1 + 0.2
Output: result: 0.30000000000000004  # Floating point precision
```

## 🛡️ Error Messages

The calculator provides clear error messages:

```
❌ Need at least 3 arguments! 1 given
❌ Error! xyz is unknown.
❌ Error! Unbalanced parentheses.
❌ Error! Add "*" before '('
❌ Error! 0 cannot divide by zero!
❌ Please enter a number!
❌ please enter an operation!
```

## 🎨 Color Scheme

The calculator uses the `colored` library for a vibrant interface:
- **Purple/Pink tones** (fg 177, 199) for menu items and prompts
- **Magenta** (fg 5) for user input prompts
- Color-coded output for better readability

## 🎯 Features in Detail

### Calculation History

All calculations are automatically saved to `history.txt`:
- **Persistent storage**: History survives program restarts
- **Automatic saving**: Every calculation is saved upon completion
- **View anytime**: Access via menu option 2
- **Confirmation before deletion**: Prevents accidental loss via option 3
- **Format**: Stores as `expression = result` for easy reading

### Clean Interface

The calculator maintains a clean, focused interface:
- **Clear screen**: Automatically clears between operations
- **Visual feedback**: Uses `time.sleep()` for user-friendly pauses
- **Organized flow**: Separate screens for calculation, history, and menu
- **Graceful exit**: Handles `Ctrl+C` with a goodbye message

### Input Flexibility

The parser handles various input formats seamlessly:
- `5+3` (no spaces)
- `5 + 3` (with spaces)
- `5  +  3` (irregular spacing)
- `(5+3)*2` (complex expressions without spaces)
- `( 5 + 3 ) * 2` (complex expressions with spaces)

### Interactive Workflow

After each calculation:
- Results are displayed immediately
- History is automatically saved
- User is prompted: "do you want to try again? (y/n)"
- Type `y` to continue calculating or `n` to return to menu

## 🚧 Known Limitations

- Floating-point precision limitations (standard for Python)
- No support for trigonometric functions (sin, cos, tan)
- No support for variables or constants (π, e)
- No support for square roots (use `** 0.5` instead)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest new features
- Submit pull requests
- Improve documentation

### Future Enhancement Ideas
- Add scientific functions (sin, cos, sqrt, etc.)
- Support for variables and memory storage
- Multi-line expression support
- Export history to CSV/JSON
- Unit tests for all functions
- Configuration file for color customization

## 📦 Dependencies

```
colored>=1.4.0
```

Install with:
```bash
pip install colored
```

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Mahira Manico**
- GitHub: [@mahira-manico](https://github.com/mahira-manico)

## 🙏 Acknowledgments

Built as a learning project to understand:
- Python fundamentals and best practices
- Parsing algorithms and tokenization
- Error handling and validation
- File I/O operations and data persistence
- User interface design and UX principles
- Terminal color formatting
- Recursive algorithm design (parentheses evaluation)

---

**Enjoy calculating! 🎉**

*Made with ❤️ and Python*