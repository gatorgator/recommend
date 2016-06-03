#!/home/xfanwang/anaconda/bin/python
# -*- coding: utf-8 -*-

def RandomSelectNegativeSample(self, items):
    ret = dict()
    for i in items.keys():
        ret[i] = 1
    n = 0
    for i in range(0, len(items) * 3):
        item = items_pool[randomint(0, len(item_pool) - 1)]
        if item in ret:
            continue
        ret[item] = 0
        n += 1
        if n > len(items):
            break
    return ret

#randome gradient descend
# num of laten feature --> F
# learning rate --> alpha
# negative positive sample ratio --> ratio
def LatenFactorModel(user_items, F, N, alpha, lamda):
    [P, Q] = InitModel(user_item, F)
    for step in range(0, N):
        for user, items in user_items.items():
            samples = RandSelectNegativeSamples(items)
            for item, rui in samples.items():
                eui = rui - Predict(user, item)
                for f in range(0, F):
                    #iteratively get P,Q
                    P[user][f] += alpha * (eui * Q[item][f] - \
                            lambda * P[user][f])
                    Q[items][f] += alpha * (eui * P[item][f] - \
                            lambda * Q[user][f])
        alpha *= 0.9

def Recommend(user, P, Q):
    rank = dict()
    for f, puf in range(0, len(P[user])):
        for i, qfi in Q[f]:
            if i not in rank:
                rank[i] = Predict(user, i)
    return rank
