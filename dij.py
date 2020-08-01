import math
counter=-1
def distance(c1,c2):
    x1,y1,x2,y2 = c1[0],c1[1],c2[0],c2[1]
    dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return dist


class elements:
    def __init__(self,name,cord,cost=None,neigbour=None):
        self.name=name
        self.cord=cord
        self.cost=cost
    
    def find_cost(self):
        cost=[]
        for i in  self.neigbour:
            cost.append(distance(self.cord,i.cord))
        self.cost=cost    
    
    def print_neigbour(self):
        a=[]
        a=[i.cost for i in self.neigbour]
        b=min(a)
        b=b[0]
        for i in self.neigbour:
            if b== i.cost[0]: 
                return i,b 
        
    
    

house = elements("house",(1,-2))
rest = elements("rest",(3,2))
inter = elements("inter",(0,3))
school = elements("school",(-2,0))
college = elements("college",(-2,-2))

obj=[house,rest,inter,school,college]

house.neigbour=[rest,college]
house.find_cost()
rest.neigbour=[inter]
rest.find_cost()
inter.neigbour=[school]
inter.find_cost()
school.neigbour=[house]
school.find_cost()
college.neigbour=[school]
college.find_cost()
#print(house.cost,rest.cost,inter.cost,school.cost,college.cost)
dict1={}
for i in obj:
    dict1[i.name] = 1000
dict1['house']=0
counter = -1
def get():
    global counter
    counter=counter+1
    lis=sorted(dict1.items(),key=lambda X: X[1])
    return lis[counter][0],lis[counter][1]
  
def match(component):
    for i in obj:
        if component == i.name:
            return i    

for i in range(0,5):
    component,du=get()
    obj_1=match(component)
    (obj_1.name)
    nbr,cost=obj_1.print_neigbour()
    a=(nbr.name)
    dv = dict1[a]
    if dv>cost+du:
        dv= cost + du
        dict1[a]=dv
print(dict1.items())
print(house.cost)




