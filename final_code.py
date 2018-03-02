# ##Minsweeper with generator

from collections import Counter
import numpy
import math
from itertools import combinations
import copy
from itertools import combinations
from collections import Counter
import copy
import itertools
from itertools import chain
def mazegen():
    mazee=[[0, 1, 1, 1],
         [0, 1,10, 1],
         [1, 2, 1, 1],
         [1, 10,1 ,0]]
    return mazee
def minesweep():
    mazee=[["x", "x", "x", "x"],
         ["x", "x","x", "x"],
         ["x", "x", "x", "x"],
         ["x", "x","x","x"]]
    return mazee
    
## Discovering nearby nodes:
def neighbour(x,y):
    
    k=[]
    if x < (len(mazee)-1):
            k.append((x+1,y))
            while(y!=len(mazee)-1):
                k.append((x+1,y+1))
                break
        
    if x >0:
            k.append((x-1,y))
            if y>0:
                k.append((x-1,y-1))
                
            
    if y<(len(mazee)- 1):
            k.append((x,y+1))
            if x>0:
                k.append((x-1,y+1))
                
    if y >0:
            k.append((x,y-1))
            while(x!=len(mazee)-1) :
                k.append((x+1,y-1))
                break
    return k
def formdictionary(k):          
    i=0
    while(i<len(k)):## k consisit of co-ordinates neighbours
        t,p=k[i]
        val=(mazee[t][p])  ##value of the matrix
        dict2={(t,p):val}##value of cells and co-ordinates
        dict1.update(dict2)
        i=i+1    
    return dict1
def getallzeroneighbours(dict1):
    for key,value in dict1.items():
        if value==0:
            if key not in lval0:
                lval0.append((key))
    return lval0
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
   
def inference(nit,nt):
    po=[]
    for key,value in nt.items():    ### to get the all occurence of the unexplored node present in the list from all the equations and  
        for kt,v in value.items():  
            for k,y in v.items():
                if k==(1,2):
                    po.append(key)      
    mini=min(Counter(po),key=Counter(po).get)   ###select the one which is minimum
    for key,value in nt.items():                ###assume mine on the selected key and 
        if key==mini:
            for v in value.values():
                for k,vet in v.items():
                    if k==(1,2) and vet==1:
                        kl=0
            
def intelligenttracking(gd3,dict1,nit,mines):
    dictio={}
    for key,value in gd3.items():
        count1=0
        x3,y3=key
        k=neighbour(x3,y3)
        
        for each in k:
            if each in dict1:
                count1=count1+1
        for each in k:
            if each not in dict1:
                if len(k)-count1==1 and dict1[x3,y3]==1:
                    
                    j=0
                    while(j<len(nit)):
                        if nit[j]==each:
                            dictio={each:"t"}
                            dict1.update(dictio)
                            mines=mines-1
                            del nit[j]
                            #print("nitinis here")
                        j=j+1
           
    

    return dict1,mines

def satisifiability(gd3, dict1,unexplored1):
    dat = []
    for key,value in dict1.items():
        x6,y6 = key
        k = neighbour(x6,y6)
        for each in k:
            if each not in unexplored1:
            
                if dict1[each] == 't' and value ==1:

                    if gd3[key]!= []:
                        dat.append(gd3[key])
    
    #print (dat)
    each2 = (3,0)
    dictio={each2:'t'}
    dict1.update(dictio)
    dat1 = list(chain.from_iterable(dat))
    t4 = set(dat1)
    t4 = list(t4)
    for each in t4:
        print("Enter The following values for co-ordinates",each)
        aa =int(input())
        dictio={each:aa}
        dict1.update(dictio)

    return dict1
        
        
        
