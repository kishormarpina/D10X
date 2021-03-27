def groupAnagrams(strs):
  d = {}
  res = []
  for i in range(len(strs)):
    sorted_word = ("".join(sorted(strs[i])))
    if(sorted_word not in d):
        d[sorted_word] = [strs[i]]
    else:
        d[sorted_word].append(strs[i])
  for key,val in d.items():
    res.append(val)
  return res
groupAnagrams(['cog','fog','gco'])  
