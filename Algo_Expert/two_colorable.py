def twoColorable(edges):
    # Write your code here.
    colors = [None for row in edges]
    stack = []

    stack.append(0)
    colors[0] = True
    is_colorable = checkTwoColorable(edges, stack, colors)
    
    return is_colorable

def checkTwoColorable(edges, stack, colors):
    while len(stack) > 0:
        current = stack.pop(0)
        current_color = colors[current]

        for edge in edges[current]:
            if colors[edge] == None:
                if current_color:
                    colors[edge] = False
                else:
                    colors[edge] = True
                stack.append(edge)
            else:
                if colors[edge] == current_color:
                    return False
    return True


if __name__ == '__main__':
    edges = [
        [1,3],
        [0,2],
        [1,3],
        [0,2]
    ]

    print(twoColorable(edges))