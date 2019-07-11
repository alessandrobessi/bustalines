#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <assert.h>
#include "bustalines.h"

unsigned long int get_file_size(const char *filename) {
    struct stat st;
    stat(filename, &st);
    unsigned long int filesize = (unsigned long int) st.st_size;
    return filesize;
}

int remove_map(struct Map *map) {
    int rc = munmap(map->begin, map->filesize);
    free(map->map);
    return rc;
}

struct Map *create_map(const char *filename) {

    struct Map *map = (struct Map *) malloc(sizeof(struct Map));
    unsigned long int filesize = get_file_size(filename);
    map->filesize = filesize;
    printf("Mapping %s (%li bytes)\n", filename, filesize);
    int fd = open(filename, O_RDONLY, 0);
    assert(fd != -1);

    char *data = (char *) mmap(NULL, filesize, PROT_READ, MAP_PRIVATE | MAP_POPULATE, fd, 0);
    assert(data != MAP_FAILED);
    close(fd);

    int count = 0;
    char ch;
    char *begin = data;
    char *end = data + filesize;
    while (data < end) {
        ch = *data++;
        if (ch == '\n') {
            count++;
        }
    }

    printf("Number of lines = %d\n", count);

    char **m = (char **) malloc(sizeof(char *) * count);
    data = begin;
    int len = 0;
    count = 0;
    while (data < end) {
        ch = *data++;
        if (ch == '\n') {
            m[count] = data - len - 1;
            // printf("Line %d len = %d, memory address = %p\n", count, len, data - len - 1);
            count++;
            len = 0;
        } else {
            len++;
        }
    }

    map->begin = begin;
    map->map = m;
    map->count = count;

    return map;
}

void print_line(struct Map *map, int index) {
    printf("\nLine %d\n", index);
    char *ch = map->map[index];
    while (*ch != '\n') {
        printf("%c", *ch);
        ch++;
    }
}

char *get_line(struct Map *map, int index) {

    assert(index < map->count);

    char *ch = map->map[index];
    char *ptr = map->map[index];
    int len = 0;
    while (*ch != '\n') {
        ch++;
        len++;
    }
    char *line = malloc(sizeof(char) * len);
    for (int i = 0; i < len; i++) {
        line[i] = *ptr;
        ptr++;
    }
    return line;
}

unsigned long int get_map_len(struct Map *map) {
    return map->count;
}
