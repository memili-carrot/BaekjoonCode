import sys
heart = """ @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     
"""
n = int(input().strip())
sys.stdout.write(heart * n)