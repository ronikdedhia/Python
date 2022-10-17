graph = {
 '5' : ['3','7'],
 '3' : ['2', '4'],
 '7' : ['8'],
 '2' : [],
 '4' : ['8'],
 '8' : []
}
visited = []
queue = []
def bfs(visited, graph, node, goal):
 visited.append(node)
 queue.append(node)
 goalReached = False
while (queue):
 m = queue.pop(0)
 if(m==goal):
 print(goal)
 print("Goal State Reached")
 goalReached = True
 break
 print (m, end = "->")
 for neighbour in graph[m]:
 if neighbour==goal:
 visited.append(neighbour)
 queue.append(neighbour)
 break
 if neighbour not in visited:
 visited.append(neighbour)
 queue.append(neighbour)

 if not goalReached:
 print("\nGoal State not Reached")

start = input("Enter start state: ")
goal = input("Enter Goal state: ")
print("Following is the Breadth-First Search")
bfs(visited, graph, start, goal)