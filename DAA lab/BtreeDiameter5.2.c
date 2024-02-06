#include <stdio.h>
#include <stdlib.h>
struct TreeNode {
    int data;
    struct TreeNode* left;
    struct TreeNode* right;
};
struct TreeNode* newNode(int data) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}
int max(int a, int b) {
    return (a > b) ? a : b;
}
int height(struct TreeNode* root) {
    if (root == NULL)
        return 0;
    return 1 + max(height(root->left), height(root->right));
}
int diameter(struct TreeNode* root) {
    if (root == NULL)
        return 0;
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    int leftDiameter = diameter(root->left);
    int rightDiameter = diameter(root->right);
    return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter));
}
struct TreeNode* buildTree() {
    int data;
    printf("Enter the data for the root node: ");
    scanf("%d", &data);
    if (data == -1)
        return NULL;
    struct TreeNode* root = newNode(data);
    printf("Enter the left subtree of %d:\n", data);
    root->left = buildTree();
    printf("Enter the right subtree of %d:\n", data);
    root->right = buildTree();

    return root;
}
int main() {
    struct TreeNode* root = NULL;
    printf("Enter the binary tree (use -1 for null nodes):\n");
    root = buildTree();
    printf("Diameter of the given binary tree is %d\n", diameter(root));
    return 0;
}
