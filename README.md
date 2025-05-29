# 🌊 Underwater Acoustic Transmission Loss Simulation using ARLpy + Bellhop

This project uses **ARLpy** and **Bellhop** to simulate underwater acoustic transmission loss in three different ocean environments, both with and without ray tracing.

## 📦 Requirements
- Python 3.x
- ARLpy (`pip install arlpy`)
- Bellhop (install from http://oalib.hlsresearch.com/AcousticsToolbox/)
  - Add `bellhop.exe` to your system PATH

## 📁 Files
- `compare_envs.py` : Main simulation script
- `README.md` : Documentation and usage guide

## ▶️ How to Run
1. Install dependencies:
   ```
   pip install arlpy matplotlib numpy
   ```
2. Run the script:
   ```
   python compare_envs.py
   ```

## 📈 Output
A single plot showing transmission loss vs. range for three environments, with and without ray tracing.
