# Polyrhythmic MIDI Sequence Generator

So I heard you like polyrhythmic MIDI sequences? Well, now you can make your own without all that tedious clicking about in Ableton, and they will loop perfectly.

## Features

- Generate polyrhythmic MIDI sequences with customizable parameters
- Create perfectly looping sequences
- Adjust note pitches, durations, and gaps
- Control the number of sweeps and slope aggressiveness
- Automatically generate unique filenames with timestamps

## Requirements

- Python 3.x
- midiutil library

## Installation

1. Clone the repository (or just grab poly_MIDI.py):

   ```
   git clone https://github.com/theeasyway/polyrhythmic.git
   ```

2. Install the required dependencies:

   ```
   pip install midiutil
   ```
## Usage

1. Open the `poly_MIDI.py` file in a text editor.

2. Modify the parameters in the script according to your preferences:
- `pitches`: List of MIDI pitch values for the notes
- `sweeps`: Number of sweeps in the sequence
- `base_note_gap`: Gap between the notes at a given pitch
- `note_length`: Duration of each note
- `slope_factor`: Multiplier for the number of extra notes (affects slope aggressiveness)
- `start_offset`: Start offset for the first pitch
- `start_offset_increase`: Increase in start offset for each pitch pair

3. Save the changes to the script.

4. Run the script:
    ```
    python poly_MIDI.py
    ```
5. The generated MIDI file will be saved in the same directory as the script, with a unique filename based on the current timestamp.

## Example

See the /examples folder for .mid and .mp3 examples.

## Additional Utility

The repository also includes a utility script `note_to_pitch.py` that converts musical note names to their corresponding MIDI pitches. This can be helpful when working with specific note sequences in your polyrhythmic MIDI sequences.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The midiutil library for simplifying MIDI file creation in Python.
