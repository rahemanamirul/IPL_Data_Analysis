#!/usr/bin/env python
# coding: utf-8

# # project / Task - 3

#  # Matrics / Numpy-----
#   
#   
# :- Matrix is the tabular representation of the data
# 
# :- Lot of datas are stored in table format,that is why Matrices is very very important topic in python
# 
# :- as we working on dataframe so matrices are played a  
#    major rule
# 
# :- List is one dimension & matrix is multidimension
# 
# :- indexation is very important to plot the datapoints
# 
# :- we will see tht & we gonna analyze the NBA players
# 
# :- hear i have taken top 10 highest paid player in 2015-2016 season
# 
# :- we will analyze how 10 players have been playing over the past 10 years & we had the data for past 10yrs yrs
# 
# :- our main goal is to find trends,patterns & their performance for the past 10 yrs
# 
# :- ultimately they haven't always been top 10 player & lets see how they improving, what actually secreates or patterns
# 
# :- dont worry guys if you dont know anything about basket 
# 
#   ball NBA
# 
# :- I will explain indepth of everything
# 
# :- lets analyze the statistics of the basket ball player
# 
# :- gp - total games played,mpg - minutes per game,field goal(accuracy), ppg (points per game) -- this is no of point player has scores in that season
# 
# :- guys slowly i am bringing you into data analytics, jump into datavisualization using python
# 
# :- i will give you the this code can everybody copy and paste your jupyter notebook
# 
# :- Now i will explain with matrices

# In[221]:


import numpy as np


# In[222]:


#Seasons


# In[223]:


Seasons = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
Sdict = {"2010":0,"2011":1,"2012":2,"2013":3,"2014":4,"2015":5,"2016":6,"2017":7,"2018":8,"2019":9}


# In[224]:


#Players


# In[225]:


Players = ["Sachin","Rahul","Smith","Sami","Pollard","Morris","Samson","Dhoni","Kohli","Sky"]
Pdict = {"Sachin":0,"Rahul":1,"Smith":2,"Sami":3,"Pollard":4,"Morris":5,"Samson":6,"Dhoni":7,"Kohli":8,"Sky":9}


# In[226]:


#Salaries
Sachin_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Rahul_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
Smith_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Sami_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Pollard_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Morris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Samson_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Dhoni_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Kohli_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Sky_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, Sami_Salary, Pollard_Salary, Morris_Salary, Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])


# In[227]:


#GAMES
Sachin_G = [80,77,82,82,73,82,58,78,6,35]
Rahul_G = [82,57,82,79,76,72,60,72,79,80]
Smith_G = [79,78,75,81,76,79,62,76,77,69]
Sami_G = [80,65,77,66,69,77,55,67,77,40]
Pollard_G = [82,82,82,79,82,78,54,76,71,41]
Morris_G = [70,69,67,77,70,77,57,74,79,44]
Samson_G = [78,64,80,78,45,80,60,70,62,82]
Dhoni_G = [35,35,80,74,82,78,66,81,81,27]
Kohli_G = [40,40,40,81,78,81,39,0,10,51]
Sky_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([Sachin_G, Rahul_G, Smith_G, Sami_G, Pollard_G, Morris_G, Samson_G, Dhoni_G, Kohli_G, Sky_G])



# In[228]:


#Points
Sachin_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Rahul_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
Smith_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Sami_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Pollard_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Morris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Samson_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Dhoni_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Kohli_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Sky_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, Sami_PTS, Pollard_PTS, Morris_PTS, Samson_PTS, Dhoni_PTS, Kohli_PTS, Sky_PTS])             


# In[229]:


Salary # matrix format


# In[230]:


Games # Building your first matrix----


# In[231]:


Points 


# In[232]:


mydata = np.arange(0,20)
print(mydata)


# In[233]:


np.reshape(mydata,(4,5)) # 5 rows and 4 columns


# In[234]:


mydata


# In[235]:


# np.reshape(mydata, (5,4), order = "c") # means to read / write the element using c-like index order
mat1 = np.reshape(mydata, (5,4), order = "c")
mat1


# In[236]:


mat1


# In[237]:


mat1[4,3]


# In[238]:


mat1[2,3]


# In[239]:


mat1


# In[240]:


mat1[-3,-1]


# In[241]:


mydata


# In[242]:


## mat2 = np.reshape(mydata, (5,4), order = "F") # reshape behaviour are  - 'C','F','A'
mat2


# In[243]:


mat2[4,3]


# In[244]:


mat2[3,1]


