# def numberOfWaysToTraverseGraph(width, height):
#     # Write your code here.
#     mat_ways = [[0] * (width) for _ in range(height)]

#     for hei_idx in range(0, height):
#         for wid_idx in range(width):
#             if wid_idx == 0 or hei_idx == 0:
#                 mat_ways[hei_idx][wid_idx] = 1
#             else:
#                 left_val = mat_ways[hei_idx - 1][wid_idx]
#                 right_val = mat_ways[hei_idx][wid_idx - 1]
#                 mat_ways[hei_idx][wid_idx] = left_val + right_val
#     return mat_ways[height - 1][width - 1]

def numberOfWaysToTraverseGraph(width, height):
    memo = {}
    return helper(height - 1, width - 1, memo)

def helper(width, height, memo):
    if width == 0 or height == 0:
                return 1
    if (height, width) in memo:
          return memo[(height, width)]
    memo[(height, width)] = helper(height - 1, width, memo) + helper(height, width - 1, memo)
    return memo[(height, width)]


if __name__ == '__main__':
    width = 4
    height = 3
    print(numberOfWaysToTraverseGraph(width, height))