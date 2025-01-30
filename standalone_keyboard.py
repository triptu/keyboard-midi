import pygame
from pypiano import draw_keyboard, display_note_on, display_note_off, color_grey
from note_maps import KEY_TO_NOTE, NOTE_TO_NUMBER
import tinysoundfont
from threading import Timer

# The number of different notes in an octave
note_count = 12

# The octave we're playing in
octave = 4

# The default velocity (volume)
velocity = 100

synth = tinysoundfont.Synth()
sfid = synth.sfload("florestan-piano.sf2")
synth.program_select(0, sfid, 0, 0)
synth.start()
print("soundfont loaded")


def main() -> None:
    '''The main entrypoint for our program'''
    pygame.font.init()
    pygame.display.init()
    pygame.display.set_caption('Standalone Piano')
    window = pygame.display.set_mode((640, 360))
    window.fill(color_grey)
    draw_keyboard(window)
    pygame.display.update()

    # We only want to get events for our keyboard
    # Let's disable the others for performance
    # XXX: fix allowed events
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT])

    # Our main loop which gets pressed keys, plays or stops notes and updates the display
    go_on = True
    while go_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go_on = False

            # Turn note on if known key
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key in KEY_TO_NOTE:
                    note = KEY_TO_NOTE[key]
                    print(f'DOWN: Key: {key} Note: {note} ')
                    display_note_on(note)
                    synth.noteon(0, NOTE_TO_NUMBER[note], velocity)

                # Exit is user pressed <escape>
                elif key == pygame.K_ESCAPE:
                    go_on = False

            # Turn note off if known key
            elif event.type == pygame.KEYUP:
                key = event.key
                if key in KEY_TO_NOTE:
                    note = KEY_TO_NOTE[key]
                    print(f'UP: Key: {key} Note: {note} ')
                    display_note_off(note)
                    Timer(1.0, synth.noteoff, (0, NOTE_TO_NUMBER[note])).start()

        draw_keyboard(window)
        pygame.display.update()

    synth.stop()

if __name__ == '__main__':
    main()
