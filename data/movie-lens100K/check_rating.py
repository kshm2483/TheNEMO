with open('u.data', 'r', encoding="UTF-8") as p:
    for line in p.readlines():
        [UserID, MovieID, Rating, Timestamp] = line.split('\t')
        if int(UserID) > 943 or int(MovieID) > 1682:
            print([UserID, MovieID, Rating, Timestamp])