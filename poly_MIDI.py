from midiutil import MIDIFile    
from datetime import datetime


# Parameters
#pitches = [16, 19, 23, 26, 28, 31, 35, 38, 40, 42, 43, 45, 47, 50, 52, 54, 55, 57, 59, 62, 64, 66, 67, 69, 71, 74, 76, 78, 79, 81, 83, 86, 88]  # MIDI notes to use
#pitches = [24, 36, 43, 53, 63, 70, 74, 77, 82, 86, 91]
#pitches = [24, 36, 43, 53, 62, 69, 74, 82, 86]
#pitches = [12, 24, 31, 39, 46, 50, 53, 58, 62, 65, 70, 72, 75]
pitches = [0, 12, 17, 22, 24, 27, 29, 32, 34, 36, 39, 41, 44, 46, 48, 51, 53, 56] 
sweeps = 50  # Number of sweeps
base_note_gap = 2.0  # Gap between the notes at a given pitch usually 2.0 for large notesets
note_length = 0.8  # Duration of each note
slope_factor = 1 # multiplier for number of extra notes (will make the slope more aggressive)
start_offset = 0
#start_offset_increase = 0.1 # increase in start offset for each pitch pair


sequence_duration = sweeps * base_note_gap  # Duration of the whole sequence

note_count = [0] * len(pitches)  # Number of notes to play for each pitch
note_gap_list = [0] * len(pitches)  # Gap between the notes at a given pitch
note_start = [0] * len(pitches)  # Start time of the note

# Create the timing data for each pitch
extra_notes = 0
for i, pitch in enumerate(pitches):
    note_count[i] = int(sequence_duration / base_note_gap) + (slope_factor * extra_notes)
    note_gap_list[i] = sequence_duration / note_count[i]
    extra_notes += 1
    note_start[i] = start_offset 
    

# Create a MIDI file
midi = MIDIFile(1)

# Set the track, time, and tempo
track = 0
time = 0
midi.addTempo(track, time, 100)

# Add notes to the MIDI file
for i, pitch in enumerate(pitches):
    time = 0
    for _ in range(note_count[i]):
        midi.addNote(track, 0, pitch, time, note_length, 100)
        time += note_gap_list[i]

# Generate a timestamp
timestamp = datetime.now().strftime('%H%M%S')

# Construct the new filename with the timestamp
filename = f"super_arpeggio_{timestamp}.mid"

# Save the MIDI file with the new filename
with open(filename, "wb") as output_file:
    midi.writeFile(output_file)
