def TagPopularity(records):
    tagfreq = dict()
    #<user, item, tag>
    for user,item,tag in records:
        if tag not in tagfreq:
            tagfreq[tag] = 1
        else:
            tagfreq[tag] += 1
    return tagfreq

def CosineSim(item_tags, i, j):
    ret = 0
    #item_tags[i] vector of tags for item i
    for b, wib in item_tags[i].items():
        if b in item_tags[j]:
            #item_tags[j][b] times of tag b for item i
            ret += wib * item_tags[j][b]
    ni = 0
    nj = 0
    for b, w in item_tags[i].items():
        ni += w * w
    for b, w in item_tags[j].items():
        nj += w * w
    if ret == 0:
        return 0
    return ret/math.sqrt(ni*ni)

def Diversity(item_tags, recommend_items):
    ret = 0
    n = 0
    for i in recommend_items.keys():
        for j in recommend_items.keys():
            if i == j:
                continue
            ret += CosineSim(item_tags, i, j)
            n += 1
    return ret/(n * 1.0)
