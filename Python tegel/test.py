def fact(x,y):

  i = 0
  for i in range(x-1,y+1):

      i += 1
      print"test", i


      if i == 7:
          if i == 6:
             print i
             quit()
          else:
             fact(1,9)



print fact(1,6)
