import pygame
import heapq
import tkinter as tk
from tkinter import messagebox

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 650
BACKGROUND = (228, 213, 199)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER_THICKNESS = 2
FONT_SIZE = 24
PADDING = 20
BUTTON_WIDTH = 200
MAX_PATIENTS = 20

# Priority Queue
priority_queue = []

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital Priority Queue")
font = pygame.font.Font(None, FONT_SIZE)

# Function to render text
def draw_text(text, rect, color=BLACK):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(rect.centerx, rect.centery))
    screen.blit(text_surface, text_rect)

# Function to draw the priority queue on the screen
def draw_priority_queue():
    display_rect = pygame.Rect(WIDTH // 2 + 25, display_margin_top, display_width, display_height)
    gap_between_items = 4  # Adjust this value as needed

    for i, (priority, patient_id, patient) in enumerate(priority_queue):
        if i == 0:
            y_position = display_rect.top + 12
        else:
            y_position = display_rect.top + 12 + i * (FONT_SIZE + gap_between_items)

        text = f"{i + 1}. {patient['name']} - Age: {patient['age']} Priority: {priority}"
        text_surface = font.render(text, True, BLACK)

        # Check if the text fits within the display area
        if display_rect.collidepoint(display_rect.centerx, y_position):
            text_rect = text_surface.get_rect(center=(display_rect.centerx, y_position))
            screen.blit(text_surface, text_rect)
        else:
            break

# Function to check if the mouse is over a button
def is_button_clicked(pos, button_rect):
    return button_rect.collidepoint(pos)

# Function to check if the mouse is over an input area
def is_input_area_hovered(pos, input_rect):
    return input_rect.collidepoint(pos)

# Tkinter setup for error alert
root = tk.Tk()
root.withdraw()

# Function to show an alert error
def show_error(message):
    error_window = tk.Toplevel(root)
    error_window.title("Error")
    tk.Label(error_window, text=message, padx=20, pady=20, background='#E4D5C7').pack()
    tk.Button(error_window, text="OK", command=error_window.destroy).pack()

# Initialize input fields and labels
name_label_rect = pygame.Rect(PADDING, PADDING, BUTTON_WIDTH, 30)
name_input_rect = pygame.Rect(name_label_rect.left, name_label_rect.bottom + 5, BUTTON_WIDTH, 30)

age_label_rect = pygame.Rect(PADDING, name_input_rect.bottom + 10, BUTTON_WIDTH, 30)
age_input_rect = pygame.Rect(age_label_rect.left, age_label_rect.bottom + 5, BUTTON_WIDTH, 30)

priority_label_rect = pygame.Rect(PADDING, age_input_rect.bottom + 10, BUTTON_WIDTH, 30)
priority_input_rect = pygame.Rect(priority_label_rect.left, priority_label_rect.bottom + 5, BUTTON_WIDTH, 30)

patient_number_label_rect = pygame.Rect(PADDING, priority_input_rect.bottom + 10, BUTTON_WIDTH, 30)
patient_number_input_rect = pygame.Rect(patient_number_label_rect.left, patient_number_label_rect.bottom + 5, BUTTON_WIDTH, 30)

new_priority_label_rect = pygame.Rect(PADDING, patient_number_input_rect.bottom + 10, BUTTON_WIDTH, 30)
new_priority_input_rect = pygame.Rect(new_priority_label_rect.left, new_priority_label_rect.bottom + 5, BUTTON_WIDTH, 30)

name_input = ""
age_input = ""
priority_input = ""
patient_number_input = ""
new_priority_input = ""

# Initialize button rectangles
add_button_rect = pygame.Rect(PADDING, new_priority_input_rect.bottom + 20, BUTTON_WIDTH, 50)
remove_button_rect = pygame.Rect(PADDING, add_button_rect.bottom + 10, BUTTON_WIDTH, 50)
change_button_rect = pygame.Rect(PADDING, remove_button_rect.bottom + 10, BUTTON_WIDTH, 50)

# Display section dimensions
display_width = WIDTH // 2 - 50  # Adjusted width with a 25px margin on both sides
display_height = 600
display_margin_top = 25
display_margin_bottom = 25

# Variable to keep track of added patients
added_patients = 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                x, y = event.pos

                # Add patient button
                if is_button_clicked((x, y), add_button_rect) and added_patients < MAX_PATIENTS:
                    # Get patient information from input fields
                    patient_name = name_input
                    patient_age = int(age_input) if age_input.isdigit() else 0
                    patient_priority = int(priority_input) if priority_input.isdigit() else 0

                    # Ensure all fields are filled
                    if not all([patient_name, patient_age, patient_priority]):
                        show_error("Please enter patient information.")
                        continue

                    # Ensure priority is between 1 and 5
                    patient_priority = max(1, min(5, patient_priority))

                    patient = {'name': patient_name, 'age': patient_age}
                    patient_id = added_patients  # Assign a unique ID to the patient based on order added
                    heapq.heappush(priority_queue, (patient_priority, patient_id, patient))
                    # Clear input fields
                    name_input = ""
                    age_input = ""
                    priority_input = ""
                    added_patients += 1
                    priority_queue.sort(reverse=True)  # Sort the queue based on priority

                # Remove patient button
                elif is_button_clicked((x, y), remove_button_rect):
                    if priority_queue:
                        heapq.heappop(priority_queue)
                        added_patients -= 1

                # Change patient priority button
                elif is_button_clicked((x, y), change_button_rect):
                    # Get patient information from input fields
                    patient_number = int(patient_number_input) if patient_number_input.isdigit() else -1
                    new_priority = int(new_priority_input) if new_priority_input.isdigit() else -1

                    # Ensure patient number is valid
                    if 0 < patient_number <= added_patients and 0 < new_priority <= 5:
                        # Update the priority of the specified patient
                        for i, (_, p_id, p) in enumerate(priority_queue):
                            if p_id == patient_number - 1:
                                priority_queue[i] = (new_priority, p_id, p)
                                heapq.heapify(priority_queue)
                                break
                    else:
                        show_error("Invalid patient number or new priority.")
                        continue

        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos

            # Change cursor to input cursor when hovering over input areas
            if (
                is_input_area_hovered((x, y), name_input_rect)
                or is_input_area_hovered((x, y), age_input_rect)
                or is_input_area_hovered((x, y), priority_input_rect)
                or is_input_area_hovered((x, y), patient_number_input_rect)
                or is_input_area_hovered((x, y), new_priority_input_rect)
            ):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        elif event.type == pygame.KEYDOWN:
            # ... (previous code remains unchanged)

    screen.fill(BACKGROUND)

    # Draw display section with border
    display_rect = pygame.Rect(WIDTH // 2 + 25, display_margin_top, display_width, display_height)
    pygame.draw.rect(screen, WHITE, display_rect)
    pygame.draw.rect(screen, BLACK, display_rect, BORDER_THICKNESS)

    # Draw input labels
    pygame.draw.rect(screen, BACKGROUND, name_label_rect)
    pygame.draw.rect(screen, BACKGROUND, age_label_rect)
    pygame.draw.rect(screen, BACKGROUND, priority_label_rect)
    pygame.draw.rect(screen, BACKGROUND, patient_number_label_rect)
    pygame.draw.rect(screen, BACKGROUND, new_priority_label_rect)

    draw_text("Name:", name_label_rect, color=BLACK)
    draw_text("Age:", age_label_rect, color=BLACK)
    draw_text("Priority:", priority_label_rect, color=BLACK)
    draw_text("Patient Number:", patient_number_label_rect, color=BLACK)
    draw_text("New Priority:", new_priority_label_rect, color=BLACK)

    # Draw input fields with black border
    pygame.draw.rect(screen, BLACK, name_input_rect, BORDER_THICKNESS)
    pygame.draw.rect(screen, WHITE, name_input_rect.inflate(-BORDER_THICKNESS * 2, -BORDER_THICKNESS * 2))
    draw_text(name_input, name_input_rect, color=BLACK)

    pygame.draw.rect(screen, BLACK, age_input_rect, BORDER_THICKNESS)
    pygame.draw.rect(screen, WHITE, age_input_rect.inflate(-BORDER_THICKNESS * 2, -BORDER_THICKNESS * 2))
    draw_text(age_input, age_input_rect, color=BLACK)

    pygame.draw.rect(screen, BLACK, priority_input_rect, BORDER_THICKNESS)
    pygame.draw.rect(screen, WHITE, priority_input_rect.inflate(-BORDER_THICKNESS * 2, -BORDER_THICKNESS * 2))
    draw_text(priority_input, priority_input_rect, color=BLACK)

    pygame.draw.rect(screen, BLACK, patient_number_input_rect, BORDER_THICKNESS)
    pygame.draw.rect(screen, WHITE, patient_number_input_rect.inflate(-BORDER_THICKNESS * 2, -BORDER_THICKNESS * 2))
    draw_text(patient_number_input, patient_number_input_rect, color=BLACK)

    pygame.draw.rect(screen, BLACK, new_priority_input_rect, BORDER_THICKNESS)
    pygame.draw.rect(screen, WHITE, new_priority_input_rect.inflate(-BORDER_THICKNESS * 2, -BORDER_THICKNESS * 2))
    draw_text(new_priority_input, new_priority_input_rect, color=BLACK)

    # Draw buttons with centered text
    pygame.draw.rect(screen, (200, 200, 200), add_button_rect)
    pygame.draw.rect(screen, (200, 200, 200), remove_button_rect)
    pygame.draw.rect(screen, (200, 200, 200), change_button_rect)
    draw_text("Add Patient", add_button_rect, color=BLACK)
    draw_text("Remove Patient", remove_button_rect, color=BLACK)
    draw_text("Change Priority", change_button_rect, color=BLACK)

    # Draw priority queue
    draw_priority_queue()

    pygame.display.flip()

# Quit Tkinter
root.destroy()
pygame.quit()
