
def read_file():
    infile = open("input_file.txt","r")
    mylist = []
    for line in infile:
        mylist = mylist + [int(line)]
    infile.close()
    return mylist

def sort(mylist1):
    for i in range(1, len(mylist1)):
        key = mylist1[i]
        j = i - 1
        while j >=0 and key < mylist1[j] :
            mylist1[j+1] = mylist1[j]
            j =j - 1
        mylist1[j+1] = key
    return mylist1

def repeated(mylist1):
    size = len(mylist1)
    mylist2 = []
    for i in range(0,size):
        count = 0
        for j in range(i+1,size):
            if mylist1[i]==mylist1[j]:
                count = count+1
        if count == 0:
            mylist2 = mylist2 + [mylist1[i]]
    return mylist2

def find_average(mylist2):
    total = 0
    for i in mylist2:
        i=float(i)
        total = total + i
    average = total/len(mylist2)
    return average


def above(mylist2,average):
    upper_list=[]
    for i in range(len(mylist2)):
        if mylist2[i] > average:
            upper_list=upper_list+[mylist2[i]]
    return upper_list

def below(mylist2,average):
    lower_list=[]
    for i in range(len(mylist2)):
        if mylist2[i]< average:
            lower_list=lower_list+[mylist2[i]]
    return lower_list

def output_file(mylist,mylist1,mylist2,average,above,below):  
    outfile = open("output_file.txt","w")
    
    outfile.write("Numbers Read:\n")
    for i in mylist:
        outfile.write(str(i) + " ")
    
    outfile.write("\n\nSorted:\n")
    for i in mylist1:
        outfile.write(str(i)+ " ")
    
    outfile.write("\n\nDistinct Numbers:\n")
    for i in mylist2:
        outfile.write(str(i)+" ")

    average = format(average,".3f")
    outfile.write("\n\nCalculated Average:")
    outfile.write(str(average))
    
    total_distinct=len(mylist2)
    outfile.write("\nTotal Distinct numbers:")
    outfile.write(str(total_distinct))

    outfile.write("\n\nAbove Average\tBelow Average\n")
    if len(above)> len(below):

        for x in range(len(below)):
            outfile.write(str(above[x]) + "\t\t" + str(below[x]) + "\n")

        for y in range(len(below), len(above)):
            outfile.write(str(y) + "\n")

    elif len(above) < len(below):

        for x in range(len(above)):
            outfile.write(str(above[x]) + "\t\t" + str(below[x]) + "\n")

        for y in range(len(above), len(below)):
            outfile.write("\t\t"+str(y)+"\n")
    else:
        for x in range(len(above)):
            outfile.write (str(above[x])+"\t\t"+str(below[x])+"\n")
    outfile.close()
    
def main():
    a = read_file()
    a_0 = read_file()
    b = sort(a_0)
    c = repeated(b)
    d = find_average(c)
    e = above(c,d)
    f = below(c,d)
    output_file(a,b,c,d,e,f)
main()


