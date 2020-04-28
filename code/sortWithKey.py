# function defined with def
def num_vowel(x):
  cnt = 0
  for char in x.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
      cnt += 1
  print(cnt)
  return cnt

names = ['Paula', 'Amanda', 'Ana', 'Amaranta', 'Li']

names.sort(key=num_vowel ,reverse=True)

print(names)
# ['Li', 'Ana', 'Paula', 'Amanda', 'Amaranta']
