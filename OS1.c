#include<unistd.h>
#include<stdio.h>
#include<sys/types.h>
#include<sys/wait.h>

int main()
{
int c=0;

while(c<=0)
{
printf("Enter Number: ");
scanf("%d",&c);
}
pid_t pid=fork();

if(pid ==0)
{
  printf("Child Process is Running\n");
  printf("%d\n",c);
  while(c!=1)
  {
    if(c%2==0)
    {
      c=c/2;
      printf(" %d\n",c);
    }
  }
  printf("Child Process is Completed\n");
}
else
{
  printf("Parent Process is Waiting for Child to complete\n");
  wait(NULL);
  printf("Parent process is done. \n");
}
return 0;
}


