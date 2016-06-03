def RecentPopularity(records, alpha, T):
    ret = dict()
    for user, item, tm in records:
        if tm >= T:
            continue
        addToDict(ret, item, 1/(1.0+alpha * (T - tm)))
    return ret

def ItemSimilarity(train, alpha):
    #calculate co-rated users between items
    C = dict()
    N = dict()
    for u, items in train.items():
        for i, tui in items.items():
            N[i] += 1
            for j, tuj in items.items():
                if i == j:
                    continue
                C[i][j] += 1 / (1 + alpha * abs(tui - tuj))
    #calculate final similarity matrix W
    W = dict()
    for i, related_items in C.items():
        for j, cij in related_items.items():
            W[u][v] = cij / math.sqrt(N[i] * N[j])
    return W

def Recommendation(train, user_id, W, K, t0):
    rank = dict()
    ru =  train[user_id]
    for i, pi in ru.items():
        for j, wj in sorted(W[i].items(),\
                key=itemgetter(i), reverse=True)[0:K]:
            if j, tuj in ru.items():
                continue
            rank[j] += pi * wj / (1 + alpha * (t0 - tuj))
    return rank

def UserSimilarity(train):


def Recommend(user, T, train , W):


def PathFusion(user, time, G, alpha):




