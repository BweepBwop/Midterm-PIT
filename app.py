from flask import Flask, render_template, jsonify, request
import numpy as np
from scipy.fft import fft, fftfreq
import plotly.express as px  
import plotly.io as pio
import sounddevice as sd

app = Flask(__name__)

dtmf_frequencies = {
    '1': (697, 1209), '2': (697, 1336), '3': (697, 1477),
    '4': (770, 1209), '5': (770, 1336), '6': (770, 1477),
    '7': (852, 1209), '8': (852, 1336), '9': (852, 1477),
    '*': (941, 1209), '0': (941, 1336), '#': (941, 1477)
}

def generate_dtmf_tone(key, duration=0.5, fs=8000):
    f_low, f_high = dtmf_frequencies[key]
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    low_signal = np.sin(2 * np.pi * f_low * t)
    high_signal = np.sin(2 * np.pi * f_high * t)
    signal = np.add(low_signal, high_signal)
    return signal, t, f_low, f_high

def compute_fft(signal, fs):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / fs)[:N // 2]
    magnitude = np.abs(yf[:N // 2]) * (2.0 / N)
    return xf, magnitude

def play_sound(signal, fs=8000):
    sd.play(signal, samplerate=fs)
    sd.wait()

def create_plotly_plot(x, y, title, x_label, y_label):
    fig = px.line(x=x, y=y, labels={'x': x_label, 'y': y_label}, title=title)
    return pio.to_json(fig)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play_key', methods=['POST'])
def play_key():
    key = request.json.get('key')
    signal, _, f_low, f_high = generate_dtmf_tone(key)
    play_sound(signal)
    return jsonify({
        "status": "success",
        "message": f"Playing sound for key {key}",
        "frequencies": (f_low, f_high)
    })

@app.route('/analyze_key', methods=['POST'])
def analyze_key():
    key = request.json.get('key')
    signal, t, f_low, f_high = generate_dtmf_tone(key)
    fs = 8000

    xf, magnitude = compute_fft(signal, fs)

    time_domain_plot = create_plotly_plot(
        t[:100], signal[:100], f"Time-Domain Signal for Key '{key}'", "Time [s]", "Amplitude"
    )
    freq_domain_plot = create_plotly_plot(
        xf, magnitude, f"Frequency-Domain Spectrum for Key '{key}'", "Frequency [Hz]", "Magnitude"
    )

    low_signal = np.sin(2 * np.pi * f_low * t)
    high_signal = np.sin(2 * np.pi * f_high * t)
    combined_signal = (low_signal + high_signal) / 2

    combined_plot = pio.to_json(
        px.line(
            x=t[:200],
            y=[low_signal[:200], high_signal[:200], combined_signal[:200]],
            labels={'x': 'Time [s]', 'y': 'Amplitude'},
            title=f"Sine Wave Representation for Key '{key}'",
            line_shape='linear'
        )
    )

    identified_keys = [k for k, v in dtmf_frequencies.items() if v == (f_low, f_high)]

    return jsonify({
        'time_domain_plot': time_domain_plot,
        'freq_domain_plot': freq_domain_plot,
        'combined_plot': combined_plot,
        'identified_key': identified_keys,
        'frequencies': (f_low, f_high)
    })

if __name__ == '__main__':
    app.run(debug=True)
