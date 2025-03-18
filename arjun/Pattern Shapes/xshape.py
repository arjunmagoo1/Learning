#X shape

#       0    1   2   3   4     

#   0   *                *

#   1       *        *        

#   2            *                      

#   3       *        *       

#   4  *                  * 

                       

                       



for row in range(0,5):

    for col in range(0,5):

       if( (col==0 and row!=1 and row!=2 and row!=3) or (col==1 and row!=0 and row!=2 and row!=4) or (col==2 and row!=0 and row!=1 and row!=3 and row!=4 ) or ( col==3 and row!=0 and row!=2 and row!=4) or (col==4 and row!=1 and row!=2 and row!=3) ):

         print("*" , end=" ")

       else:

         print(" ", end=" ")


    print() 