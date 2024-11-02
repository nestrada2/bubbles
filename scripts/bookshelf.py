"""
File: bookshelf.py
Author: Nino Estrada
Date: September 23, 2024

Description:
This script generates a bookshelf model in Maya with custom settings such as 
shelf count, width, height, spacing, and the option to add books with color.

Note: The default settings will be applied if the user does not specify their preferred 
settings. 

Usage:
- Import this script into Maya using the Python script editor.
- Call create_bookshelf() to generate a bookshelf with default or custom settings.
- Can be use in conjuction with create_bookshelf_ui() to create a user-friendly interface for creating the bookshelf.

Examples:
# Create a basic bookshelf with 12 shelves
create_bookshelf(shelf_count=12)

# Create 7 shelves with 32 books on each shelf, randomly placed
create_bookshelf(shelf_count=7, add_books=True, book_count=32)

Note: When specifying custom settings, it’s best to use keyword arguments (e.g., `create_bookshelf(shelf_count=10, shelf_width=12.5)`). 
This ensures each argument is assigned correctly, regardless of the order, preventing potential misalignment.
"""


import maya.cmds as cmds
import random  # Generating random values


def create_bookshelf(
        shelf_count: int = 10, 
        shelf_width: float = 10, 
        shelf_thickness: float = 0.5, 
        shelf_depth: float = 1, 
        shelf_spacing: float = 2,
        add_books: bool = False,
        book_count: int = 10,
        color_option: int = 1,
        specific_color: tuple = (0, 0, 0)
) -> None:
    """
    Creates a bookshelf based on the specified parameters.

    Args:
        shelf_count (int, optional): The number of shelves. (default: 10)
        shelf_width (float, optional): The width of each shelf. (default: 10)
        shelf_thickness (float, optional): The thickness of each shelf. (default: 0.5)
        shelf_depth (float, optional): The depth of each shelf. (default: 1)
        shelf_spacing (float, optional): The spacing between shelves. (default: 2)
        add_books (bool, optional): Add books to the bookshelf. (default: False)
        book_count (int, optional): The number of books on each shelf. (default: 10)
        color_option (int, optional): 1 = No color (default), 2 = random, and 3 = specific color.
        specific_color (tuple, optional): The specify color of each book if color option = 3. (default: (0, 0, 0))

    Returns:
        None
    """

    bookshelf_count = 1

    # Finding the Next Available Bookshelf Number in case Other Bookshelves have Been Created Before
    while (len(cmds.ls(f'Bookshelf_{bookshelf_count}')) > 0):
        bookshelf_count += 1

    bookshelf_name = f'Bookshelf_{bookshelf_count}'

    # Store the List of Objects
    objects = []
       
    # Bookshelf Frame
    frame_thickness = 0.5

    # Total Height of the Bookshelf
    frame_height = shelf_count * shelf_spacing + shelf_thickness
    
    # Create/Move Left Side of the Bookshelf
    cmds.polyCube(name=f'{bookshelf_name}_left_side', width=frame_thickness, height=frame_height, depth=shelf_depth)
    cmds.move(-shelf_width/2 - frame_thickness/2, frame_height/2, 0) # Note: Maya places objects at the origin (0, 0, 0) by default
    objects.append(f'{bookshelf_name}_left_side')
    
    # Create/Move Right Side of the Bookshelf
    cmds.polyCube(name=f'{bookshelf_name}_right_side', width=frame_thickness, height=frame_height, depth=shelf_depth)
    cmds.move(shelf_width/2 + frame_thickness/2, frame_height/2, 0)
    objects.append(f'{bookshelf_name}_right_side')

    # Create Shelves
    for i in range(0, shelf_count + 1):
        shelf_name = f'{bookshelf_name}_shelf_{i + 1}'
        shelf_y = (i * shelf_spacing) + (shelf_thickness/2)

        # Create/Move Current Shelf
        cmds.polyCube(name=shelf_name, width=shelf_width, height=shelf_thickness, depth=shelf_depth)
        cmds.move(0, shelf_y, 0)
        objects.append(shelf_name)

        # Optional: Add Books to Each Shelf
        if add_books and i < shelf_count:
            add_books_to_shelf(shelf_name, shelf_num=i, objects=objects, book_count=book_count, shelf_spacing=shelf_spacing, shelf_width=shelf_width, shelf_thickness=shelf_thickness, color_option = color_option, specific_color=specific_color)
    
    #  Group All the Objects Together
    cmds.group(*objects, name=bookshelf_name)

