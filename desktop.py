#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random
n = random.randrange(1,100)
guess = int(input("Enter any number: "))
while n!= guess:
   if guess < n:
       print("Your guess is too low. Guess again.")
       guess = int(input("Enter number again: "))
   elif guess>n:
       print("Your guess is too high. Guess again.")
       guess = int(input("Enter number again: "))
   else:
     break
print("Congratulations! You guessed the number correctly!")


# In[ ]:




