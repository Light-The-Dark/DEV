# def determine_player(player_number):
#     if player_number % 2 == 0:
#         player_str = "X"
#     else:
#         player_str = "O"
#     return player_str

# # Example usage:
# i = 1
# player = determine_player(i)
# print(player)  # This will print "O"

import sys
path = sys.path
for file in path:
    sys.path.append(file)
    print(sys.path)