#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
/**
 * infinite_while - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
	int i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else
			exit(1);
		i++;
	}
	infinite_while();
	return (0);
}
