# DTMF Signal Generator

This project is designed to generate Dual-Tone Multi-Frequency (DTMF) signals, simulating the sounds produced by pressing keys on a phone keypad. Each key corresponds to a unique frequency combination, producing distinct tones.

## Features

- **DTMF Signal Generation**: Real-time audio synthesis using DTMF frequencies for each keypress.
- **Interactive Web Interface**: Built using Python Flask with JavaScript for handling button inputs.
- **Graph Visualization**: Displays both time-domain and frequency-domain analysis of the generated signals using Plotly.
- **Real-Time Sound**: Replicates the authentic phone keypad experience by generating corresponding DTMF tones for each key.

## Technologies Used

- **Flask**: Serves the web interface, allowing users to interact with the application.
- **JavaScript**: Manages the button inputs and communicates with the backend for an interactive experience.
- **Sounddevice**: Generates DTMF tones in real-time based on key selections.
- **Plotly & Plotly Express**: Used to visualize the generated signals, featuring both time-domain and frequency-domain analysis.

## How It Works

1. **Web-Based Interface**: The interface allows users to select keys from a virtual keypad, which corresponds to phone keypad tones.
2. **Real-Time Sound Generation**: Upon keypress, the corresponding DTMF tone is generated using the `sounddevice` library.
3. **Signal Visualization**: Plotly is employed to create dynamic graphs to analyze the signal in both the time and frequency domains.

## Necessary Imports and Their Purposes

- `Flask`, `render_template`, `jsonify`, `request`: For creating the web application and handling HTTP requests.
- `numpy`: For numerical operations such as array manipulation and mathematical computations.
- `scipy.fft`, `fftfreq`: Used to perform Fast Fourier Transform (FFT) for analyzing frequency components of the signals.
- `plotly.express`, `plotly.io`: For creating interactive visualizations and managing the input/output of Plotly figures.
- `sounddevice`: For real-time audio playback of the generated DTMF tones.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dtmf-signal-generator.git
   cd dtmf-signal-generator
