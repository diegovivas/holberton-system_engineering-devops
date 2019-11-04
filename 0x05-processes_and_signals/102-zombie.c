#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
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
		if (pid == 0)
		{
			pid = getpid();
			printf("Zombie process created, PID: %d\n", pid);
			infinite_while();
		}
		i++;
	}

	return (0);
}
