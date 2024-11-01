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

<!-- OVERVIEW OF COMMANDS -->
## 📖 Overview of Bookshelf Commands
The `create_bookshelf()` and `create_bookshelf_ui()` commands allow users to create customizable 3D bookshelves directly in Maya. The `create_bookshelf()` command generates the bookshelf model based on specified parameters, while `create_bookshelf_ui()` provides a user-friendly interface for setting these parameters visually.

<!-- FILES ADDED -->
### **📁➕ Files Added**
#### scripts:
- `bookshelf.py` - Generates a 3D bookshelf model in Maya with custom settings.
#### ui:
- `create_bookshelf_ui.py` - Script to create a user-friendly interface for setting up a bookshelf with custom settings in Maya.

<!-- Parameters -->
### **🔖 Parameter Reference**
| Parameters      | Data Type   | Description                                                                               | 
| :---------:     |:-----------:| :-----------:                                                                             |  
| shelf_count     | int         | The number of shelves on the bookshelf. The default is 10 if not provided.                | 
| shelf_width     | float       | The width of each shelf. The default is 10 if not provided.                               |   
| shelf_thickness | float       | The thickness of each shelf. The default is 0.5 if not provided.                          | 
| shelf_depth     | float       | The depth of each shelf. The default is 1 if not provided.                                | 
| shelf_spacing   | float       | The spacing between shelves. The default is 2 if not provided.                            | 
| add_books       | bool        | Add books to the bookshelf. The default is false.                                         | 
| book_count      | int         | The number of books on each shelf. The default is 10 if not provided.                     | 
| color_option    | int         | The color settings for books: 1 = no color (default), 2 = random, and 3 = specific color. |
| specific_color  | tuple       | The specified color of each book if color option = 3. The default is black, (0, 0, 0).    | 

**⚠️ Note**: All parameters in `create_bookshelf()` are optional. When specifying custom settings, it’s best to use **keyword arguments** (e.g., `create_bookshelf(shelf_count=10, shelf_width=12.5)`). This ensures each argument is assigned correctly, regardless of the order, preventing potential misalignment. 

<!-- EXAMPLES -->
### **📋 Examples**
 **Bookshelf with Default Settings**
```
create_bookshelf()
```
 
 **Bookshelf with Books Added**
```
create_bookshelf(add_books=True)
```
 
 **Bookshelf with Custom Shelf Count, Shelf Spacing, Shelf Width, and 13 Books Added**
```
create_bookshelf(shelf_count=14, shelf_spacing=3.0, shelf_width=12.5, add_books=True, book_count=13)
```

<!-- UI Overview -->
## **🖥️ UI Overview**
The `create_bookshelf_ui()` command opens a user interface that allows you to customize a bookshelf.

![Bookshelf UI Example](./images/UI%20Example.png)
*Example of the 'Create Bookshelf' UI in Maya*

<!-- UI -->
### **🗂️ UI Components Reference**
| Component       | Type         | Description                                                                | 
| :---------:     |:-----------: | :-----------:                                                              |  
| Shelf Count     | Input Field  | The number of shelves on the bookshelf. The default is 10 if not provided. | 
| Shelf Width     | Input Field  | The width of each shelf. The default is 10 if not provided.                |   
| Shelf Thickness | Input Field  | The thickness of each shelf. The default is 0.5 if not provided.           | 
| Shelf Depth     | Input Field  | The depth of each shelf. The default is 1 if not provided.                 | 
| Shelf Spacing   | Input Field  | The spacing between shelves. The default is 2 if not provided.             | 
| Add Books?      | Checkbox     | Add books to the bookshelf. The default is false.                          | 
| Books per Shelf | Input Field  | The number of books on each shelf. The default is 10 if not provided.      | 
| Book Colors     | Radio Button | Color option for each book: No color (default), random, or specific color. |
| Choose Color    | Color Picker | The specified color of each book. The default is black, (0, 0, 0).         | 

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
    ```
    create_bookshelf()
    ```

- **Creates a user-friendly interface for creating a bookshelf**
    ```
    create_bookshelf_ui()
    ```