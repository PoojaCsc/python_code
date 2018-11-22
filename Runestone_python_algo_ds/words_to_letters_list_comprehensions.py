# o/p - ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']
#print ("".join(["cat","dog","rabbit"]))

print ([ch for ch in "".join(["cat","dog","rabbit"])])

print ([word[i] for word in ["cat","dog","rabbit"] for i in range(len(word))])   # nested list comprehension

print(list(set([word[i] for word in ["cat","dog","rabbit"] for i in range(len(word))])))   # remove duplicates by putting in set and then converting it to list