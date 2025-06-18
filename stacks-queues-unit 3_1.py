# Problem 1: Post Format Validator

def is_valid_post_format(post):
  stack = []
  matching_operands = {')':'(','}':'{',']':'['}

  for char in post:
    if char in '({[':
      stack.append(char)
    elif char in ')]}':
      if not stack or stack.pop() != matching_operands[char]:
        return False
  return len(stack) == 0
      

'''print(is_valid_post_format("{()}"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))'''

# Problem 2: Reverse User Comments Queue

def reverse_comments_queue(comments):
  stack = []
  while comments:
    stack.append(comments.pop())
  return stack

'''print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))'''

# Problem 3: Check Symmetry in Post Titles

def is_symmetrical_title(title):
    title = title.lower()
    title = title.replace(" ","")
    i = 0
    j = len(title) - 1
    while i<j:
      if(title[i] != title[j]):
        return False
      i+=1
      j-=1
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 