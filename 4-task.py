def factorial(k):
  f = 1
  for i in range(1, k+1):
    f *= i

  return f


def stair(n):
  k = int(n/2)
  count = 0
  for i in range(k+1, n):
    count += factorial(i)/(factorial(n-i) * factorial(i-(n-i)))

  if n%2==0: count+=2
  else: count+=1
  
  return int(count)

print(stair(6))