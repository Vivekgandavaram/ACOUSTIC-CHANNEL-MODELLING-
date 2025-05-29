from arlpy import acoustics, utils
import matplotlib.pyplot as plt

# -------------------------------
# COMMON PARAMETERS
# -------------------------------
ranges = utils.linspace(0, 5000, 101)
frequency_khz = 50000
tx_depth = 50
rx_depth = [50]

# -------------------------------
# SIMULATION FUNCTION
# -------------------------------
def simulate_env(title, depth, ssp_func, bottom_type):
    env = acoustics.environment(
        depth=depth,
        sound_speed=ssp_func,
        bottom=bottom_type
    )
    tl_basic = acoustics.simulate(
        env=env,
        freq=frequency_khz,
        tx_depth=tx_depth,
        rx_depths=rx_depth,
        ranges=ranges,
        model='bellhop',
        raytrace=False
    )
    tl_ray = acoustics.simulate(
        env=env,
        freq=frequency_khz,
        tx_depth=tx_depth,
        rx_depths=rx_depth,
        ranges=ranges,
        model='bellhop',
        raytrace=True
    )
    return title, tl_basic.transmission_loss[0], tl_ray.transmission_loss[0]

# -------------------------------
# RUN SIMULATIONS
# -------------------------------
results = []

# 1. Shallow Coastal Waters
results.append(simulate_env(
    title='Shallow Coastal (Mud)',
    depth=100,
    ssp_func=lambda z: 1500 + 0.03 * z,
    bottom_type='mud'
))

# 2. Deep Ocean
results.append(simulate_env(
    title='Deep Ocean (Sand)',
    depth=3000,
    ssp_func=lambda z: 1520 - 0.02 * z + 0.00005 * z**2,
    bottom_type='sand'
))

# 3. Estuarine/Harbor
results.append(simulate_env(
    title='Estuary (Silt)',
    depth=30,
    ssp_func=lambda z: 1490 + 0.01 * z,
    bottom_type='silt'
))

# -------------------------------
# PLOT ALL RESULTS
# -------------------------------
plt.figure(figsize=(12, 8))

for title, tl_no_ray, tl_ray in results:
    plt.plot(ranges, tl_no_ray, linestyle='-', linewidth=2, label=f'{title} - No Rays')
    plt.plot(ranges, tl_ray, linestyle='--', linewidth=2, label=f'{title} - Ray Traced')

plt.title("Transmission Loss Comparison - With & Without Ray Tracing")
plt.xlabel("Range (m)")
plt.ylabel("Transmission Loss (dB)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
