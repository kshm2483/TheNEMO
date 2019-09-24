
# 가장 많이 존재하는 이름 리턴
def raw_majority_vote(labels):
    votes = Counter(labels)
    winner,_ = votes.most_common(1)[0]

return winner


# 가장 많이 존재하는 이름 찾는데, 하나뿐이면 그것 리턴, 
# 축구 야구 둘다 동일한 숫자가 k 거리 이내가 있다면, 제일 멀리 있는 놈 제외하고 다시 찾기
def majority_vote(labels):
    vote_counts = Counter(labels):
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                        for count in vote_counts.values()
                        if count == winner_count])

    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])




# k: 어느정도 가까운 것들을 찾는가?
# labeled_points: 분류에 사용될 데이터목록들
# your_point : 분류하고 싶은 데이터
def knn_classify(k, labeled_points, your_point):
    # 분류에 사용될 데이터를 분류될 데이터와 거리순으로 정렬
    by_distance = sorted(labeled_points,
                         key = lambda (point,_): distance(point, your_point()))

    k_nearest_labels = [label for _, label in by_dustance[:k]]

    return majority_vote(k_nearest_labels)

