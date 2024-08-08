#include <stdio.h>

#define MAX 5

int c_arr[MAX];
int front = -1;
int rear = -1;

void enqueue(int item){
    if ((front ==0 && rear == MAX-1) ||(front == rear+1)){
        printf("Queue overflow \n");
        return;
        }

    if (front == -1){
        front = 0;
        rear = 0;
    }

    else{
        rear++;
        }

    c_arr[rear]= item;
    }

void dequeue(){
    if (front == -1)
    {
        printf("Queue underflow \n");
        return;
    }
    printf("Element deleted from queue is: %d \n", c_arr[front]);

    if (front == rear){
        front =-1;
        rear = -1;
    }
    else{
        if(front == MAX-1)
            front = 0;
        else
            front = front + 1;
        }
}

void display(){
    int fpos = front, rpos = rear;

    if (front == -1){
        printf("Queue is empty \n");
        return;
    }
    printf("Queue elements: \n");
    if(fpos <= rpos)
    while(fpos <=rpos){
        printf("%d ", c_arr[fpos]);
        fpos++;
    }
    else{
        while(fpos <= MAX-1){
            printf("%d ", c_arr[fpos]);
            fpos++;
        }
    }
    printf("\n");
}


int main(){
    int ch, item;
    printf(" 1. Insert \n 2. Delete \n 3. Display \n 4. Quit \n");

    do{
        printf("enter your choice: ");
        scanf("%d", &ch);

        switch(ch){
        case 1:
            printf("Enter the element: ");
            scanf("%d", &item);
            enqueue(item);
            break;
        case 2:
            dequeue();
            break;
        case 3:
            display();
            break;
        case 4:
            exit(1);
            break;
        default:
            printf("Incorrect choice\n");
            }
    }

while(ch!= 4);

return 0;
}
