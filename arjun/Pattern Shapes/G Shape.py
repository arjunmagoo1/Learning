#G shape

#       0    1   2   3   4  5     

#   0   *    *   *   *   *    

#   1   *                 

#   2   *                 

#   3   *            *   *   *    

#   4   *                *

#   5   *                *

#   6   *   *   *   *    *    



for row in range(0,7):

    for col in range(0,6):

       if(col==0 or (col==4 and row!=1 and row!=2 ) or ((row==0 or row==6) and col<5 or (row==3 and col!=1 and col!=2 ))):

         print("*" , end=" ")

       else:

         print(" ", end=" ")


    print() 