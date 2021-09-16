def exchange(money):
  min_count = 0

  coins = [1, 5, 10, 20, 50]
  coins.sort(reverse=True)
  
  for i in coins:
    if money <= 0: break

    min_count += int(money/i)
    money %= i
  
  return min_count


print(exchange(70))