s1 = [{1,2,3,4}, {3,4,5}]
s2 = [{1,2,3,4}, {3,4,5}, {2,6}]

def unique(collection):

  all = []
  blacklist = []

  for col in collection:
    for t in col:

      if t not in all:
        if t not in blacklist:
          # not on blacklist, not added yet
          all.append(t)
          blacklist.append(t) 
      else: 
        all.remove(t)
        blacklist.append(t)

  return all


print(unique(s2))
