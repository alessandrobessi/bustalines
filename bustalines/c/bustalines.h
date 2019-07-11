#ifndef BUSTALINES_H
#define BUSTALINES_H

unsigned long int get_file_size(const char *filename);

struct Map *create_map(const char *filename);

int remove_map(struct Map *map);

void print_line(struct Map *map, int index);

char *get_line(struct Map *map, int index);

unsigned long int get_map_len(struct Map *map);

struct Map {
    unsigned long int count;
    unsigned long int filesize;
    char *begin;
    char **map;
};

#endif
