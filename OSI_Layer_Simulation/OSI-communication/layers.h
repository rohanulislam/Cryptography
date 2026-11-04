#ifndef LAYERS_H
#define LAYERS_H

#define BUFFER_SIZE 2048

void encapsulate_all_layers(const char *input_data, char *output_packet);
void decapsulate_all_layers(const char *packet);

#endif