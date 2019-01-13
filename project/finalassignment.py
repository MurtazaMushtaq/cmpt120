#####################################################################################################
####                             CMPT 120 Final Project (Scantron)                               ####
####                             Authors:  Murtaza Mushtaq(301347189)                            ####
####                                       Taalib Bhatti(301324537)                              ####
####                                       Todor Baljak (3013332526)                             ####
#####################################################################################################


maxi=0     #This variable gives the maximum number of points obtained
avg=0      #This variable gives the average marks of the test
t=""       #this string "t" will be used to make a string of the right answers in alphabets form
kl=[]      #this list will be filled with the points obtained by each student depending on the number of right answers they give.
c=0        #"c" will be used to count the maximum points of the exam
final_output_in_excel=[]        #this list will be filled with data depending on the user's choice
percent_range=[10,20,30,40,50,60,70,80,90,100] #this is the range of percentages for the result


def read_string_list_from_file(the_file):
    fileRef=open(the_file,"r")
    localList=[]
    for line in fileRef:
        string=line[0:len(line)-1]
        localList.append(string )          
    fileRef.close()
    print("\n JUST TO TRACE, the local list of strings is:\n")
    for element in localList:
        print(element)
    return localList

def write_result_to_file(lres,the_file):
    '''
    Creates a text output file from a list of strings
    AUTHOR: Diana Cukierman
    
    Assumptions:
    1) lres is a list of strings, where each string
       will be one line in the output file
    2) the_file will contain the name fo the output file.
       for this porgram it shoudl be a name with .csv extension
    3) it is assumed that each string in lres already includes
       the character "\n" at the end
    4) the resulting file will be in the same directory (folder) as this program 
    5) the resulting file will  contain one student data per line 
    '''
    
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
                                    
    fileRef.close()
    return

def studs_in_range(g):
    c1=0       #"c1" will be used to count the students in range 0-10
    c2=0       #"c2" will be used to count the students in range 10-20
    c3=0       #"c3" will be used to count the students in range 20-30
    c4=0       #"c4" will be used to count the students in range 30-40
    c5=0       #"c5" will be used to count the students in range 40-50
    c6=0       #"c6" will be used to count the students in range 50-60
    c7=0       #"c7" will be used to count the students in range 60-70
    c8=0       #"c8" will be used to count the students in range 70-80
    c9=0       #"c9" will be used to count the students in range 80-90
    c10=0      #"c10" will be used to count the students in range 90-100


    for i in range(len(g)):
        if(g[i] >=0 and g[i]<=10):
            c1=c1+1
        if(g[i] >10 and g[i]<=20):
            c2=c2+1
        if(g[i] >20 and g[i] <=30):
            c3=c3+1
        if(g[i] >30 and g[i] <=40):
            c4=c4+1
        if(g[i] >40 and g[i] <=50):
            c5=c5+1
        if(g[i] >50 and g[i] <=60):
            c6=c6+1
        if(g[i] >60 and g[i] <=70):
            c7=c7+1
        if(g[i] >70 and g[i] <=80):
            c8=c8+1
        if(g[i] >80 and g[i] <=90):
            c9=c9+1
        if(g[i] >90 and g[i] <=100):
            c10=c10+1
    ctot=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
    return ctot

def end_message(s):
    print()
    print("All stats are done, bye!")

def turtle_bars(y):
    import turtle as t
    t.fd(500)
    t.backward(500)
    t.left(90)
    t.fd(300)
    t.backward(300)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.begin_fill()
    t.fillcolor("red")
    for i in range(len(y)):
        t.fd(y[i]*10)
        t.right(90)
        t.fd(30)
        t.right(90)
        t.fd(y[i]*10)
        t.left(90)
        t.fd(20)
        t.left(90)
    t.end_fill()
    t.ht()




l=read_string_list_from_file("IN_data_studs.txt")     #"l" is the list of all students and their answers
x=read_string_list_from_file("IN_key+pts.txt")        #"x" is the list of all right answers and the points assigned to each questiom


print("")
print("         WELCOME TO THE CMPT 120 Scantron Processing Program!!!")
print("         ======================================================")
print("")
print("The data files in this folder are",len(l))
print("There are",len(x[0]) ,"questions")
print("The answer key is:")
for i in range(len(x[0])):
    if(int(x[0][i])==1):
        t=t+"A"+" "
    if(int(x[0][i])==2):
        t=t+"B"+" "
    if(int(x[0][i])==3):
        t=t+"C"+" "
    if(int(x[0][i])==4):
        t=t+"D"+" "
    if(int(x[0][i])==5):
        t=t+"E"+" "
