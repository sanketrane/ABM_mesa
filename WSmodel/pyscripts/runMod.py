import matplotlib.pyplot as plt
import numpy as np
from WS_model import *


'''
all_wealth = []
# This runs the model 100 times, each model executing 10 steps.
for j in range(100):
    # Run the model
    model = MoneyModel(10)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_wealth.append(agent.wealth)

plt.hist(all_wealth, bins=range(max(all_wealth) + 1))
plt.show()
'''

model = MoneyModel(50, 10, 10)
for i in range(20):
    model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]
p1 = plt.figure(1)
plt.hist(agent_wealth)
p1.show()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for block in model.grid.coord_iter():
    block_content, x, y = block
    agent_count = len(block_content)
    agent_counts[x][y] = agent_count


agent_loc = [a.pos for a in model.schedule.agents]

# open file in write mode
with open('sales.txt', 'w') as fp:
    for a in agent_loc:
        line = ' '.join(str(x) for x in a)
        fp.write("%s\n" % line)
    print('Done')
    
p2 = plt.figure(3)
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()

p2.show()

'''
block_wealth = np.zeros((model.grid.width, model.grid.height))
for block in model.grid.coord_iter():
    block_content, wealth = block


'''
input()