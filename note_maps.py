import pygame

KEY_TO_NOTE = {
    pygame.K_a: "C4",    # C3
    pygame.K_w: "Cs4",    # C#3
    pygame.K_s: "D4",    # D3
    pygame.K_e: "Ds4",    # D#3
    pygame.K_d: "E4",    # E3
    pygame.K_f: "F4",    # F3
    pygame.K_t: "Fs4",    # F#3
    pygame.K_g: "G4",    # G3
    pygame.K_y: "Gs4",    # G#3
    pygame.K_h: "A4",    # A3
    pygame.K_u: "As4",    # A#3
    pygame.K_j: "B4",    # B3
    pygame.K_k: "C5",    # C4
    pygame.K_o: "Cs5",    # C#4
    pygame.K_l: "D5",    # D4
    pygame.K_p: "Ds5",    # D#4
    pygame.K_SEMICOLON: "E5",  # E4
    pygame.K_LEFTBRACKET: "Es5",
    pygame.K_QUOTE: "F5"
}


# the pitch number of each note
NOTE_TO_NUMBER = {
    "C0": 12,
    "Cs0": 13,
    "D0": 14,
    "Ds0": 15,
    "E0": 16,
    "F0": 17,
    "Fs0": 18,
    "G0": 19,
    "Gs0": 20,
    "A0": 21,
    "As0": 22,
    "B0": 23,
    "C1": 24,
    "Cs1": 25,
    "D1": 26,
    "Ds1": 27,
    "E1": 28,
    "F1": 29,
    "Fs1": 30,
    "G1": 31,
    "Gs1": 32,
    "A1": 33,
    "As1": 34,
    "B1": 35,
    "C2": 36,
    "Cs2": 37,
    "D2": 38,
    "Ds2": 39,
    "E2": 40,
    "F2": 41,
    "Fs2": 42,
    "G2": 43,
    "Gs2": 44,
    "A2": 45,
    "As2": 46,
    "B2": 47,
    "C3": 48,
    "Cs3": 49,
    "D3": 50,
    "Ds3": 51,
    "E3": 52,
    "F3": 53,
    "Fs3": 54,
    "G3": 55,
    "Gs3": 56,
    "A3": 57,
    "As3": 58,
    "B3": 59,
    "C4": 60,
    "Cs4": 61,
    "D4": 62,
    "Ds4": 63,
    "E4": 64,
    "F4": 65,
    "Fs4": 66,
    "G4": 67,
    "Gs4": 68,
    "A4": 69,
    "As4": 70,
    "B4": 71,
    "C5": 72,
    "Cs5": 73,
    "D5": 74,
    "Ds5": 75,
    "E5": 76,
    "F5": 77,
    "Fs5": 78,
    "G5": 79,
    "Gs5": 80,
    "A5": 81,
    "As5": 82,
    "B5": 83,
    "C6": 84,
    "Cs6": 85,
    "D6": 86,
    "Ds6": 87,
    "E6": 88,
    "F6": 89,
    "Fs6": 90,
    "G6": 91,
    "Gs6": 92,
    "A6": 93,
    "As6": 94,
    "B6": 95,
    "C7": 96,
    "Cs7": 97,
    "D7": 98,
    "Ds7": 99,
    "E7": 100,
    "F7": 101,
    "Fs7": 102,
    "G7": 103,
    "Gs7": 104,
    "A7": 105,
    "As7": 106,
    "B7": 107,
    "C8": 108,
    "Cs8": 109,
    "D8": 110,
    "Ds8": 111,
    "E8": 112
}