def turtles(dict1):
    #print("nitin")
    import turtle
    t=[]

    n=4
    dimen=n
    walls=[]
    k=[]
    i=0
    def drawGrid():
        
        turtle.penup()
        turtle.goto(0,0)
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.forward(n*n*n)
        turtle.right(90)
        turtle.forward(n*n*n)
        turtle.right(90)
        turtle.forward(n*n*n)
        turtle.right(90)
        turtle.forward(n*n*n)

    def drawColumns():
        for i in range(int(n/2)):
        
            #turtle.begin_fill()
            turtle.right(90)
            turtle.forward(64/4)
            turtle.right(90)
            turtle.forward(64)
            turtle.left(90)
            turtle.forward(64/4)
            turtle.left(90)
            turtle.forward(64)
        #turtle.end_fill()
     

    def drawRows():
        turtle.left(180)
        rows = 0 
        while rows <= (n/2)-1:
            rows += 1
            turtle.forward(64/4)
            turtle.right(90)
            turtle.forward(64)
            turtle.left(90)
            turtle.forward(64/4)
            turtle.left(90)
            turtle.forward(64)
            turtle.right(90)
    def drawwalls():
        #leng=[(0,2),(2,4),(3,3),(9,9)]
        #l.append((-300+0,250+0))
        #l.append((-300+(50*0),250-(50*2)))
        #l.append((-300+(50*1),250-(50*2)))
        #l.append((-300+(50*1),250-(50*4)))
        #l.append((-300+(50*7),250-(50*7)))
        for key,value in ne.items():
            e,r=key
            x=e+1
            y=r+1
            #for i in range(len(walls)):   
            #x,y=walls[i]
            #print (x,y)
            turtle.penup()
            turtle.goto(15*x,-15*y)
            turtle.pendown()
            turtle.write(value, move=False, align="right", font=("Arial", 10, "normal"))
            '''turtle.color("black")
            turtle.begin_fill()
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            turtle.end_fill()'''    
    drawGrid()
    drawColumns()
    drawRows()
    drawwalls()
    
    turtle.penup()
    turtle.goto(0,0)

    

def inference(nit,nt,kb):
    po=[]
    remaining_nodes=[]
    tr=0
    while(tr<4):
        
        for key,value in nt.items():    ### to get the all occurence of the unexplored node present in the list from all the equations and  
            for kt,v in value.items():  
                for k,y in v.items():
                    if k==nit[tr]:  ##first item in list nit
                        po.append(key)     

        mini=min(Counter(po),key=Counter(po).get) 
        

        ###select the parent node for which occurance of unexplored node is minimum
        for key,value in nt.items():
                                            ###assume mine on the selected key and 
            if key==mini:
                for infer in value.values():
                    for k,vet in infer.items():
                        
                        if k==nit[tr] and vet==1:
                            ##assumption of a mine
                            print("Enter The following values for co-ordinates", k)
                            remaining_nodes.append(k)
                            knowledgebase(key,infer,nit,nt,kb,k) ##send the parent node, global dictionary, list of unexplored coordinates, sub dictionary for mine assumed
        tr=tr+1
    #print("priting remaining nodes",remaining_nodes)
    return remaining_nodes
