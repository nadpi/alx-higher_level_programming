#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if there is a cycle or not
 * @list: linked list to check
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current->next != NULL)
	{
		if (current->next->n == list->n)
			return (1);

		current = current->next;
	}

	return (0);
}
