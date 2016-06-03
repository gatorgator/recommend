#!/home/xfanwang/anaconda/bin/python
# -*- coding: utf-8 -*-

def Recommend(user, train, W):
    rank = dict()
    iteracted_items = train[user]
    for v, wuv in sorted(W[u].items, key=itemgetter(1),\
            reverse=True)[0:K]:
        for i, rvi in train[v].items:
            if i in iteracted_items:
                #we should filter item users interacted before
                continue
            rank[i] = wuv * rvi
    return rank
