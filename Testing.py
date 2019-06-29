#/usr/bin/python3

#import this

print("Take a bow")

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)

def exampleForLoop():
  fruits = ["apple", "banana", "cherry"]
  for x in fruits:
    print(x)

print("\n\nFor loop example")
exampleForLoop()

def theEncodings():
  #convert between bytes and string

  norsk = "the quick brown dog"
  print(norsk)
  data = norsk.encode('utf-8')
  print (data)

theEncodings()

def askQuestions():
      
  print("please provide a widget")
  response = input()
  print ("the widget you provided was: ")
  print(response)


def exampleWhileLoop(i, loop):
  while (i < loop):
    print(i)
    i += 1

exampleWhileLoop(4,12)

#List vs dictionaries

def exampleList():
  list("bob")
  colors = {'red','blue'}
  print (colors)

  
exampleList()

