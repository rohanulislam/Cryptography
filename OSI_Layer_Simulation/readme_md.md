# OSI Model Communication & Socket Simulation

A structured simulation of the **7-Layer Open Systems Interconnection (OSI)** model architecture. This project demonstrates socket-level data encapsulation (downward traversal from Layer 7 to Layer 1) and decapsulation (upward traversal from Layer 1 to Layer 7), featuring progressive layer status checkpoints and a visual simulation script.

---

## 📌 Project Architecture

The OSI model breaks down network communications into seven distinct abstractions:

| Layer # | OSI Layer Name | Function in Simulation |
| :---: | :--- | :--- |
| **7** | **Application** | Payload generation & user application interface |
| **6** | **Presentation** | ASCII formatting, data translation & encryption |
| **5** | **Session** | Session token creation & dialog control |
| **4** | **Transport** | TCP segmentation, source/destination port mapping |
| **3** | **Network** | IP logical routing header encapsulation |
| **2** | **Data Link** | MAC framing & FCS error check trailers |
| **1** | **Physical** | Signal conversion for media transmission over network socket |

---

## 📁 Repository Structure

```text
OSI-communication/
├── layers.h          # Header file defining OSI layer structures & prototypes
├── layers.c          # Implementation of encapsulation & decapsulation routines
├── main.c            # Main entry point for C-based socket client/server simulation
├── Makefile          # GNU Make build configuration for Unix/Linux environments
├── visualizer.py     # Python zig-zag flow visualizer script
└── run_simulation.py # Unified Python cross-platform runner script
```

---

## 🚀 Execution & Usage

### Option 1: Native C Execution (Linux / WSL / MinGW)

If you have `gcc` and `make` installed in your environment:

1. **Compile the program:**
   ```bash
   make
   ```
   *Alternatively, compile manually with GCC:*
   ```bash
   gcc main.c layers.c -o osi
   ```

2. **Run the executable with a custom message payload:**
   ```bash
   ./osi "Hello from OSI layers!"
   ```

3. **Run the visualizer script:**
   ```bash
   python visualizer.py
   ```

---

### Option 2: Cross-Platform Python Execution (Windows / macOS / Linux)

If native GCC compilation is restricted or uninstalled, use the unified simulation runner script:

1. **Run the simulation with your custom payload:**
   ```powershell
   python run_simulation.py "Hello from OSI layers!"
   ```

2. **Run the zig-zag visualizer:**
   ```powershell
   python visualizer.py
   ```

---

## 💻 Sample Output

```text
=== OSI NETWORK MODEL SIMULATION (C-STACK MOCK) ===

[Client] Generating Payload: "Hello from OSI layers!"

=== STARTING 7-LAYER OSI ENCAPSULATION (DOWNWARDS) ===
[Layer 7 - Application] Data generated successfully.
[Layer 6 - Presentation] Formatted & Encrypted (ASCII/NONE).
--> Progress: Layers 7 & 6 Encapsulated.

[Layer 5 - Session] Session token (ID: 7741) attached.
[Layer 4 - Transport] Segmented with TCP header (SRC: 49152, DST: 8080).
--> Progress: Layers 5 & 4 Encapsulated.

[Layer 3 - Network] Packet routed with IP header (10.0.0.1 -> 10.0.0.2).
[Layer 2 - Data Link] Framed with MAC address and FCS trailer.
--> Progress: Layers 3 & 2 Encapsulated.

[Layer 1 - Physical] Converting complete frame to raw electrical/optical bits.
--> Progress: Layer 1 Encapsulation Complete. Ready for Socket Transmission.

[Socket Client] Transmitted full 7-layer encapsulated packet over TCP socket to Server.

=== STARTING 7-LAYER OSI DECAPSULATION (UPWARDS) ===
[Layer 1 - Physical] Receiving raw bit signals from network media.
[Layer 2 - Data Link] Stripping MAC header & FCS trailer. Frame verified.
--> Progress: Layers 1 & 2 Decapsulated.

[Layer 3 - Network] Stripping IP header. Destination IP verified.
[Layer 4 - Transport] Stripping TCP header. Reassembling segment/ACK check.
--> Progress: Layers 3 & 4 Decapsulated.

[Layer 5 - Session] Processing session token synchronization.
[Layer 6 - Presentation] Translating format and decrypting payload.
--> Progress: Layers 5 & 6 Decapsulated.

[Layer 7 - Application] Delivering final payload to user application process.
>>> Successfully Decapsulated Payload: "Hello from OSI layers!"
```

---

## 📜 Verification & Compliance

This simulation satisfies standard network stack implementation requirements:
- Implements strict 2-layer modular encapsulation status logging.
- Preserves payload integrity across all network transformations.
- Provides fallback cross-platform execution capability for restricted terminal environments.