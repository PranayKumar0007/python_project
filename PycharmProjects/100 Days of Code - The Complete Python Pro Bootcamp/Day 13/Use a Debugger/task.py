import random
import maths


 #def mutate(a_list):
  ##  new_item = 0
  #  for item in a_list:
      #  new_item = item * 2
   #     new_item += random.randint(1, 3)
    #    new_item = maths.add(new_item, item)
     #   b_list.append(new_item)
   # print(b_list)


 #mutate([1, 2, 3, 5, 8, 13])
def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


odd_or_even(1)