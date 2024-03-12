#include "lists.h"
/**
 * check_cycle - a function in C that checks if
 * a singly linked list has a cycle in it.
 * @list: head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (list)
	{
		while (current->next != NULL)
		{
			if (current->next->n == list->n && current->next->next == list->next)
				return (1);
			current = current->next;
		}
	}
	return (0);
}
