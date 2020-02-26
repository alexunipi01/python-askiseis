with open('example.txt') as f:
    good = 0
    bad = 0
    for line in f:
        for word in line.split():
            for i in word :
                if i=='f' or i=='F' or i=='c' or i=='C' or i=='k' or i=='K' or i=='r' or i=='R':
                    bad = bad + 1
                else:
                    good = good + 1
  
            if bad > good :
                print(word , ": bad word")
            else:
                print(word , ": good word")

            good = 0
            bad = 0
                



