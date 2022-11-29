##############################
####  AUTHOR: MADHU VP #######
############################## 

f = open('/species.json')
species = json.load(f)


##############################################################   BARKTYPE    ###############################################################

barktypes= []
for num in range(len(species['data'])):
    found = species['data'][num]['BARK_TYPE'].split(',')
    barktypes+=found
#count distinct occurrences
dictforcount = {}
count = 0
for bark in barktypes:
  bark = bark.strip()
  if bark:
    if bark in dictforcount:
      dictforcount[bark] +=1
    else:
      dictforcount[bark] =1
  else:
    count+=1
print("\n\nCount of Barktypes",dictforcount)
print("Count of blank barktypes: ",count)
#visualization
categories = list(dictforcount.keys())
count = list(dictforcount.values())
fig = plt.figure(figsize = (25, 5))
plt.bar(categories, count, color ='crimson',
        width = 0.4)
plt.xlabel("Bark types")
plt.ylabel("Count")
plt.title("Count of Barktypes")
plt.show()


##############################################################   NEEDLE TRAITS(CONIFER)    ###############################################################


#counting needle traits
needletraits= []
for num in range(len(species['data'])):
  if("NEEDLE_TRAITS" in species['data'][num]):
    found2 = species['data'][num]['NEEDLE_TRAITS'].split(',')
    needletraits+=found2

dictforcount2 = {}
count = 0
for needle in needletraits:
  needle = (needle.strip()).lower()
  if needle:
    if needle in dictforcount2:
      dictforcount2[needle] +=1
    else:
      dictforcount2[needle] =1
  else:
    count+=1

print("\n\nCount of Needles: ",dictforcount2)
print("Count of blank needles: ", count)
#visualization
categories = list(dictforcount2.keys())
count = list(dictforcount2.values())
fig = plt.figure(figsize = (38, 10))
plt.bar(categories, count, color ='blue',
        width = 0.5)
plt.xlabel("Needle Traits")
plt.ylabel("Count")
plt.title("Count of Needle Traits (Conifer)")
plt.show()

##############################################################   LEAFTYPE(BROADLEAF)    ###############################################################


#counting leaftypes

leaftype= []
for num in range(len(species['data'])):
  if("LEAF_TYPE" in species['data'][num]):
    found3 = species['data'][num]['LEAF_TYPE'].split(',')
    leaftype+=found3

dictforcount3 = {}
count = 0
for leaf in leaftype:
  leaf = (leaf.strip()).lower()
  if leaf:
    if leaf in dictforcount3:
      dictforcount3[leaf] +=1
    else:
      dictforcount3[leaf] =1
  else:
    count+=1

print("\n\nCount of Leaftypes: ",dictforcount3)
print("Count of blank leaftypes: ", count)

#visualization
categories = list(dictforcount3.keys())
count = list(dictforcount3.values())
fig = plt.figure(figsize = (20, 5))
plt.bar(categories, count, color ='green',
        width = 0.4)
plt.xlabel("Leaf Type")
plt.ylabel("Count")
plt.title("Count of Leaftypes(Broadleaf)")
plt.show()


##############################################################   DIRECTION    ###############################################################

#count cone features - counting directions
c_directioncol= []
c_directions = []
for num in range(len(species['data'])):
  if("CONE" in species['data'][num]):
    found4 = species['data'][num]['CONE'].split(',')[0]
    c_directioncol.append(found4)

for direction in c_directioncol:
  dirnow = (re.split(r'/',(direction.strip()).lower()))
  c_directions+=dirnow

dictforcount4 = {}
count = 0
for dir in c_directions:
  dir = (dir.strip()).lower()
  if dir:
    if dir in dictforcount4:
      dictforcount4[dir] +=1
    else:
      dictforcount4[dir] =1
  else:
    count+=1

print("\n\nCount of Directions: ",dictforcount4)
print("Count of blank dirctions: ", count)
#visualization
categories = list(dictforcount4.keys())
count = list(dictforcount4.values())
fig = plt.figure(figsize = (20, 5))
plt.bar(categories, count, color ='purple',
        width = 0.4)

plt.xlabel("Direction")
plt.ylabel("Count")
plt.title("Count of Cone Directions")
plt.show()

##############################################################   SHAPE    ###############################################################


#counting cone features - shapes
c_shapecol = []
c_shapes = []
for num in range(len(species['data'])):
  if("CONE" in species['data'][num]):
    found5 = species['data'][num]['CONE'].split(',',2)[1:2]
    c_shapecol+=found5

for shape in c_shapecol:
  shapenow = (re.split(r'/',(shape.strip()).lower()))
  c_shapes+=shapenow

dictforcount5 = {}
count_s = 0
for sh in c_shapes:
  if sh:
    if sh in dictforcount5:
      dictforcount5[sh] +=1
    else:
      dictforcount5[sh] =1
  else:
    count_s+=1

print("\n\nCount of Shapes: ",dictforcount5)
print("Count of blank shapes: ", count_s)
#visualization
categories = list(dictforcount5.keys())
count = list(dictforcount5.values())
fig = plt.figure(figsize = (29, 5))
plt.bar(categories, count, color ='olive',
        width = 0.4)

plt.xlabel("Shape")
plt.ylabel("Count")
plt.title("Count of Shapes")
plt.show()


##############################################################   COLOR    ######################################################################

c_colorcol = []
c_colors =[]

#separate colors from cone features. This includes slashes
for num in range(len(species['data'])):
  if("CONE" in species['data'][num]):
    found5 = re.split(r',',species['data'][num]['CONE'])[2:3]
    c_colorcol+=found5

#separate each color from color column, (without slashes)
for color in c_colorcol:
  colornow = (re.split(r'/',(color.strip()).lower()))
  c_colors+=colornow



#count each color
dictforcount6 = {}
count_c = 0
for col in c_colors:
  if col:
    if col in dictforcount6:
      dictforcount6[col] +=1
    else:
      dictforcount6[col] =1
  else:
    count_c+=1
print("Count of blank colors: ", count_c)
print("\nList: ",dictforcount6)


#visualization
categories = list(dictforcount6.keys())
count = list(dictforcount6.values())
fig = plt.figure(figsize = (29, 5))
plt.bar(categories, count, color ='turquoise',
        width = 0.4)

plt.xlabel("Color")
plt.ylabel("Count")
plt.title("Count of Colors")
plt.show()

