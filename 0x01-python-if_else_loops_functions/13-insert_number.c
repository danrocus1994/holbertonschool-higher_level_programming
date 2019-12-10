#include <stdlib.h>
#include "lists.h"
/**
 *insert_node - insert a node
 *@head: the head
 *@number: the number
 *Return: the pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *l = *head;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	while (l != NULL)
	{
		if (l->n < number && l->next && l->next->n > number)
		{
			newnode->next = l->next;
			l->next = newnode;
			return (newnode);
		}
		l = l->next;
	}
	return (NULL);
}
