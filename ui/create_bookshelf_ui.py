"""
File: bookshelf.py
Author: Nino Estrada
Date: September 23, 2024

Description:
This script generates a bookshelf UI model asking users for their preferred 
settings such as shelf count, width, height, and spacing, etc. and, based on 
their inputs, will create a tailor-made bookshelf.

Note: The default settings will be applied if the user does not specify their preferred 
settings or leaves input fields empty. 

Usage:
- Import this script into Maya using the Python script editor.
- Call create_bookshelf_ui() to generate a bookshelf custom settings UI.

Examples:
# Generate bookshelf ui
create_bookshelf_ui()
"""


import maya.cmds as cmds
from scripts.bookshelf import create_bookshelf


def create_bookshelf_ui():
    """
    Creates a bookshelf UI asking user's specified preferences for a bookshelf.

    Returns:
        None
    """

    if cmds.window('bookshelfWindow', exists=True):
        cmds.deleteUI('bookshelfWindow', window=True)

    # UI Window Dimensions
    window = cmds.window('bookshelfWindow', title='Create Bookshelf', widthHeight=(500, 400))
    cmds.columnLayout(adjustableColumn=True)
    
    cmds.text(label='Bookshelf Dimensions')
    
    # Shelf Parameters: Input Fields
    shelf_count_field = cmds.intFieldGrp(label='Shelf Count', value1=5)
    shelf_width_field = cmds.floatFieldGrp(label='Shelf Width', value1=10)
    shelf_height_field = cmds.floatFieldGrp(label='Shelf Height', value1=0.5)
    shelf_depth_field = cmds.floatFieldGrp(label='Shelf Depth', value1=1)
    shelf_spacing_field = cmds.floatFieldGrp(label='Shelf Spacing', value1=2)
    
    # Bookshelf Options
    shelf_count=cmds.intFieldGrp(shelf_count_field, query=True, value1=True),
    shelf_width=cmds.floatFieldGrp(shelf_width_field, query=True, value1=True),
    shelf_height=cmds.floatFieldGrp(shelf_height_field, query=True, value1=True),
    shelf_depth=cmds.floatFieldGrp(shelf_depth_field, query=True, value1=True),
    shelf_spacing=cmds.floatFieldGrp(shelf_spacing_field, query=True, value1=True)

    # Spacing
    cmds.separator(h=10)
    cmds.text(label='Book Options')

    # Optional: Add Books
    add_books_field = cmds.checkBoxGrp(label='Add Books?', value1=False)

    # Optional: Book Count
    book_count_field = cmds.intFieldGrp(label='Books per Shelf', value1=10)

    # Optional: Book Color Options (None, Random, Specific)
    color_option_field = cmds.radioButtonGrp(label='Book Colors', labelArray3=['None', 'Random', 'Specific'], numberOfRadioButtons=3, select=1)
    color_picker_field = cmds.colorSliderGrp(label='Choose Color', rgb=(1, 1, 1))

    # Button to Create Bookshelf and Add Books
    cmds.button(label='Create Bookshelf with Books', command=lambda _: create_bookshelf(
        shelf_count=cmds.intFieldGrp(shelf_count_field, query=True, value1=True),
        shelf_width=cmds.floatFieldGrp(shelf_width_field, query=True, value1=True),
        shelf_depth=cmds.floatFieldGrp(shelf_depth_field, query=True, value1=True),
        shelf_spacing=cmds.floatFieldGrp(shelf_spacing_field, query=True, value1=True),
        add_books=cmds.checkBoxGrp(add_books_field, query=True, value1=True),
        book_count=cmds.intFieldGrp(book_count_field, query=True, value1=True),
        color_option=cmds.radioButtonGrp(color_option_field, query=True, select=True),
        specific_color=cmds.colorSliderGrp(color_picker_field, query=True, rgb=True)
    ))

    cmds.showWindow(window)
