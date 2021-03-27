def transform(word):
  arr = ["#"]*26
  for i in word:
    char = (ord(i)-97)
    if(arr[char] == "#"):
      arr[char] = 1
    else:
      arr[char] += 1
  s = [str(i) for i in arr]
  return ".".join(s)

def groupAnagrams(strs):
  d = {}
  res = []
  for i in range(len(strs)):
    sorted_word = transform(strs[i])
    # print(sorted_word)
    if(sorted_word not in d):
      d[sorted_word] = [strs[i]]
    else:
      d[sorted_word].append(strs[i])
  for key,val in d.items():
    res.append(val)
  return res
groupAnagrams(['cog','fog','gco'])    
