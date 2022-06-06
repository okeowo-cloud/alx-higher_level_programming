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
 * is_palindrome - function checks if a singly linked list is a palindrome.
 * @head: pointer to base of a linkedlist
 * Return: 0 if not a palindrome, 1 otherwise
 */
int is_palindrome(listint_t **head)
{
	int i, j, *arr;

	listint_t *current = *head;

	if (head == NULL || *head == NULL)
		return (1);
	i = 0;
	arr = malloc(sizeof(int) * get_length(*head));
	if (!arr)
		return (0);
	while (current)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	j = 0;
	i--;
	while (j < i)
	{
		if (arr[j] != arr[i])
			return (0);
		i--;
		j++;
	}
	free(arr);
	return (1);
}
