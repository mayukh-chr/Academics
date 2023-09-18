//doubly linked list functions: 1. creation, 2. insertion, 3.. deletion, 4. traversal


#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node* next;
  struct Node* prev;
};

struct DoublyLinkedList {
  struct Node* head;
};

// Create a new doubly linked list.
struct DoublyLinkedList* createDoublyLinkedList() {
  struct DoublyLinkedList* list = (struct DoublyLinkedList*)malloc(sizeof(struct DoublyLinkedList));
  list->head = NULL;
  return list;
}

// Insert a new node at the beginning of the doubly linked list.
void insertAtBeginning(struct DoublyLinkedList* list, int data) {
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = list->head;
  newNode->prev = NULL;
  if (list->head != NULL) {
    list->head->prev = newNode;
  }
  list->head = newNode;
}

// Insert a new node at the end of the doubly linked list.
void insertAtEnd(struct DoublyLinkedList* list, int data) {
  struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->data = data;
  newNode->next = NULL;
  newNode->prev = NULL;
  if (list->head == NULL) {
    list->head = newNode;
    return;
  }
  struct Node* temp = list->head;
  while (temp->next != NULL) {
    temp = temp->next;
  }
  temp->next = newNode;
  newNode->prev = temp;
}

// Delete a node from the doubly linked list.
void deleteNode(struct DoublyLinkedList* list, int data) {
  struct Node* temp = list->head;
  while (temp != NULL) {
    if (temp->data == data) {
      if (temp == list->head) {
        list->head = temp->next;
        if (list->head != NULL) {
          list->head->prev = NULL;
        }
        free(temp);
        return;
      } else if (temp->next != NULL) {
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        free(temp);
        return;
      } else {
        temp->prev->next = NULL;
        free(temp);
        return;
      }
    }
    temp = temp->next;
  }
}

// Traverse the doubly linked list and print the data of each node.
void traverseDoublyLinkedList(struct DoublyLinkedList* list) {
  struct Node* temp = list->head;
  while (temp != NULL) {
    printf("%d ", temp->data);
    temp = temp->next;
  }
  printf("\n");
}

int main() {
  struct DoublyLinkedList* list = createDoublyLinkedList();

  insertAtBeginning(list, 10);
  insertAtBeginning(list, 20);
  insertAtEnd(list, 30);
  insertAtEnd(list, 40);

  traverseDoublyLinkedList(list);

  deleteNode(list, 20);

  traverseDoublyLinkedList(list);

  return 0;
}

int main() {
  struct DoublyLinkedList* list = createDoublyLinkedList();

  int choice;
  int data;

  do {
    printf("1. Insert at beginning\n");
    printf("2. Insert at end\n");
    printf("3. Delete node\n");
    printf("4. Traverse linked list\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    switch (choice) {
      case 1:
        printf("Enter data to insert: ");
        scanf("%d", &data);
        insertAtBeginning(list, data);
        break;
      case 2:
        printf("Enter data to insert: ");
        scanf("%d", &data);
        insertAtEnd(list, data);
        break;
      case 3:
        printf("Enter data to delete: ");
        scanf("%d", &data);
        deleteNode(list, data);
        break;
      case 4:
        traverseDoublyLinkedList(list);
        break;
      case 5:
        exit(0);
      default:
        printf("Invalid choice!\n");
    }
  } while (choice != 5);

  return 0;
}
