def vowels(x):
      vo=["a"or"e"or"i"or"o"or"u"or"A"or"E"or"I"or"O"or"u"]
      count=0
      for char in x:
          if char in vo:
                count=+1
      return  count
x=input("enter a string: ")
print(vowels(x))