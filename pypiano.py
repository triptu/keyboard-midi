import pygame
from note_maps import KEY_TO_NOTE, NOTE_TO_HINDI_NOTE

# Colors for keys and background
color_grey  = (127, 127, 127)
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_white_key_text = (50, 50, 50)
color_white_selected   = (200, 200, 200)
color_black_selected   = (80, 80, 80)

is_note_on: dict[str, bool] = {}

num_white_keys = 0

# based on https://github.com/gabriel-duque/pygame-piano


'''
- Displays a piano with keys, controlled via keyboard(A,S,D... for white keys and W,E... for black keys)
- Makes sound when a key is pressed
- The events are exposed via midi as well, so if there is a website which can receive
  midi events, it will get the signal.
'''

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
    font = pygame.font.Font(None, white_width // 2)

    left = margin
    top = margin
    bottom = window.get_height() - top

    # Draw white keys
    for note in is_note_on:
        if "s" in note:
            continue
        color = color_white_selected if is_note_on[note] else color_white
        pygame.draw.rect(window, color, (left, top, white_width, bottom - top))

        # write the note names in the center of the white key on bottom
        text = font.render(note[0], True, color_white_key_text)
        hindi_note = font.render(NOTE_TO_HINDI_NOTE[note[0]], True, color_white_key_text)

        window.blit(text, (left + white_width // 2 - 15, bottom - top - white_width // 2 - 15))
        window.blit(hindi_note, (left + white_width // 2 - 15, bottom - top - white_width // 2 + white_width // 4 - 5))

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

        color = color_black_selected if is_note_on[note] else color_black
        pygame.draw.rect(window, color, (left, top, black_width, bottom - top))
        left += margin + white_width
