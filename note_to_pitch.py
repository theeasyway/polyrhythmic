# Script: note_to_midi_conversion.py
#
# Description:
# This script defines a function 'note_to_midi' that converts musical note names to corresponding MIDI pitches.
# It also includes a list of musical notes in string format and converts each note to its MIDI pitch using the 'note_to_midi' function.
# The resulting MIDI pitches are printed to the console.
#
# Function:
# def note_to_midi(note):
#     Converts a musical note in string format to its corresponding MIDI pitch.
#     The input 'note' should follow the format "<NoteName><Octave>", e.g., "C4" for middle C.
#     Returns the MIDI pitch value as an integer.
#
# Usage:
# Run the script to convert a list of musical notes to MIDI pitches and display the results.
# Adjust the 'notes' list as needed to include different musical notes for conversion.

def note_to_midi(note):
    note_to_index = {
        "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
        "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9,
        "A#": 10, "Bb": 10, "B": 11
    }
    octave = int(note[-1])
    note_name = note[:-1]
    midi_pitch = note_to_index[note_name] + (octave - 1) * 12
    return midi_pitch

#notes = ["E1", "B1", "E2", "G2", "B2", "D3", "E3", "G3", "B3", "D4", "E4", "F#4", "G4", "A4", "B4", "D5", "E5", "F#5", "G5", "A5", "B5", "D6", "E6", "F#6", "G6", "A6", "B6", "D7", "E7", "F#7", "G7", "A7", "B7", "D8", "E8"]
#notes = ["C2", "C3", "G3", "D#4", "A#4", "D5", "F5", "A#5", "D6", "F6", "A#6", "C7", "D#7"]
notes = ["C1", "G1", "C2", "G2","D#2", "A#3", "C3",  "G3", "D#3","A#4", "C4", "D4", "D#4", "F4", "G4", "A#5", "C5", "D5", "D#5", "F5", "G5", "A#6", "C6", "D6", "D#6", "F6", "G6", "A#7", "C7", "D7", "D#7", "F7", "G7", "A#8", "C8"]
midi_pitches = [note_to_midi(note) for note in notes]

print(midi_pitches)



