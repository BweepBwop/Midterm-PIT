# DTMF Signal Generator
Short Demo:

The project is designed to generate Dual-Tone Multi-Frequency (DTMF) signals, simulating the sounds produced by pressing keys on a phone keypad. Each key corresponds to a specific frequency combination, creating unique tones.

# What is used?:

Flask: Used for serving the web-based interface that allows users to interact with the application.
JavaScript: Manages button inputs and facilitates communication between the client and server.
Sounddevice: Generates the DTMF tones in real-time based on the selected keys, providing immediate audio feedback.
UI: Built with Python Flask, the interface employs JavaScript to create an interactive experience, allowing users to select phone keypad keys.
Sound Generation: Utilizes the sounddevice library for real-time audio synthesis based on DTMF frequencies associated with each keypress.
Graph: Visualizes generated signals using Plotly and Plotly Express, featuring both time-domain and frequency-domain graphs for detailed analysis.
Keypad Sound: Each keypress generates the corresponding DTMF tone, replicating an authentic phone keypad experience.

# Necessary Imports and Their Purposes:
Flask, render_template, jsonify, request: For creating the web application and handling HTTP requests
numpy: For numerical operations, including array and mathematical computations
scipy.fft and fftfreq: For performing Fast Fourier Transform (FFT) to analyze the frequency components of signals
plotly.express: For creating interactive and dynamic visualizations of the data
plotly.io: For handling the input/output of Plotly figures
sounddevice: For real-time audio playback of generated DTMF tones

# Libraries:
Plotly: Employed to create dynamic and adjustable graphs for visualizing signal characteristics in both time and frequency domains.
Plotly Express: Used for simplifying the creation of complex visualizations, allowing for easy plotting of the DTMF signals.
