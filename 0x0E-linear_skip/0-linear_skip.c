#include "search.h"
/**
 * print_index - sdfasd
 * @index: asdfasd
 * @value: sadfsa
 * Return: Nothing
 */
static void print_index(int index, int value)
{
	printf("Value checked at index [%d] = [%d]\n", index, value);
}

/**
 * print_between - asdf
 * @index_1: sadf
 * @index_2: sadfd
 */
static void print_between(int index_1, int index_2)
{
	printf("Value found between indexes [%d] and [%d]\n", index_1, index_2);
}

/**
 * linear_skip - asdfsd
 * @list: asdf
 * @value: asdfsa
 * Return: asdfs
 */
skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *tmp = NULL;
	size_t i = 0;

	if (!list)
		return (NULL);
	if (list->n == value)
		return (list);
	while (value > list->n && list->express)
	{
		tmp = list;
		list = list->express;
		print_index(list->index, list->n);
	}
	if (value <= list->n)
	{
		print_between(tmp->index, list->index);
		for (i = tmp->index; i < list->index; i++)
		{
			print_index(tmp->index, tmp->n);
			if (value == tmp->n)
				return (tmp);
			tmp = tmp->next;
		}
	}
	if (value >= list->n)
	{
		tmp = list;
		while (tmp->next)
			tmp = tmp->next;
		print_between(list->index, tmp->index);
		while (list && value >= list->n)
		{
			print_index(list->index, list->n);
			if (value == list->n)
				return (list);
			list = list->next;
		}
	}
	return (NULL);
}
