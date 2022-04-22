#include "sort.h"

void swich(int *array, int *a, int *b, int size);
void high(int *array, int n, int i, int size);

/**
 * heap_sort - sorts an array of integers in ascending
 * order using the Heap sort algorithm
 * @array: array to sort
 * @size: size of array
 */
void heap_sort(int *array, size_t size)
{
	size_t i;

	if (!array)
		return;

	for (i = size / 2; i > 0; i--)
		high(array, size, i - 1, size);

	for (i = size - 1; i > 0; i--)
	{
		swich(array, &array[0], &array[i], size);
		high(array, i, 0, size);
	}
}

/**
 * swich - asdafs
 * @a: asfda
 * @b: asfad
 * @array: adfasf
 * @size: asd
 */
void swich(int *array, int *a, int *b, int size)
{
	int temp;

	temp = *a;
	*a = *b;
	*b = temp;

	print_array(array, size);
}

/**
 * high - asdasf
 * @array: asfsfq
 * @n: asdfaq
 * @i: asffq
 * @size: asdqd
 */
void high(int *array, int n, int i, int size)
{
	int largest, left, right;

	largest = i;
	left = (2 * i) + 1;
	right = (2 * i) + 2;

	if (left < n && array[left] > array[largest])
		largest = left;

	if (right < n && array[right] > array[largest])
		largest = right;

	if (largest != i)
	{
		swich(array, &array[i], &array[largest], size);
		high(array, n, largest, size);
	}
}
