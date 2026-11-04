import time
import sys

def simulate_c_osi_layers(message):
    print("=== OSI NETWORK MODEL SIMULATION (C-STACK MOCK) ===")
    time.sleep(0.5)
    print(f"\n[Client] Generating Payload: \"{message}\"")
    
    print("\n=== STARTING 7-LAYER OSI ENCAPSULATION (DOWNWARDS) ===")
    time.sleep(0.3)
    print("[Layer 7 - Application] Data generated successfully.")
    time.sleep(0.3)
    print("[Layer 6 - Presentation] Formatted & Encrypted (ASCII/NONE).")
    print("--> Progress: Layers 7 & 6 Encapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 5 - Session] Session token (ID: 7741) attached.")
    time.sleep(0.3)
    print("[Layer 4 - Transport] Segmented with TCP header (SRC: 49152, DST: 8080).")
    print("--> Progress: Layers 5 & 4 Encapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 3 - Network] Packet routed with IP header (10.0.0.1 -> 10.0.0.2).")
    time.sleep(0.3)
    print("[Layer 2 - Data Link] Framed with MAC address and FCS trailer.")
    print("--> Progress: Layers 3 & 2 Encapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 1 - Physical] Converting complete frame to raw electrical/optical bits.")
    print("--> Progress: Layer 1 Encapsulation Complete. Ready for Socket Transmission.\n")
    time.sleep(0.5)
    print("[Socket Client] Transmitted full 7-layer encapsulated packet over TCP socket to Server.\n")

def simulate_decapsulation(message):
    print("=== STARTING 7-LAYER OSI DECAPSULATION (UPWARDS) ===")
    time.sleep(0.3)
    print("[Layer 1 - Physical] Receiving raw bit signals from network media.")
    time.sleep(0.3)
    print("[Layer 2 - Data Link] Stripping MAC header & FCS trailer. Frame verified.")
    print("--> Progress: Layers 1 & 2 Decapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 3 - Network] Stripping IP header. Destination IP verified.")
    time.sleep(0.3)
    print("[Layer 4 - Transport] Stripping TCP header. Reassembling segment/ACK check.")
    print("--> Progress: Layers 3 & 4 Decapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 5 - Session] Processing session token synchronization.")
    time.sleep(0.3)
    print("[Layer 6 - Presentation] Translating format and decrypting payload.")
    print("--> Progress: Layers 5 & 6 Decapsulated.\n")
    time.sleep(0.3)
    
    print("[Layer 7 - Application] Delivering final payload to user application process.")
    print(f">>> Successfully Decapsulated Payload: \"{message}\"\n")

if __name__ == "__main__":
    msg = "Hello from OSI layers!"
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    
    simulate_c_osi_layers(msg)
    time.sleep(0.5)
    simulate_decapsulation(msg)