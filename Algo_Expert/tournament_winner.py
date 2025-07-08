def tournamentWinner(competitions, results):
    # Write your code here.
    scores = {}
    i = 0
    max_score = 0
    winner = ""
    for match in competitions:
        if match[1 - results[i]] in scores:
            scores[match[1 - results[i]]] += 3
            if scores[match[1 - results[i]]] > max_score:
                winner = match[1 - results[i]]
            max_score = max(max_score, scores[match[1 - results[i]]])
            i += 1
        else:
            scores[match[1 - results[i]]] = 3
            if scores[match[1 - results[i]]] > max_score:
                winner = match[1 - results[i]]
            max_score = max(max_score, scores[match[1 - results[i]]])
            i += 1
            
    return winner




if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]
    print(tournamentWinner(competitions=competitions, results=results))