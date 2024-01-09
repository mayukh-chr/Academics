//
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int key;
    struct Node *left, *right;
};

struct Node* root = NULL;

struct Node* create(int value)
{
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->key = value;
    temp->left = temp->right = NULL;
    return temp;
}

struct Node* insertNode(struct Node* node, int value)
{
    if (node == NULL)
        return create(value);

    if (value < node->key)
        node->left = insertNode(node->left, value);

    else if (value > node->key)
        node->right = insertNode(node->right, value);

    return node;
}

struct Node* searchNode(struct Node* root, int target)
{
    if (root == NULL || root->key == target)
        return root;

    if (root->key < target)
        return searchNode(root->right, target);

    return searchNode(root->left, target);
}

void inOrder(struct Node* root)
{
    if (root != NULL) {
        inOrder(root->left);
        printf(" %d ", root->key);
        inOrder(root->right);
    }
}

int main(){
    root = insertNode(root, 50);
    insertNode(root, 30);
    insertNode(root, 20);
    insertNode(root, 40);
    insertNode(root, 70);
    insertNode(root, 60);
    insertNode(root, 80);

    int q;
    scanf("%d", &q);

    if (searchNode(root, q) != NULL) {
        printf("key found\n");
    }
    else {
        printf("key not found\n");
    }


    inOrder(root);
    printf("\n");
    return 0;
}
