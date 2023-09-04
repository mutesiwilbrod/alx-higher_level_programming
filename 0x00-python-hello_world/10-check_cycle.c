#include "lists.h"
/**
* check_cycle - checks for a cycle in a singly linked list
* @list: singly list to check
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;

	if (list != NULL)
	{
		while (head && head->next)
		{
			head = head->next->next;
			tail = tail->next;
			if (tail == head)
			{
				tail = list;
				while (tail != head)
				{
					tail = tail->next;
					head = head->next;
				}
				return (1);
			}
		}
	}
	return (0);
}
