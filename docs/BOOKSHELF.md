<!-- COMMAND LOGO -->
<div align="center">
    📚
    <h3 align="center" style="font-size: 2.1em; font-weight: bolder;">Bookshelf Documentation Guide</h3>

  <p align="center">
    Generate customizable 3D bookshelves directly in Maya
    <br />
    <br />
    <a href="https://github.com/nestrada2/bubbles/issues/new?labels=bug&template=bug_report.md">Report Bug</a>
    ·
    <a href="https://github.com/nestrada2/bubbles/issues/new?labels=enhancement&template=feature_request.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-overview-of-bookshelf-commands">Overview of Bookshelf Commands</a>
      <ul>
        <li><a href="#-files-added">Files Added</a></li>
      </ul>
    </li>
    <li>
      <a href="#-main-bookshelf-script">Main Bookshelf Script</a>
      <ul>
        <li><a href="#-parameter-reference">Parameter Reference</a></li>
        <li><a href="#-examples">Examples</a></li>
      </ul>
    </li>
    <li>
      <a href="#-ui-overview">UI Overview</a>
      <ul>
        <li><a href="#-components-reference">Components Reference</a></li>
      </ul>
    </li>
    <li><a href="#-running-the-program">Running the Program</a></li>
  </ol>
</details>

<!-- OVERVIEW OF BOOKSHELF COMMANDS -->
## 📖 Overview of Bookshelf Commands

The `create_bookshelf()` and `create_bookshelf_ui()` commands allow users to create customizable 3D bookshelves directly in Maya. The `create_bookshelf()` command generates the bookshelf model based on specified parameters, while `create_bookshelf_ui()` provides a user-friendly interface for setting these parameters visually.

<!-- FILES ADDED -->
### **📁➕ Files Added**
#### scripts:
- `bookshelf.py` - Generates a 3D bookshelf model in Maya with custom settings.
#### ui:
- `create_bookshelf_ui.py` - Script to create a user-friendly interface for setting up a bookshelf with custom settings in Maya.

<!-- Script Overview -->
## **🔧 Main Bookshelf Script**
The `bookshelf.py` script is the core of the Bookshelf tool, containing all functionality required to generate a customizable 3D bookshelf in Maya. It can be run independently or with the `create_bookshelf_ui()` script.

- **Command Name**: `create_bookshelf()`

- **Synopsis**
    ```python
    create_bookshelf( [shelf_count=int], [shelf_width=float], [shelf_thickness=float], [shelf_depth=float], [shelf_spacing=float], [add_books=bool], [book_count=int], [color_option=int], [specific_color=tuple] )
    ```

    **⚠️ Note:** Parameters in square brackets are optional.

<!-- Parameters -->
### **🔖 Parameter Reference**
| Parameters      | Data Type   | Description                                                                              | 
| :---------:     |:-----------:| :-----------:                                                                            |  
| shelf_count     | int         | The number of shelves on the bookshelf (default: 10)                                     | 
| shelf_width     | float       | The width of each shelf (default: 10)                                                    |   
| shelf_thickness | float       | The thickness of each shelf (default: 0.5)                                               | 
| shelf_depth     | float       | The depth of each shelf (default: 1)                                                     | 
| shelf_spacing   | float       | The spacing between shelves (default: 2)                                                 | 
| add_books       | bool        | Add books to the bookshelf (default: False)                                              | 
| book_count      | int         | The number of books on each shelf (default: 10)                                          | 
| color_option    | int         | The color settings for books: 1 = no color (default), 2 = random, and 3 = specific color |
| specific_color  | tuple       | The specified color of each book if color option = 3 (default: (0, 0, 0))                | 

**⚠️ Note**: When specifying custom settings, it’s best to use **keyword arguments** (e.g., `create_bookshelf(shelf_count=10, shelf_width=12.5)`). This ensures each argument is assigned correctly, regardless of the order, preventing potential misalignment. 

<!-- EXAMPLES -->
### **📋 Examples**
 **Bookshelf with Default Settings**
```python
create_bookshelf()
```
 
 **Bookshelf with Books Added**
```python
create_bookshelf(add_books=True)
```
 
 **Bookshelf with Custom Shelf Count, Shelf Spacing, Shelf Width, and 13 Books Added**
```python
create_bookshelf(shelf_count=14, shelf_spacing=3.0, shelf_width=12.5, add_books=True, book_count=13)
```

<!-- UI Overview -->
## **🖥️ UI Overview**
The `create_bookshelf_ui()` command opens a user interface that allows you to customize a bookshelf. It cannot be run independently, as it relies on `bookshelf.py` to function properly, which contains the core functionality required for bookshelf creation. Make sure both scripts are available when running.

- **Command Name**: `create_bookshelf_ui()`

- **Synopsis**
    ```python
    create_bookshelf_ui()
    ```

![Bookshelf UI Example](./images/UI%20Example.png)
<br />
*Example of the 'Create Bookshelf' UI in Maya*

<!-- UI -->
### **🗂️ UI Components Reference**
| Component       | Type         | Description                                                                | 
| :---------:     |:-----------: | :-----------:                                                              |  
| Shelf Count     | Input Field  | The number of shelves on the bookshelf (default: 10)                       | 
| Shelf Width     | Input Field  | The width of each shelf (default: 10)                                      |   
| Shelf Thickness | Input Field  | The thickness of each shelf (default: 0.5)                                 | 
| Shelf Depth     | Input Field  | The depth of each shelf (default: 1)                                       | 
| Shelf Spacing   | Input Field  | The spacing between shelves (default: 2)                                   | 
| Add Books?      | Checkbox     | Add books to the bookshelf (default: False)                                | 
| Books per Shelf | Input Field  | The number of books on each shelf (default: 10)                            | 
| Book Colors     | Radio Button | Color option for each book: No color (default), random, or specific color. |
| Choose Color    | Color Picker | The specified color of each book (default: black)                          | 

**⚠️ Note:** If no values are provided, the default settings are applied.

<!-- RUNNING THE PROGRAM -->
## **▶️ Running the Program**
1. **Import the Script into Maya**
   - Open Maya
   - Open the Script Editor (Window > General Editors > Script Editor)
   - Copy/paste the script into the Python tab of the Script Editor
2. **Execute the Script**
   - In the Maya Script Editor, make sure the language is set to Python, and click Execute (`Ctrl + Enter`) to run the script
3. **Run Commands**
- **Generates a bookshelf with default or custom settings**
    ```python
    create_bookshelf()
    ```

- **Creates a user-friendly interface for creating a bookshelf**
    ```python
    create_bookshelf_ui()
    ```