import logging
import pymidi.client
import coloredlogs
import pygame
import tinysoundfont
from threading import Timer


from note_maps import KEY_TO_NOTE, NOTE_TO_NUMBER
from pypiano import draw_keyboard, color_grey, display_note_on, display_note_off


logger = logging.getLogger('pymidi.examples.server')

coloredlogs.install(level=logging.DEBUG)

# the address of the rtp midi server which the client connects to
host = '192.168.1.2'
port = 5004


class RTPMIDIKeyboardSimulator:
    def __init__(self):
        # MIDI note mapping (standard piano key layout)
        self.key_to_note_map = KEY_TO_NOTE

        # Active notes to track which are currently pressed
        self.active_notes = set()

        # Initialize Pygame for keyboard input
        pygame.init()
        pygame.display.set_caption('Midi Keyboard Client!')
        pygame.mixer.quit()
        self.window = pygame.display.set_mode((640, 360))
        self.window.fill(color_grey)
        draw_keyboard(self.window)
        pygame.display.update()

        # We only want to get events for our keyboard, disable the others for performance
        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT])

        # Set up RTP MIDI
        self.client = pymidi.client.Client(name="py-keyboard", ssrc=242423)
        self.synth = tinysoundfont.Synth() # for playing the notes


    def send_note_on(self, note, velocity=100):
        """Send a MIDI Note On message via RTP"""
        try:
            print(f"Note On: {note}")
            self.synth.noteon(0, NOTE_TO_NUMBER[note], velocity)
            display_note_on(note)
            self.client.send_note_on(note)
        except Exception as e:
            print(f"Error sending Note On: {e}")

    def send_note_off(self, note):
        """Send a MIDI Note Off message via RTP"""
        try:
            print(f"Note Off: {note}")
            Timer(1.0, self.synth.noteoff, (0, NOTE_TO_NUMBER[note]))
            display_note_off(note)
            self.client.send_note_off(note)
        except Exception as e:
            print(f"Error sending Note Off: {e}")

    def run(self):
        """Main event loop to capture keyboard input and send MIDI messages"""
        # Start RTP MIDI session
        logger.info(f'Connecting to RTP-MIDI server @ {host}:{port} ...')
        self.client.connect(host, port)
        logger.info('Connected!')

        logger.info("Loading SoundFont...")
        sfid = self.synth.sfload("florestan-piano.sf2")
        self.synth.program_select(0, sfid, 0, 0)
        self.synth.start()
        logger.info("SoundFont loaded!")

        running = True
        try:
            while running:
                event_happened = False
                for event in pygame.event.get():
                    event_happened = True
                    if event.type == pygame.QUIT:
                        running = False

                    # Key Down Event
                    if event.type == pygame.KEYDOWN:
                        if event.key in self.key_to_note_map:
                            note = self.key_to_note_map[event.key]
                            if note not in self.active_notes:
                                self.send_note_on(note)
                                self.active_notes.add(note)

                    # Key Up Event
                    if event.type == pygame.KEYUP:
                        if event.key in self.key_to_note_map:
                            note = self.key_to_note_map[event.key]
                            if note in self.active_notes:
                                self.send_note_off(note)
                                self.active_notes.remove(note)

                if event_happened and running:
                    draw_keyboard(self.window)
                    pygame.display.update()
                pygame.time.delay(50)  # Small delay to reduce CPU usage

        except KeyboardInterrupt:
            print("\nStopping RTP MIDI server...")
        finally:
            # Cleanup
            pygame.quit()
            self.synth.stop()


def main():
    simulator = RTPMIDIKeyboardSimulator()
    simulator.run()



if __name__ == "__main__":
    main()
