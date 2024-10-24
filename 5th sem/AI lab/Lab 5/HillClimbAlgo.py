import random

def hill_climbing(f, neighbor, x_range, max_iter=1000):
    current = random.choice(x_range)
    for _ in range(max_iter):
        next_neighbor = max(neighbor(current), key=f)
        if f(next_neighbor) <= f(current):
            break
        current = next_neighbor
    return current, f(current)

def f(x):
    return -x**2

def neighbor(x):
    return [x - 0.1, x, x + 0.1]

x_range = range(11)  # 0 to 10
best_x, best_y = hill_climbing(f, neighbor, x_range)
print(f"Best solution: x = {best_x:.2f}, f(x) = {-best_y:.2f}")