def add_books_to_shelf(
        shelf_name: str,
        shelf_num: int,
        objects: list,
        shelf_spacing: float = 2, 
        shelf_width: float = 10, 
        shelf_thickness: float = 0.5,
        book_count: int = 10,
        color_option: int = 0,
        specific_color: tuple = (0, 0, 0)  
) -> None:
    """
    Creates and adds a specified number of books to a given shelf in a bookshelf.

    Args:
        shelf_name (str): The name of the shelf transform node in Maya.
        shelf_num (int): The index of the shelf where books will be placed.
        objects (list): The list of all the objects within the current bookshelf for grouping purposes.
        shelf_spacing (float, optional): The spacing between shelves. (default: 2)
        shelf_width (float, optional): The width of each shelf. (default: 10)
        shelf_thickness (float, optional): The thickness of each shelf. (default: 0.5)
        book_count (float, optional): The number of books to place on the shelf. (default: 10)
        color_option (int, optional): 1 = No color (default), 2 = random, and 3 = specific color.
        specific_color (tuple, optional): The specify color of each book if color option = 3. (default: (0, 0, 0))

    Returns:
        None
    """

    # Query the World-Space Position of the Shelf: Return Value is an array: [x, y, z]
    shelf_position = cmds.xform(shelf_name, query=True, worldSpace=True, translation=True) 

    # Ensure Books Fit Between Shelves
    available_height = shelf_spacing - shelf_thickness 

    for i in range(book_count):
        # Randomize Book Dimensions Slightly
        book_width = random.uniform(0.3, 0.7)
        book_height = random.uniform(1.5, min(2.5, available_height - 0.1)) 
        book_depth = random.uniform(0.5, 1)

        # Track Available Width on the Shelf
        remaining_width = shelf_width

        # Check if there's Enough Space Left on the Shelf for Another Book
        if book_width > remaining_width:
            print(f"No more space on shelf {shelf_num} for additional books.")
            break 

        
        # Create Book
        book_name = f'{shelf_name}_book_{i + 1}'
        book = cmds.polyCube(name=book_name, width=book_width, height=book_height, depth=book_depth)[0]
        objects.append(book_name)
        
        # Position the Book on the Shelf
        x_pos = random.uniform(-shelf_width/2 + book_width/2, shelf_width/2 - book_width/2)

        # Align to Bottom of the Shelf
        y_pos = (shelf_thickness / 2) + (book_height / 2) 
        
        # Position the Book Relative to the Current Shelf's Position
        cmds.move(
            # Add Shelf's x, y, z
            x_pos + shelf_position[0],  
            y_pos + shelf_position[1],  
            shelf_position[2]  
        )

        # Update the Remaining Width on the Shelf after Placing the Book
        remaining_width -= book_width + 0.1 
        
        # Only Apply Color if User Specifies
        if color_option > 1:
            apply_colors_to_books(color_option, specific_color)


def apply_colors_to_books(color_option: int, specific_color: tuple) -> None:
    '''
    Applies the specify color option to the last book created. 

    Args:
        color_option (int, optional): 1 = No color (default), 2 = random, and 3 = specific color.
        specific_color (tuple, optional): The specify color of each book if color option = 3. (default: (0, 0, 0))

    Returns:
        None
    '''

    # No Color Specified
    if color_option <= 1:
        return
    
    # Get the Selected Book Meshes
    selection = cmds.ls(selection=True)
    
    for i, mesh in enumerate(selection):
        # Create a New Shader for Each Book
        shader = cmds.shadingNode('aiStandardSurface', asShader=1, name=f'MAT_{i}')

        if color_option == 2:  
            # Random Color
            r = [random.random() for _ in range(3)]
        elif color_option == 3:  
            # Specific Color
            r = specific_color

        # Apply the Color
        cmds.setAttr(f'{shader}.baseColor', r[0], r[1], r[2], type='double3')
        cmds.select(mesh)
        cmds.hyperShade(a=shader)