# In[245]:


mat2[0:2]


# In[58]:


mat2


# In[59]:


mat2[1:2]


# In[60]:


mat2[1:4]


# In[61]:


mat2[0:3]


# In[62]:


mat2


# In[63]:


mat2[1,2]


# In[64]:


mat2[3,2]


# In[65]:


mat2[3,3]


# In[66]:


mat2[-2,-1]


# In[67]:


mat2


# In[68]:


mat2[-3,-3]


# In[69]:


mat2[0:2]


# In[70]:


mydata


# In[72]:


mat2 = np.reshape(mydata, (5,4), order = "A")
mat2


# In[73]:


mat2 # F shaped


# In[74]:


mat2 # c shaped


# In[75]:


a1 = ["welcome", "to", "datascience"]
a2 = ["request", "hard", "work" ]
a3 = [1,2,3]


# In[76]:


[a1,a2,a3] # list same datatype


# In[77]:


np.array([a1,a2,a3]) # u11 _ unicode 11 character : 3*3


# In[78]:


Games


# In[79]:


Games[1]


# In[81]:


Games[5]


# In[83]:


Games[0:5]


# In[84]:


Games[0,5]


# In[85]:


Games[0,8]


# In[87]:


Games[3,3]


# In[88]:


Games


# In[89]:


Games[0:2]


# In[90]:


Games[0:5]


# In[91]:


Games


# In[92]:


Games[1:2]


# In[93]:


Games[2]


# In[94]:


Games[3:8]


# In[96]:


Games


# In[97]:


Games[-3:-1]


# In[98]:


Games[-3,-1]


# In[100]:


Points


# In[101]:


Points[0]


# In[102]:


Points


# In[103]:


Points[6,1]


# In[105]:


Points[3:6]


# In[106]:


Points


# In[107]:


Points[-6,-1]


# In[109]:


#==========Dictionary=============#
# dict does not maintain the order
 
dict1 = {"key1":"val1","key2":"val2","key3":"val3"}
dict1


# In[110]:


dict1["key2"]


# In[111]:


dict2 = {"banglore":1,"hydrabad":2,"odisha":True}
dict2


# In[112]:


dict3 = {"india":"amirul","usa":"razika","canada":"rafika"}
dict3


# In[113]:


dict3


# In[115]:


dict3["india"]


# In[116]:


dict3["usa"]


# In[117]:


dict3["canada"]


# In[118]:


# if you check theat dataset seasons & players are dictionary type of data
# if you look at the pdict players names are key part:nos are the values
# dictionary can guide us which player at which level and which row
# main advantage of the dictionary is we dont required to count which no row which players are sitting


# In[119]:


Games


# In[121]:


Pdict


# In[127]:


# how do i know player kobebryant is a
Pdict["Sky"]


# In[128]:


Games[1]


# In[129]:


Games


# In[130]:


Pdict["Kohli"]


# In[131]:


Games


# In[132]:


Pdict["Dhoni"]


# In[133]:


Games


# In[134]:


Games[2]


# In[135]:


Games[Pdict["Dhoni"]]


# In[137]:


Points[Pdict["Dhoni"]]


# In[139]:


Salary[Pdict["Dhoni"]]


# In[140]:


Salary[2,4]


# In[141]:


Salary


# In[144]:


Salary[Pdict["Dhoni"]][Sdict["2018"]]


# In[145]:


Salary


# In[147]:


Salary[Pdict["Kohli"]][Sdict["2017"]]


# In[148]:


Salary/Games


# In[149]:


import numpy as np
import matplotlib.pyplot as plt


# In[150]:


get_ipython().run_line_magic('matplotlib.pyplot', 'as plt')


# In[152]:


Salary[8]


# In[154]:


Pdict


# In[153]:


plt.plot(Salary[8])


# In[157]:


plt.plot(Salary[0], c="green")


# In[162]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams["figure.figsize"] = 10,6


# In[165]:


plt.plot(Salary[0], c= "blue", ls = ":")


# In[167]:


plt.plot(Salary[0], c="red", ls = "--", marker = "o")# s - squares


# In[168]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams["figure.figsize"] = 10,8 ##runtime configuration parameter


# In[172]:


plt.plot(Salary[0], c= "blue", ls = ":", marker = "*", ms = 15)
plt.show


# In[173]:


list(range(0,9))


# In[174]:


Sdict


# In[175]:


Pdict


# In[179]:


plt.plot(Salary[7], c="gray" , ls = "--" , marker = "o", ms = 15)
plt.xticks(list(range(0,10)),Seasons)
plt.show()


