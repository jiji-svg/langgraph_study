def print_update(graph, args: dict):
    for event in graph.stream(**args):
        for key, value in event.items():
            print(f"\n[{key}]\n")
            print(value)
