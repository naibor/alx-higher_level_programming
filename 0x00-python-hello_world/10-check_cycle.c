#include "lists.h"
/**
 * check_cycle - Function
 *
 * Description: checks if a singly linked list has a cycle in it
 *
 * @list: pointer of type listint_t, the singly list
 *
 * Return: returns 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *second = list, *first = list;

	if (!list)
	{
		return (0);
	}
	while (second && first && first->next)
	{
		second = second->next;
		first = first->next->next;
		if (second == first)
			return (1);
	}

	return (0);
}