# In[182]:


plt.plot(Salary[0], c="pink" , ls = ":" , marker = "*" , label =Players[8], ms = 15)
plt.xticks(list(range(0,10)), Seasons,rotation="vertical")
plt.show()


# In[183]:


Games


# In[185]:


Pdict


# In[188]:


plt.plot(Salary[0], c="Purple" , ls = "-." , marker = "*" , label =Players[8], ms = 15)
plt.xticks(list(range(0,10)), Seasons,rotation="horizontal")
plt.show()


# In[189]:


Salary[8]


# In[190]:


Salary[1]


# In[193]:


plt.plot(Salary[1], c= "red" , ls = ":" , marker = "*" , ms = 15, label = Players[1])


# In[194]:


# more visualization


# In[197]:


plt.plot(Salary[0], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[1])

plt.xticks(list(range(0,10)), Seasons,rotation="horizontal")
plt.show



# In[201]:


plt.plot(Salary[0], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "green" , ls = "-." , marker = "o" , ms = 10, label = Players[1])
plt.plot(Salary[2], c= "blue" , ls = "-" , marker = "s" , ms = 10, label = Players[2])

plt.xticks(list(range(0,10)), Seasons,rotation="horizontal")
plt.show


# In[206]:


plt.plot(Salary[0], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "yellow" , ls = "-." , marker = "o" , ms = 10, label = Players[2])
plt.plot(Salary[2], c= "green" , ls = "--" , marker = "D" , ms = 10, label = Players[3])
plt.plot(Salary[3], c= "blue" , ls = "-" , marker = "^" , ms = 10, label = Players[4])

plt.legend()
plt.xticks(list(range(0,10)), Seasons,rotation="vertical")

plt.show


# In[208]:


plt.plot(Salary[0], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "yellow" , ls = "-." , marker = "o" , ms = 10, label = Players[2])
plt.plot(Salary[2], c= "green" , ls = "--" , marker = "D" , ms = 10, label = Players[3])
plt.plot(Salary[3], c= "blue" , ls = "-" , marker = "^" , ms = 10, label = Players[4])

plt.legend(loc = "upper left",bbox_to_anchor=(0,0))
plt.xticks(list(range(0,10)), Seasons,rotation="vertical")

plt.show


# In[210]:


plt.plot(Salary[0], c= "red" , ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "yellow" , ls = "-." , marker = "o" , ms = 10, label = Players[2])
plt.plot(Salary[2], c= "green" , ls = "--" , marker = "D" , ms = 10, label = Players[3])
plt.plot(Salary[3], c= "blue" , ls = "-" , marker = "^" , ms = 10, label = Players[4])

plt.legend(loc = "lower right",bbox_to_anchor=(0.5,1))
plt.xticks(list(range(0,10)), Seasons,rotation="vertical")

plt.show


# In[219]:


plt.plot(Salary[0], c= "red" ,  ls = ":" , marker = "*" , ms = 10, label = Players[0])
plt.plot(Salary[1], c= "yellow", ls = "-." , marker = "o" , ms = 10, label = Players[1])
plt.plot(Salary[2], c= "green" , ls = "--" , marker = "D" , ms = 10, label = Players[2])
plt.plot(Salary[3], c= "blue" , ls = "-" , marker = "^" , ms = 10, label = Players[3])
plt.plot(Salary[4], c= "purple", ls = ":" , marker = "s" , ms = 10, label = Players[4])
plt.plot(Salary[5], c= "black" , ls = ":" , marker = "1" , ms = 10, label = Players[5])
plt.plot(Salary[6], c= "magenta" , ls = ":" , marker = "2" , ms = 10, label = Players[6])
plt.plot(Salary[7], c= "white" , ls = ":" , marker = "3" , ms = 10, label = Players[7])
plt.plot(Salary[8], c= "cyan" , ls = ":" , marker = "h" , ms = 10, label = Players[8])
plt.plot(Salary[9], c= "black" , ls = ":" , marker = "|" , ms = 10, label = Players[9])



plt.legend(loc = "upper right",bbox_to_anchor=(0.5,1))
plt.xticks(list(range(0,10)), Seasons,rotation="vertical")

plt.show


# In[220]:


# we can visualize the how many games played by a player
plt.plot(Games[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Games[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Games[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Games[3], c='Red', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Games[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Games[5], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Games[6], c='red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Games[7], c='Green', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Games[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Games[9], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[ ]:




