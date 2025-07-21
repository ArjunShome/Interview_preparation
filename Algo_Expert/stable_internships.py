def stableInternships(interns, teams):
    # Write your code here.

    # Final intern and team pair
    team_intern_pair = {}
    
    # dict to store the intern and team mapping.
    intern_team_map = {}

    # Team ranking of Interns
    i = 0
    for team_idx, team in enumerate(teams):
        intern_team_map[team_idx] = {}
        for intern_idx, intern in enumerate(team):
            intern_team_map[team_idx][intern] = intern_idx

    # list of interns (can be stack or queue)
    intern_stack = list(range(len(interns)))
    intern_choice = [0] * len(intern_stack)

    if len(interns) == 1:
        return [[interns[0][0], teams[0][0]]]

    while len(intern_stack) > 0:
        intern_num = intern_stack.pop()

        if intern_choice[intern_num] >= len(interns[intern_num]):
            continue
        intern = interns[intern_num]
        team_preference = intern[intern_choice[intern_num]]
        intern_choice[intern_num] += 1

        if team_preference not in team_intern_pair:
            team_intern_pair[team_preference] = intern_num
            continue

        previous_intern = team_intern_pair[team_preference]
        previous_rank = intern_team_map[team_preference][previous_intern]
        current_rank = intern_team_map[team_preference][intern_num]

        if current_rank < previous_rank:
            intern_stack.append(previous_intern)
            team_intern_pair[team_preference] = intern_num
        else:
            intern_stack.append(intern_num)
            
    return sorted([[intern, team] for team, intern in team_intern_pair.items()])


if __name__ == '__main__':
    interns = [
        [0, 1],
        [0, 1]
    ] 
    teams = [
        [0, 1],
        [0, 1]
    ]

    print(stableInternships(interns, teams))