def knowledgebase(key,infer,nit,nt,kb,k1):
    #print(infer)             
    kb.update(infer)
    kbt={}
    dty={}
    temp=()
    cd={}
    combinationForCheck=[]
    listOfInferedNodes=[]
    for ke,value in nt.items():
        #print(ke)
        bool1= True
        combinationForCheck=[]
        listOfInferedNodes=[]
        if key!=ke:
            kbt={ke:value}
            qd=copy.deepcopy(kbt)
            cd.update(qd)
            #print(cd)
            ##dictionary having keys apart from present equation
            for key1,value1 in cd.items():  ##iterate in that dictionary to decide 
                dty.update(value1)
            #print(dty)
            for key3,value in dty.items():
                
                isthere = True
                #print(value)
 
                for k in infer.keys():
                    #print(k)
                    if k not in value.keys():
                    
                        isthere = False
                        break

    
                if isthere:
                    
                    t=(all(item in value.items() for item in infer.items()))
                    if(t):
                        
                        #print(" they're all here")
                        kb.update(value)
                       # bool1= False
                        break
                    else:
                        print("contradiction1")
                        re=int(input())
                        dictio={k1:re}
                        dict1.update(dictio)
                        #print (k1)
                        bool1= False
                        
                        kb={}
                        break
                if not bool1:
                    break
            if not bool1:
                break
        if not bool1:
            break
                
                        

                
            for key4,value in kb.items():
                listOfInferedNodes.append(key4)#print (listOfInferedNodes)
                
    #print(cd)
    #print(kb)
    result_list = list(map(dict, itertools.combinations( kb.items(), 2)))
    #print(result_list)
    kb6={}
    dty1={}
    for ke,value in nt.items():
        bool1= True
        combinationForCheck=[]
        listOfInferedNodes=[]
        if key!=ke:
            kbt={ke:value}
            qd=copy.deepcopy(kbt)
            cd.update(qd)
            ##dictionary having keys apart from present equation
            for key1,value1 in cd.items():  ##iterate in that dictionary to decide 
                dty.update(value1)
            for key3,value in dty.items():
                
                o=0
                while(o<len(result_list)):
                    
                    isthere = True
 
                    for k in result_list[o].keys():
                        if k not in value.keys():
                            
                            isthere = False
                            break

    
                    if isthere:
                        t=(all(item in value.items() for item in result_list[o].items()))
                   
                        if(t):
                            #print(value, result_list[o])
                            #print(" they're all here1")
                            kb.update(value)
                           # bool1= False
                            break
                        else:
                            print("contradiction2")
                            re=int(input())
                            dictio={k1:re}
                            dict1.update(dictio)
                            #print (k1)
                            bool1=False
                            kb={}
                            break
                    o=o+1
                    if not bool1:
                        break
                if not bool1:
                    break
            if not bool1:
                break
        if not bool1:
            break
                
                        

                
            for key4,value in kb.items():
                listOfInferedNodes.append(key4)#print (listOfInferedNodes)
                

              
                    
  
    #print (kb)

    

