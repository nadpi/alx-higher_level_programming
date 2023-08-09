#include "lists.h"
/**
 * insert_node - inserts a node into a sorted list
 * @head: head
 * @number: num
 * Return:the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev;
	listint_t *curr = *head;
	listint_t *newnode = malloc(sizeof(listint_t));
	
	if (newnode == NULL)
		return (NULL);

	newnode->n = number;
	if (curr == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	if (curr->next == NULL)
	{
		if (number > curr->n)
		{
			curr->next = newnode;
			return (newnode);
		}
		else
		{
			newnode->next = *head;
			*head = newnode;		
			return (newnode);
		}
	}
	while (curr->next != NULL)
	{
		if (number < curr->n)
		{
			newnode->next = *head;
			*head = newnode;
			return (newnode);
		}
		if (number >= curr->n && number <= curr->next->n)
		{
			prev = curr->next;
			curr->next = newnode;
			newnode->next = prev;
			return (newnode);
		}
		else
			curr = curr->next;
	}
	curr->next = newnode;

	return(newnode);
}
