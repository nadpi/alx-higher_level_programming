#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int flag = 1, j = 0, count = 0, k, i;
	listint_t *curr = *head, *check = *head, *hold = *head;

	if (curr != NULL)
		return (1);
	while (curr != NULL)
	{
		count++;
		curr = curr->next;
	}

	curr = *head;
	for (k = 0; k < count / 2; k++)
	{
		hold = hold->next;
	}

	for (j = 0; j < count / 2; j++)
	{
		check = hold;
		for (i = count / 2; i < count - j - 1; i++)
		{
			check = check->next;
		}
		if (curr->n != check->n)
		{
			flag = 0;
			break;
		}
		curr = curr->next;
	}
	return (flag);
}
