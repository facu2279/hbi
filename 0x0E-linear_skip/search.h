#ifndef _SEARCH_H
#define _SEARCH_H

#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>
#include <stdint.h>
#include <math.h>
/**
 * struct skiplist_s - asdfsad
 * @n: adsf
 * @index: adsf
 * @next: adsf
 * @express: sadf
 */
typedef struct skiplist_s
{
	int n;
	size_t index;
	struct skiplist_s *next;
	struct skiplist_s *express;
} skiplist_t;

skiplist_t *create_skiplist(int *array, size_t size);
void free_skiplist(skiplist_t *list);
void print_skiplist(const skiplist_t *list);
skiplist_t *linear_skip(skiplist_t *list, int value);
#endif