print(t)
print("The points are:")
g=x[1].split()       
for i in range(len(g)):
    g[i]=float(g[i])           #this loop is to change all the points to float
for q in g:
    print(str(q)+" ",end="")
for i in range(len(g)):
    c=c+g[i]
print()
print("The maximum points available are", c)
print()
print("You have to choose one of the two options")
print("Type ALL if you want to process all students")
print("Type SEL if you want to process selected students")
for i in range(len(l)):
    l[i]=l[i].split()
w=input("Type here:")
while(w.upper() !="ALL" and w.upper() !="SEL"):
    w=input("PLEASE TYPE IN ALL OR SEL!:")
if(w.upper()=="ALL"):
    print("All students have been processed")
    print()
    print("Here are the results that will be saved in the folder")
    print()
    alsl=[0]*len(x[0])    #this list will contain the number of times each question was answered correctly
    for i in range(len(l)):
        cou=0
        for k in range(len(l[i][1])):
            if(l[i][1][k]==x[0][k]):
                cou=cou+g[k]
                alsl[k]+=1
        kl.append([cou,k])
        kim="\""+l[i][0]+"\","+str(cou)+","+str(float(int((cou/c*100))))              #kim is the name, points obtained and the percentage obtained by each student
        print(kim)
        final_output_in_excel.append(kim)               #this is creating a list witl all student names, marks and percentage
        final_output_in_excel.append("\n")
        print()
if(w.upper()=="SEL"):
    stud=""
    alsl=[0]*len(x[0])
    while stud.upper()!="END":
        stud=input("Type a name or END to finish ==> ")
        if stud.upper()!="END":
            sin=0
            for i in range(len(l)):
                if l[i][0]==stud:
                    sin=1
                    cou=0
                    for k in range(len(l[i][1])):
                        if(l[i][1][k]==x[0][k]):
                            cou=cou+g[k]
                            alsl[k]+=1
                    kl.append([cou,i])
                    print("Student",l[i][0],"got",cou,"points")
            if sin==0:
                print("student not in database, type again")
    print("All your selected students have been processed!")
    print()
    print()
    print(" Here is the output that will be saved in the folder!")
    print()
    for i in range(len(kl)):
        kim="\""+l[kl[i][1]][0]+"\","+str(kl[i][0])+","+str(float(int((kl[i][0]/c*100))))
        print(kim)
        final_output_in_excel.append(kim)
        final_output_in_excel.append("\n")
        print()        
write_result_to_file(final_output_in_excel, "OUT_results.csv")
for i in range(len(kl)):
    if(kl[i][0]>=maxi):
        maxi=kl[i][0]
for i in range(len(kl)):
    avg=avg+kl[i][0]
avg=float(avg/len(kl))
print()
print("Here are the statistics")
print()
print("The maxiimum points are:", maxi)
print("The average points are:", avg)
print("The number of students processed are:", len(kl))
print("The number of times each question was answered correctly:")
print(alsl)
min1=[0]
mini=len(x[0])
for i in range(len(alsl)):
    if(alsl[i]<mini):
        mini=alsl[i]
        min1[0]=i+1
for i in range(len(alsl)):
    if alsl[i]==mini and i+1 not in min1:
        min1.append(i+1)
print("The most difficult question"+"s"*(len(min1)>1), min1)
for i in range(len(kl)):
    kl[i]=kl[i][0]
for i in range(len(kl)):
    kl[i]=(kl[i]/25)*100
list_total=studs_in_range(kl)
print("Distribution points are",list_total)
print("Considering the ranges",percent_range)
graph=input("Would you like to plot a graph of the distribution?, Y/N:")
if(graph.upper()=="Y"):
    graphplot=turtle_bars(list_total)
distance=input("Would you like to calculate the distance between the questions? Y/N:")
if(distance.upper()=="Y"):
    print()
    print("Special analysis 2 questions!")
    print()
    print("This will provide a 'distance' between two questions by accumulating the distance within each student, for all students.")    

endingmsg=end_message(kl)


