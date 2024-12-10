import pygame
from note_maps import KEY_TO_NOTE

# Colors for keys and background
color_grey  = (127, 127, 127)
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red   = (255, 0, 0)
color_blue   = (0, 0, 255)

is_note_on: dict[str, bool] = {}

num_white_keys = 0

# based on https://github.com/gabriel-duque/pygame-piano

for key in KEY_TO_NOTE:  # key is pygame keyboard event
    note = KEY_TO_NOTE[key] # the actual note like "C4", "Gs4" etc.
    is_note_on[note] = False
    if "s" not in note:
        num_white_keys += 1

def display_note_on(note: str):
    is_note_on[note] = True

def display_note_off(note: str):
    is_note_on[note] = False


def draw_keyboard(window) -> None:
    '''Draw the octave keyboard on screen'''

    margin = window.get_width() // 140

    white_width = (window.get_width() - 8 * margin) // num_white_keys
    black_width = white_width // 2 + 2 * margin

    left = margin
    top = margin
    bottom = window.get_height() - top

    # Draw white keys
    for note in is_note_on:
        if "s" in note:
            continue
        color = color_red if is_note_on[note] else color_white
        pygame.draw.rect(window, color, (left, top, white_width, bottom - top))
        left += margin + white_width

    # Reset left for black keys
    left = margin + white_width + margin // 2 - black_width // 2

    bottom = bottom - (bottom - top) // 3

    # Draw black keys
    for note in is_note_on:
        if "s" not in note:
            continue

        if note in ["Fs4", "Cs5"]:  # Skip the inexistant black key(E-F, and B-C)
            left += margin + white_width

        color = color_blue if is_note_on[note] else color_black
        pygame.draw.rect(window, color, (left, top, black_width, bottom - top))
        left += margin + white_width
