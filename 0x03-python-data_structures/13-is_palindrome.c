#include "lists.h"

/**
  * is_palindrome - Function
  * Description: it checks if a list is a palindrome.
  *
  * @head: The pointer to the head of the list.
  *
  * Return: 0 if list not a palindrome, else 1.
  */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int nodes = 0, x = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		nodes++;
		temp = temp->next;
	}
	array = malloc(sizeof(int) * nodes);
	temp = *head;
	while (temp)
	{
		array[x++] = temp->n;
		temp = temp->next;
	}
	for (x = 0; x < nodes / 2; x++)
	{
		if (array[x] != array[nodes - 1 - x])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
