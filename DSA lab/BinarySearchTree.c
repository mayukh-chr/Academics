//insert, delete, search in binary search tree.

#include <stdio.h>
#include <stdlib.h>

// Structure for a BST node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new BST node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

// Function to insert a node in the BST
struct Node* insert(struct Node* root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    return root;
}

// Function to search for a node in the BST
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key) {
        return root;
    }
    if (key < root->data) {
        return search(root->left, key);
    }
    return search(root->right, key);
}

// Function to find the minimum value node in a BST
struct Node* findMin(struct Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

// Function to find the maximum value node in a BST
struct Node* findMax(struct Node* root) {
    while (root->right != NULL) {
        root = root->right;
    }
    return root;
}

// Function to delete a node in the BST
struct Node* deleteNode(struct Node* root, int key) {
    if (root == NULL) {
        return root;
    }
    if (key < root->data) {
        root->left = deleteNode(root->left, key);
    } else if (key > root->data) {
        root->right = deleteNode(root->right, key);
    } else {
        if (root->left == NULL) {
            struct Node* temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct Node* temp = root->left;
            free(root);
            return temp;
        }
        struct Node* temp = findMin(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

int main() {
    struct Node* root = NULL;
    int choice, key;

    while (1) {
        printf("\nBinary Search Tree Operations:\n");
        printf("1. Insert a node\n");
        printf("2. Delete a node\n");
        printf("3. Search for a node\n");
        printf("4. Find Minimum Node\n");
        printf("5. Find Maximum Node\n");
        printf("6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the value to insert: ");
                scanf("%d", &key);
                root = insert(root, key);
                break;
            case 2:
                printf("Enter the value to delete: ");
                scanf("%d", &key);
                root = deleteNode(root, key);
                break;
            case 3:
                printf("Enter the value to search: ");
                scanf("%d", &key);
                if (search(root, key) != NULL) {
                    printf("Node found\n");
                } else {
                    printf("Node not found\n");
                }
                break;
            case 4:
                if (root == NULL) {
                    printf("Tree is empty\n");
                } else {
                    struct Node* minNode = findMin(root);
                    printf("Minimum Node: %d\n", minNode->data);
                }
                break;
            case 5:
                if (root == NULL) {
                    printf("Tree is empty\n");
                } else {
                    struct Node* maxNode = findMax(root);
                    printf("Maximum Node: %d\n", maxNode->data);
                }
                break;
            case 6:
                printf("Exiting program\n");
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }

    return 0;
}
