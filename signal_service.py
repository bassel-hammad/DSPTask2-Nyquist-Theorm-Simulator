import numpy as np
import pandas as pd


def extract_fmax_from_csv(df, time_series):
    """Extract max frequency from CSV metadata or estimate from time spacing."""
    if 'Fmax' in df.columns:
        fmax_values = pd.to_numeric(df['Fmax'], errors='coerce').dropna()
        if not fmax_values.empty:
            return float(fmax_values.iloc[0])

    if df.shape[1] >= 3:
        legacy_values = pd.to_numeric(df.iloc[:, 2], errors='coerce').dropna()
        if not legacy_values.empty:
            return float(legacy_values.iloc[0])

    time_values = np.asarray(time_series, dtype=float)
    if len(time_values) < 2:
        return 0.0

    dt = np.diff(time_values)
    dt = dt[dt > 0]
    if dt.size == 0:
        return 0.0

    sampling_rate = 1.0 / np.median(dt)
    return float(sampling_rate / 2.0)


def sum_sine_waves(sine_waves, sample_count):
    """Return summed waveform and maximum frequency for active sine waves."""
    if not sine_waves:
        return np.zeros(sample_count), 0.0

    max_frequency = 0.0
    y_summed = np.zeros_like(sine_waves[0].Yaxis)

    for sine_wave in sine_waves:
        max_frequency = max(max_frequency, sine_wave.get_frequency())
        y_summed += sine_wave.Yaxis

    return y_summed, max_frequency
