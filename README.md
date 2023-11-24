### Hospital Priority Queue Simulation

This Python script simulates a hospital priority queue using Pygame and Tkinter. The program allows users to add patients with different priorities, remove patients with the least priority, and perform other operations.

#### Pygame Setup

```python
import pygame
import heapq
import tkinter as tk
from tkinter import messagebox
```

1. **Initialization:** Pygame and Tkinter are initialized.

```python
pygame.init()
```

#### Constants

```python
WIDTH, HEIGHT = 1000, 650
BACKGROUND = (228, 213, 199)
# ... (Other constants)
```

2. **Constants:** Screen dimensions, colors, and button properties are defined.

#### Priority Queue

```python
priority_queue = []
```

3. **Priority Queue Initialization:** The priority queue is initialized as an empty list.

#### Pygame Setup

```python
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Priority Queue")
font = pygame.font.Font(None, FONT_SIZE)
```

4. **Pygame Setup:** Pygame window, font, and other essential elements are set up.

#### Functions

```python
def draw_text(text, rect, color=BLACK):
    # ... (Implementation)

def draw_priority_queue():
    # ... (Implementation)

def is_button_clicked(pos, button_rect):
    # ... (Implementation)

def update_patient_numbers():
    # ... (Implementation)

def is_input_area_hovered(pos, input_rect):
    # ... (Implementation)

def show_error(message):
    # ... (Implementation)

def show_max_capacity_error():
    # ... (Implementation)

def add_patient(patient_name, patient_age, patient_priority):
    # ... (Implementation)

# ... (Other functions)
```

5. **Helper Functions:** Functions for rendering text, drawing the priority queue, checking button clicks, and error handling are defined.

#### Tkinter Setup

```python
root = tk.Tk()
root.withdraw()
```

6. **Tkinter Setup:** Tkinter is set up for error alert messages.

#### Main Loop

```python
running = True
while running:
    for event in pygame.event.get():
        # ... (Event handling)

    screen.fill(BACKGROUND)

    # ... (Drawing elements)

    pygame.display.flip()

# Quit Tkinter
root.destroy()
pygame.quit()
```

7. **Main Loop:** The main loop handles Pygame events, button clicks, and updates the display.

#### Summary

This script simulates a hospital priority queue where patients are added with a given priority, and the "Remove Patient" button removes the patient with the least priority. The code also includes error handling and the ability to display the length of the priority queue.

