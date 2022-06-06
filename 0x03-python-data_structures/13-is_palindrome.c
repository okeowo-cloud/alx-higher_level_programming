#include "lists.h"

/**
 * get_length - returns the length of a linkedlist
 * @head: is a pointer to the head of a linkedlist
 * Return: is an integer represent the length of the list
 */
int get_length(listint_t *head)
{
	listint_t *current;

	int i = 0;

	current = head;

	while (current)
	{
		i++;
		current = current->next;
	}
	return (i);
}


/**
 * get_at_index - function get the element of a linkedlist
 * at given index
 * @head: is a pointer to head of linkedlist
 * @n: is the index
 * Return: is an int data in linkedlist
 */
int get_at_index(listint_t *head, int n)
{
	int i, j;

	listint_t *current = head;

	j = get_length(head);

	for (i = 0; i < j; i++)
	{
		if (i == n)
			return (current->n);
		current = current->next;
	}
	return (-1);
}

/**
 * is_palindrome - function checks if a singly linked list is a palindrome.
 * @head: pointer to base of a linkedlist
 * Return: 0 if not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i, j;

	if (head == NULL || *head == NULL)
		return (1);
	i = 0;
	j = get_length(*head) - 1;
	while (i < j)
	{
		if (get_at_index(*head, i) != get_at_index(*head, j))
			return (0);
		i++;
		j--;
	}
	return (1);
}
