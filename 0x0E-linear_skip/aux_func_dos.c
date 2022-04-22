#include <stdlib.h>
#include "search.h"
/**
 * free_skiplist - asfasd
 * @list: asdf
 */
void free_skiplist(skiplist_t *list)
{
	skiplist_t *node;

	if (list)
	{
		node = list->next;
		free(list);
		free_skiplist(node);
	}
}

/**
 * print_skiplist - asdf
 * @list: asdf
 */
void print_skiplist(const skiplist_t *list)
{
	const skiplist_t *node;

	printf("List :\n");
	for (node = list; node; node = node->next)
	{
		printf("Index[%lu] = [%d]\n", node->index, node->n);
	}
	printf("\nExpress lane :\n");
	for (node = list; node; node = node->express)
	{
		printf("Index[%lu] = [%d]\n", node->index, node->n);
	}
	printf("\n");
}
