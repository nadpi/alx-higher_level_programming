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

	while (current->next != NULL)
	{
		if (current->next->n == list->n && current->next->next == list->next)
			return (1);
		current = current->next;
	}
	return (0);
}
/**
 * check_if - checks if node value was in the previous nodes
 * @head: head
 * Return: 0 or 1
 */
int check_if(listint_t *head, listint_t *current)
{
	listint_t *temp = head;

	while (current != temp)
	{
		if (current->n == temp->n)
			return (1);
		temp = temp->next;
	}
	return (0);
}
