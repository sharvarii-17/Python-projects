import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq

graph = {
    "Sitabuldi": {"Sadar": 5, "LIC Square": 3, "Friends Colony": 7},
    "Sadar": {"Sitabuldi": 5, "Maharjbag": 4},
    "LIC Square": {"Sitabuldi": 3, "Friends Colony": 2},
    "Friends Colony": {"Sitabuldi": 7, "LIC Square": 2, "Maharjbag": 6},
    "Maharjbag": {"Sadar": 4, "Friends Colony": 6},
}
fare_per_km = 10

# using Dijkstra's algorithm
def shortest_path(start, destination):
    if start not in graph or destination not in graph:
        return "Invalid places entered."

    distances = {place: float("inf") for place in graph}
    distances[start] = 0
    queue = [(0, start)]
    previous = {}
    while queue:
        current_distance, current_place = heapq.heappop(queue)
        if current_place == destination:
            path = []
            while current_place in previous:
                path.append(current_place)
                current_place = previous[current_place]
            path.append(start)
            path.reverse()
            return path, current_distance
        for neighbor, distance in graph[current_place].items():
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                previous[neighbor] = current_place
    return "No path found between the places."

G = nx.Graph()
for place in graph:
    G.add_node(place)
for place, connections in graph.items():
    for neighbor in connections:
        G.add_edge(place, neighbor)

pos = nx.circular_layout(G)

start_place = input("Enter the start place: ")
destination_place = input("Enter the destination place: ")

shortest_path, shortest_distance = shortest_path(start_place, destination_place)
shortest_time = shortest_distance / 40
fare = shortest_distance * fare_per_km

fig, ax = plt.subplots(figsize=(10, 6))

node_colors = [
    random.choice(["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3"])
    for _ in range(len(G))
]
nx.draw_networkx_nodes(
    G,
    pos=pos,
    node_size=800,
    node_color=node_colors,
    edgecolors="black",
    linewidths=1,
    ax=ax,
)

nx.draw_networkx_edges(G, pos=pos, edge_color="#cccccc", width=2, ax=ax, alpha=0.8)
nx.draw_networkx_labels(G, pos=pos, font_size=10, font_color="black", ax=ax)
path_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(
    G, pos=pos, edgelist=path_edges, edge_color="#ff0000", width=3, ax=ax
)

ax.set_title(
    f"Shortest Path from {start_place} to {destination_place}",
    fontweight="bold",
    fontsize=14,
)
ax.set_facecolor("#f2f2f2")
ax.axis("off")

for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color("#cccccc")
    spine.set_linewidth(1)

info_text = f"Start: {start_place}\nDestination: {destination_place}\nFare: {fare} units\nDistance: {shortest_distance} km\nTime Taken: {shortest_time:.2f} hours"
ax.text(1.1, 0.5, info_text, transform=ax.transAxes, ha="left", fontsize=12)

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.show()
