import time
import sys

def simulate_zigzag():
    print("\n" + "="*60)
    print(" Python Zig-Zag Visualizer: Linux Network Stack Flow ")
    print("="*60 + "\n")

    layers = [
        ("Layer 7: Application", "User data generation"),
        ("Layer 6: Presentation", "Encryption & format translation"),
        ("Layer 5: Session", "Session establishment & token tracking"),
        ("Layer 4: Transport", "TCP segmentation & port mapping"),
        ("Layer 3: Network", "IP logical routing & packet headers"),
        ("Layer 2: Data Link", "MAC framing & FCS error trailers"),
        ("Layer 1: Physical", "Electrical signal transmission over media")
    ]

    print("--- [ ENCAPSULATION PHASE (Downwards) ] ---")
    for i in range(0, len(layers), 2):
        print(f"v-- Encapsulating [{layers[i][0]}] -> {layers[i][1]}")
        time.sleep(0.3)
        if i + 1 < len(layers):
            print(f"v-- Encapsulating [{layers[i+1][0]}] -> {layers[i+1][1]}")
            time.sleep(0.3)
        print(f"    [Progress Check]: Layers up to {i+2} successfully encapsulated.\n")

    print("[ Transmitting packet across network socket medium... ]\n")

    print("--- [ DECAPSULATION PHASE (Upwards) ] ---")
    for i in range(len(layers)-1, -1, -2):
        print(f"^-- Decapsulating [{layers[i][0]}]")
        time.sleep(0.3)
        if i - 1 >= 0:
            print(f"^-- Decapsulating [{layers[i-1][0]}]")
            time.sleep(0.3)
        print(f"    [Progress Check]: Layers stripped up to {layers[max(i-1, 0)][0]}.\n")

    print("=== OSI Zig-Zag Simulation Complete ===\n")

if __name__ == "__main__":
    simulate_zigzag()