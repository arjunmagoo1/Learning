#Pyramid shape

#       0    1   2   3   4    5     6        
 
#   0   *    *   *    *    *   *   *

#   1       *    *    *    *   *                     

#   2            *    *    *               

#   3                 *              

#   4                                     

#   5                                      

#   6                                       



for row in range(0,4):

    for col in range(0,7):

       #if( (row==0)  or (row==1 and col>0 and col<6) or ( row==2 and col>1 and col<5) or ( row==3 and col>2 and col<4)): #ulta diamond
         
       if( (row==3)  or (row==2 and col>0 and col<6) or ( row==1 and col>1 and col<5) or ( row==0 and col>2 and col<4)):   #sidha diamond
      

         print("*" , end=" ")

       else:

         print(" ", end=" ")


    print() 