#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <complex>
#include <random>

const double PI = 3.141592653589793;
const double SAMPLE_RATE = 10000.0;
const double DURATION = 1.0;

std::vector<std::complex<double>> gen_dpf(const std::vector<double>& signal) {
    int N = signal.size();
    std::vector<std::complex<double>> dpf(N);

    for (int k = 0; k < N; ++k) {
        std::complex<double> sum(0, 0);
        for (int n = 0; n < N; ++n) {
            double angle = 2 * PI * k * n / N;
            sum += signal[n] * std::complex<double>(cos(angle), -sin(angle));
        }
        dpf[k] = sum;
    }

    return dpf;
}

void dpf_to_csv(const std::vector<std::complex<double>>& dpff, const std::string& name) {
    std::ofstream file(name);
    for (size_t i = 0; i < dpff.size(); ++i) {
        double amplitude = std::abs(dpff[i]);
        double frequency = i * SAMPLE_RATE / dpff.size();
        file << frequency << "," << amplitude << "\n";
    }
    file.close();
}

void signal_to_csv(const std::vector<double>& signal, const std::string& name) {
    std::ofstream file(name);
    for (size_t i = 0; i < signal.size(); ++i) {
        file << i / SAMPLE_RATE << "," << signal[i] << "\n";
    }
    file.close();
}

std::vector<double> gen_signal(const std::vector<double>& frequencies, const std::vector<double>& amplitudes) {
    int cnt = static_cast<int>(SAMPLE_RATE * DURATION);
    std::vector<double> signal(cnt, 0.0);

    for (size_t i = 0; i < frequencies.size(); ++i) {
        for (int t = 0; t < cnt; ++t) {
            signal[t] += amplitudes[i] * cos(2 * PI * frequencies[i] * t / SAMPLE_RATE);
        }
    }

    return signal;
}

std::vector<double> add_noise(const std::vector<double>& signal, double noise_level = 1.2) {
    std::vector<double> noise_signal = signal;
    std::default_random_engine generator;
    std::normal_distribution<double> distribution(0.0, noise_level);

    for (size_t i = 0; i < signal.size(); ++i) {
        noise_signal[i] += distribution(generator);
    }

    return noise_signal;
}

int main() {
    std::vector<double> f1 = {100};
    std::vector<double> a1 = {1};

    std::vector<double> f2 = {100, 300, 700};
    std::vector<double> a2 = {1, 1, 1};

    std::vector<double> f3 = {100, 300, 700};
    std::vector<double> a3 = {3, 2, 1};

    auto signal1 = gen_signal(f1, a1);
    auto signal2 = gen_signal(f2, a2);
    auto signal3 = gen_signal(f3, a3);

    signal_to_csv(signal1, "signal1.csv");
    signal_to_csv(signal2, "signal2.csv");
    signal_to_csv(signal3, "signal3.csv");

    auto fft1 = gen_dpf(signal1);
    auto fft2 = gen_dpf(signal2);
    auto fft3 = gen_dpf(signal3);

    dpf_to_csv(fft1, "dpf_signal1.csv");
    dpf_to_csv(fft2, "dpf_signal2.csv");
    dpf_to_csv(fft3, "dpf_signal3.csv");

    auto noisy_signal1 = add_noise(signal1);
    auto noisy_signal2 = add_noise(signal2);
    auto noisy_signal3 = add_noise(signal3);

    signal_to_csv(noisy_signal1, "noisy_signal1.csv");
    signal_to_csv(noisy_signal2, "noisy_signal2.csv");
    signal_to_csv(noisy_signal3, "noisy_signal3.csv");

    auto fft_noisy1 = gen_dpf(noisy_signal1);
    auto fft_noisy2 = gen_dpf(noisy_signal2);
    auto fft_noisy3 = gen_dpf(noisy_signal3);

    dpf_to_csv(fft_noisy1, "dpf_noisy_signal1.csv");
    dpf_to_csv(fft_noisy2, "dpf_noisy_signal2.csv");
    dpf_to_csv(fft_noisy3, "dpf_noisy_signal3.csv");

}
