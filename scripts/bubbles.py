"""
File: bubbles.py
Author: Nino Estrada
Date: November 2, 2024

Description:
This script generates randomize bubbles.


Usage:
- Import this script into Maya using the Python script editor.
- Call create_bubbles() to generate ramdomize bubbles.

Examples:
# Create random bubbles
create_bubbles()
"""


import maya.cmds as cmds
import random  # Generating random values
from typing import List, Dict

def create_bubbles(bubble_count: int = 10) -> List[Dict[str, float]]:
    """
    Creates a specified number of bubbles with random positions and sizes.

    Args:
    bubble_count (int): The number of bubbles to create. (default: 10)

    Returns:
    List[Dict[str, float]]: A list of dictionaries containing information about the created bubbles.
    """
    bubbles = []

    for i in range(bubble_count):
        radius = random.uniform(0.1, 0.5)
        x_pos = random.uniform(0.1, 5)
        y_pos = random.uniform(0.1, 5)
        z_pos = random.uniform(0.1, 5)

        # Create Bubble
        bubble_name = f'bubble_{i + 1}'
        bubble = cmds.polySphere(name=bubble_name, radius=radius)[0]

        # Store Bubble Info
        bubbles.append({'name': bubble_name, 'radius': radius})

        # Move Bubble
        cmds.move(x_pos, y_pos, z_pos, bubble)

    return bubble