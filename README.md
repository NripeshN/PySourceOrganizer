### Description:

`PySourceOrganizer` is a handy Python tool that lets you rearrange functions and classes in your Python source code alphabetically. Not only does it reorder your functions and classes, but it also ensures that comments, decorators, and whitespaces associated with each function or class are preserved and moved along with them.

---

### Features:

- Automatically rearrange functions and classes alphabetically.
- Preserve comments, decorators, and whitespaces associated with each function or class.
- Handles Python source files with imports, ensuring they stay at the top.
- Provides a command-line interface for ease of use.

---

### How to Use:

1. Clone the repository:

   ```bash
   git clone https://github.com/[YourUsername]/PySourceOrganizer.git
   ```

2. Navigate to the cloned directory:

   ```bash
   cd PySourceOrganizer
   ```

3. Run the tool with the desired Python file:

   ```bash
   python formatter.py [path_to_your_file.py]
   ```

   Replace `[path_to_your_file.py]` with the path to the Python file you wish to rearrange.

---

### Example:

Before:

```python
def zeta_function():
    # Zeta Function Code
    pass

# This is the main function
def main():
    pass

class Apple:
    # Apple class description
    pass
```

After:

```python
class Apple:
    # Apple class description
    pass

# This is the main function
def main():
    pass

def zeta_function():
    # Zeta Function Code
    pass
```

---

### Contributing:

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

### License:

This project is licensed under the MIT License.

---

### Disclaimer:

This tool is designed for organizing and improving the readability of Python source code files. Always back up your original source files before using this or any other code modification tool.
