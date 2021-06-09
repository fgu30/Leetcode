import bisect
  
# initializing list
li = [0,0,0,3,3]
  
# # using bisect() to find index to insert new element
# # returns 5 ( right most possible index )
# print ("The rightmost index to insert, so list remains sorted is  : ", end="")
# print (bisect.bisect(li, 4))
  
# # using bisect_left() to find index to insert new element
# # returns 2 ( left most possible index )
print ("The leftmost index to insert, so list remains sorted is  : ", end="")
print (bisect.bisect_left(li, -1))

# # using bisect_right() to find index to insert new element
# # returns 4 ( right most possible index )
# print ("The rightmost index to insert, so list remains sorted is  : ", end="")
# print (bisect.bisect_right(li,3,3,5))