def main(size):
  
   i = 1
   while i<size:
     
      print(" "(size-i) + " " * i)
      i+=1 

   i = size
   while i>=1:
     
      print(" "(size-i) + " " * i)
      i-=1
 
print("\n=== Diamond ===\n")   
main(5)