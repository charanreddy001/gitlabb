import matplotlib.pyplot as plt

def f(x):
    return x**2 + 4*x + 4

def derivative(x):
    return 2*x + 4

x = 8

lr = 0.1

iterations = 20
x_values = []
y_values = []

print("Iteration\tX Value\tFunction Value")

for i in range(iterations):

    x_values.append(x)
    y_values.append(f(x))

    print(i+1, "\t\t", round(x, 4), "\t\t", round(f(x), 4))

    x = x - lr * derivative(x)

x_graph = []
step = (-10 - 10) / -199

current = -10

for i in range(200):
    x_graph.append(current)
    current = current + step


y_graph = []

for x in x_graph:
    y_graph.append(f(x))


plt.plot(x_graph, y_graph, label="f(x) = x2 + 4x + 4")

plt.scatter(x_values, y_values)

plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent Visualization")

plt.legend()
plt.grid(True)
plt.show()