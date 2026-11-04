#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "layers.h"

void encapsulate_all_layers(const char *input_data, char *output_packet) {
    char temp[BUFFER_SIZE];
    strcpy(temp, input_data);

    printf("\n=== STARTING 7-LAYER OSI ENCAPSULATION (DOWNWARDS) ===\n");
    usleep(200000);

    // Layer 7: Application
    printf("[Layer 7 - Application] Data generated: \"%s\"\n", temp);
    usleep(200000);

    // Layer 6: Presentation
    char l6[BUFFER_SIZE];
    snprintf(l6, sizeof(l6), "[L6_Header:FMT=ASCII|ENC=NONE]%s", temp);
    printf("[Layer 6 - Presentation] Formatted & Encrypted.\n");
    usleep(200000);
    printf("--> Progress: Layers 7 & 6 Encapsulated.\n\n");

    // Layer 5: Session
    char l5[BUFFER_SIZE];
    snprintf(l5, sizeof(l5), "[L5_Header:SESS_ID=7741]%s", l6);
    printf("[Layer 5 - Session] Session token attached.\n");
    usleep(200000);

    // Layer 4: Transport
    char l4[BUFFER_SIZE];
    snprintf(l4, sizeof(l4), "[L4_Header:TCP_SRC=49152|DST=8080]%s", l5);
    printf("[Layer 4 - Transport] Segmented with TCP header.\n");
    usleep(200000);
    printf("--> Progress: Layers 5 & 4 Encapsulated.\n\n");

    // Layer 3: Network
    char l3[BUFFER_SIZE];
    snprintf(l3, sizeof(l3), "[L3_Header:IP=10.0.0.1->10.0.0.2]%s", l4);
    printf("[Layer 3 - Network] Packet routed with IP header.\n");
    usleep(200000);

    // Layer 2: Data Link
    char l2[BUFFER_SIZE];
    snprintf(l2, sizeof(l2), "[L2_Header:MAC=AA:BB:CC->11:22:33]%s[L2_Trailer:FCS=OK]", l3);
    printf("[Layer 2 - Data Link] Framed with MAC address and FCS trailer.\n");
    usleep(200000);
    printf("--> Progress: Layers 3 & 2 Encapsulated.\n\n");

    // Layer 1: Physical
    printf("[Layer 1 - Physical] Converting complete frame to raw electrical/optical bits.\n");
    usleep(200000);
    printf("--> Progress: Layer 1 Encapsulation Complete. Ready for Socket Transmission.\n\n");

    strcpy(output_packet, l2);
}

void decapsulate_all_layers(const char *packet) {
    printf("\n=== STARTING 7-LAYER OSI DECAPSULATION (UPWARDS) ===\n");
    usleep(200000);

    // Layer 1 & 2
    printf("[Layer 1 - Physical] Receiving raw bit signals from network media.\n");
    usleep(200000);
    printf("[Layer 2 - Data Link] Stripping MAC header & FCS trailer. Frame verified.\n");
    usleep(200000);
    printf("--> Progress: Layers 1 & 2 Decapsulated.\n\n");

    // Layer 3 & 4
    printf("[Layer 3 - Network] Stripping IP header. Destination IP verified.\n");
    usleep(200000);
    printf("[Layer 4 - Transport] Stripping TCP header. Reassembling segment/ACK check.\n");
    usleep(200000);
    printf("--> Progress: Layers 3 & 4 Decapsulated.\n\n");

    // Layer 5 & 6
    printf("[Layer 5 - Session] Processing session token synchronization.\n");
    usleep(200000);
    printf("[Layer 6 - Presentation] Translating format and decrypting payload.\n");
    usleep(200000);
    printf("--> Progress: Layers 5 & 6 Decapsulated.\n\n");

    // Layer 7
    printf("[Layer 7 - Application] Delivering final payload to user application process.\n");
    printf(">>> Successfully Decapsulated Payload: \"%s\"\n\n", packet);
}