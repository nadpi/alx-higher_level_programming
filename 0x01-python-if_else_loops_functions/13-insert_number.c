#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: head
 * @number: number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;
	listint_t *temp;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while(current->next && number > current->next->n)
	{
		current = current->next;
	}
	temp = current->next;
	current->next = new;
	new->next = temp;
	return (new);
}
