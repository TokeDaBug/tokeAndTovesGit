#open scores.txt in read mode
with open("scores.txt", "r") as infile:
    max_scores = []
    for line in infile:
        collums = line.strip().split("\t")
        N = len(collums) - 1 
        accession_number = collums[0]
        scores = list(map(float, collums[1:N]))
        combined_score = sum(scores)
        line += 1
        
        while len(max_scores) < 10:
            max_scores.append((accession_number, combined_score))
            max_scores.sort(key=lambda x: x[1], reverse=True)
        if combined_score > max_scores[-1][1]:
            max_scores[-1] = (accession_number, combined_score)
            max_scores.sort(key=lambda x: x[1], reverse=True)


#open scoresextreme in writemode
with open("scoresextreme.txt", "w") as outfile:
    for accession_number, score in max_scores:
        outfile.write(f"{accession_number}\t{score}\n")
