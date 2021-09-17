def palindrome(string):

  for i in range(0, int(len(string)/2)):

    if(string[i] != string[-i-1]):
      return False

  return True


print(palindrome('radar'))

