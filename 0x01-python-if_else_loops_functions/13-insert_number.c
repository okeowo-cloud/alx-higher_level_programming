#include "lists.h"

/**
 * insert_node - function inserts a number into a sorted singly linked list.
 * @head: is a pointer to the base of linkedlist
 * @n: is an integer
 * Return: is a pointer to inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	node = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
