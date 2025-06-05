import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_signal(signal_data, title):
    plt.plot(signal_data["time"], signal_data["amplitude"])
    plt.title(title)
    plt.xlabel('Время (сек)')
    plt.ylabel('Амплитуда')
    plt.grid(True)

def plot_fft(fft_data, title):
    plt.plot(fft_data["frequency"], fft_data["amplitude"])
    plt.title(title)
    plt.xlabel('Частота (Гц)')
    plt.ylabel('Амплитуда')
    plt.grid(True)

signal1 = pd.read_csv("signal1.csv", header=None, names=["time", "amplitude"])
signal2 = pd.read_csv("signal2.csv", header=None, names=["time", "amplitude"])
signal3 = pd.read_csv("signal3.csv", header=None, names=["time", "amplitude"])

fft_signal1 = pd.read_csv("dpf_signal1.csv", header=None, names=["frequency", "amplitude"])
fft_signal2 = pd.read_csv("dpf_signal2.csv", header=None, names=["frequency", "amplitude"])
fft_signal3 = pd.read_csv("dpf_signal3.csv", header=None, names=["frequency", "amplitude"])

noisy_signal1 = pd.read_csv("noisy_signal1.csv", header=None, names=["time", "amplitude"])
noisy_signal2 = pd.read_csv("noisy_signal2.csv", header=None, names=["time", "amplitude"])
noisy_signal3 = pd.read_csv("noisy_signal3.csv", header=None, names=["time", "amplitude"])

fft_noisy_signal1 = pd.read_csv("dpf_noisy_signal1.csv", header=None, names=["frequency", "amplitude"])
fft_noisy_signal2 = pd.read_csv("dpf_noisy_signal2.csv", header=None, names=["frequency", "amplitude"])
fft_noisy_signal3 = pd.read_csv("dpf_noisy_signal3.csv", header=None, names=["frequency", "amplitude"])

plt.figure(figsize=(25, 12))

plt.subplot(3, 2, 1)
plot_signal(signal1, "Signal 1")

plt.subplot(3, 2, 3)
plot_signal(signal2, "Signal 2")

plt.subplot(3, 2, 5)
plot_signal(signal3, "Signal 3")

plt.subplot(3, 2, 2)
plot_fft(fft_signal1, "DPF Signal 1")

plt.subplot(3, 2, 4)
plot_fft(fft_signal2, "DPF Signal 2")

plt.subplot(3, 2, 6)
plot_fft(fft_signal3, "DPF Signal 3")

plt.tight_layout()
plt.show()

plt.figure(figsize=(25, 12))

plt.subplot(3, 2, 1)
plot_signal(noisy_signal1, "Noisy Signal 1")

plt.subplot(3, 2, 3)
plot_signal(noisy_signal2, "Noisy Signal 2")

plt.subplot(3, 2, 5)
plot_signal(noisy_signal3, "Noisy Signal 3")

plt.subplot(3, 2, 2)
plot_fft(fft_noisy_signal1, "DPF Noisy Signal 1")

plt.subplot(3, 2, 4)
plot_fft(fft_noisy_signal2, "DPF Noisy Signal 2")

plt.subplot(3, 2, 6)
plot_fft(fft_noisy_signal3, "DPF Noisy Signal 3")

plt.tight_layout()
plt.show()