##main function
if __name__=='__main__':
    mines=1 ## please note: this is not the number of mines but a personal counter we set for looping
    
    kb={}
    print("what don you want the length of the board to be in dimension of X and Y")
    m=int(input("enter the M Value"))
    n=int(input("enter the N Value"))
    mazee1=minesweep()
    print("the board generated")
    print(numpy.matrix(mazee1))
    mazee=mazegen()
    print("enter the co-ordinates to start the game")
    x=int(input("enter the x Value"))
    y=int(input("enter the y Value"))
    while(mines!=0):
        safe=[]
        dict1={}
        dict2={}
        dicti3={}
        dictio={}
        dicti2={}
        gd={}
        unexp=[]
        t=[]
        lval0=[]
        unexplored=[]
        ne={}
        ner=[]
        k=neighbour(x,y)##call first node to ask for the user across the co-ordinate(X,Y)
        dict1=formdictionary(k)  ##building dictionary for all neighbouring nodes
        lval0=getallzeroneighbours(dict1) ##identify clear cells(0) across the whole board
        #dict1=checkforzeroinlist(lval0)
        j=0
        q={}
        kj={}
        nt={}
        while(j<len(lval0)):     ####revealing all the clue cells adjacent to clear cells
            x1,y1=lval0[j]
            k=neighbour(x1,y1) 
            dict1=formdictionary(k)
            lval0=getallzeroneighbours(dict1)
            j=j+1
        #print (dict1)               ##dictionary of all the clue cells and clear cells
        un={}
        gd2={}
        gd3={}
        for key,value in dict1.items():

            unexplored=[]
            if value!=0:
                x1,y1=key
                #print("this is parent co-ordinate")
                #print(x1,y1)
                count=0
                k=neighbour(x1,y1)
                #print ("these are the unexlpored neighbours")
                for each in k:                        ###we are finding the unexplored nodes particular to the parent node

                    if each not in dict1:
                        count=count+1
                        unexplored.append(each)
                        unexp.append(each)
                un={(x1,y1):unexplored}              ##x1,y1 is parent node and unexp is the list of unexplored nodes 
                gd2=copy.deepcopy(un)               ##gd3 is dictionary of parent node and unexplored nodes
                gd3.update(gd2)        
                #print(unexplored)
                #print(nCr(count,value))
                t=list(combinations(unexplored,value))   ##formation of equations of possibility of mine based on the value of the parent(clue cell)
                j=0
                gd={}
                dicti2={}
                dicti0={}
                while(j<len(t)):
                    for each in unexplored:
                        if each not in t[j]:

                            dictio={each:-1}
                        else:
                            dictio={each:1}

                        dicti2.update(dictio)


                    d={"s%d"%j:dicti2}
                    gd1=copy.deepcopy(d)
                    gd.update(gd1)      ##gd is the small dictionary corresponding to that equation
                    j=j+1
                #print (gd)
                q={(x1,y1):gd}
                kj=copy.deepcopy(q)    
                nt.update(kj)           ##nt is the global dictionary of equations of all clue(parent) cells with co-ordinates
                print("\n")
                #print(gd3)
                y=(unexp)         ##maximum degree heuristic (most constrained variable) is the value we are taking as an assumptiom for mine
                #print(list(y))
                mal = {x:y.count(x) for x in y}
                nit=sorted(mal, key=mal.get,reverse=True)
                ty=sorted(mal, key=mal.get,reverse=False)
                
                                ##nit get the most constrained variable and use at as guess of  mine (CSP)
                #print((nitin))
        #print((gd3)) ##this is to print dictionary of parent nodes and unexlpored nodes
        #print(nt)                   ##nt is the global dictionary
        #print(nit)
        #print("\n")
        for key,value in dict1.items():
            x1,y1=key
            
            mazee1[x1][y1]=value
        ne=dict1
        print(numpy.matrix(mazee1))
        print("pritning nit and nt",nit,nt)
        
        remaining_nodes=inference(ty,nt,kb)
        for each in ty:
            if each not in remaining_nodes:
                ner.append(each)
        #print("ner",ner)
        for key,value in dict1.items():

            unexplored=[]
            if value!=0:
                x1,y1=key
                #print("this is parent co-ordinate")
                #print(x1,y1)
                count=0
                k=neighbour(x1,y1)
                #print ("these are the unexlpored neighbours")
                for each in k:                        ###we are finding the unexplored nodes particular to the parent node

                    if each not in dict1:
                        count=count+1
                        unexplored.append(each)
                        unexp.append(each)
                un={(x1,y1):unexplored}              ##x1,y1 is parent node and unexp is the list of unexplored nodes 
                gd2=copy.deepcopy(un)               ##gd3 is dictionary of parent node and unexplored nodes
                gd3.update(gd2)
        #print("gd3",gd3)
        dict1,mines=intelligenttracking(gd3,dict1,ner,mines)
        #print(dict1)
        for key,value in dict1.items():
            x1,y1=key
            mazee1[x1][y1]=value
        print(numpy.matrix(mazee1))
        for key,value in dict1.items():

            unexplored=[]
            if value!=0:
                x1,y1=key
                #print("this is parent co-ordinate")
                #print(x1,y1)
                count=0
                k=neighbour(x1,y1)
                #print ("these are the unexlpored neighbours")
                for each in k:                        ###we are finding the unexplored nodes particular to the parent node

                    if each not in dict1:
                        count=count+1
                        unexplored.append(each)
                        unexp.append(each)
                un={(x1,y1):unexplored}              ##x1,y1 is parent node and unexp is the list of unexplored nodes 
                gd2=copy.deepcopy(un)               ##gd3 is dictionary of parent node and unexplored nodes
                gd3.update(gd2)
        unexplored1 = []
        for key,value in dict1.items():
        
            x8,y8 = key
            k = neighbour(x8,y8)
            for each in k:
                if each not in dict1:
                    unexplored1.append(each)
        unexplored1 = set(unexplored1)
        unexplored1 = list(unexplored1)

        dict1 = satisifiability(gd3, dict1,unexplored1)
        for key,value in dict1.items():
            x1,y1=key
            mazee1[x1][y1]=value
        print(numpy.matrix(mazee1))
        
        
        turtles(dict1)
        
   
