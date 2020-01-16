# importing datetime module 
import datetime 
  
# datetime.datetime.now() to get  
# current date as filename. 
filename = datetime.datetime.now() 
  
# create empty file 
def create_file(): 
    # Function creates an empty file 
    # %d - date, %B - month, %Y - Year 
    with open(filename.strftime("found - %d %B %Y")+".txt", "w") as file: 
        file.write("") 
  
# Driver Code 
create_file() 
