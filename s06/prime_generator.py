def prime_gen(n):

     if n==2 or n==3 or n==1:
        yield "true"
     if n%2==0:
        yield "false"


prime_gen(10)