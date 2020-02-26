def my_function(t):

    print ("The decoded text in ASCII is : ")

    for ch in t:

        num = ord(ch)
        print (num)

        if num > 1: 

           for i in range(2, num//2): 

               if (num % i) == 0: 

                   print(num, "is not a prime number") 
                   break

           else: 

               print(num, "is a prime number") 
      
        else: 

           print(num, "is not a prime number") 


t = input("Enter text : ")
my_function(t)
