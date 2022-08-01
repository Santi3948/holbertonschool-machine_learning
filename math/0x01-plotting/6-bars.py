import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))


labels = ["Farrah", "Fred", "Felicia"]
apples = fruit[0]
bananas = fruit[1]
oranges = fruit[2]
peaches = fruit[3]
fig, ax = plt.subplots()

ax.bar(labels, apples,  width=0.5, color="red", label="apples")
ax.bar(labels, bananas, width=0.5, color="yellow", label="bananas", bottom=apples)
ax.bar(labels, oranges, width=0.5, color="#ff8000", label="oranges", bottom=bananas+apples)
ax.bar(labels, peaches, width=0.5, color="#ffe5b4", label="peaches", bottom=oranges+bananas+apples)

ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.axis([None,None,0,80])
ax.set_yticks(np.arange(0, 81, 10))
ax.legend()
plt.show()