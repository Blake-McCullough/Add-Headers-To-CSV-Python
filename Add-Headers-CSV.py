# import pandas with shortcut 'pd'
import pandas as pd  
#Adds header if not there already (manual check needed)
def Add_Header(filename,headers):
  #Lets user know of actions occuring
  print("Adding headers: \n",headers,"\nTo",filename)
  # read_csv function which is used to read the required CSV file
  file = pd.read_csv(filename,header=None)
  #Sets headers to be added from variable
  headerList = headers
  #Sets
  file.to_csv("header-added.csv", header=headerList, index=False)
  #Lets user know of actions occuring
  print("\nSuccesfully added headers: \n",headers,"\nTo",filename)


#Add_Header(filename,headerlist)
filename="output.csv"
headerList = ['POS','DIV','TEAM','GP','WIN','LOSS','PTS','MMR' ]
Add_Header(filename,headerList)
