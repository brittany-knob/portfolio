#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
   
    fin.open("rawdata.dat");
    if (fin.fail())
    {
        cout<<"input file opening failed.\n";
        exit(1);
    }

double a[21][21];

/* the data in rawdata.dat are now saved in a matrix a whose first column is
 the x data and the second column is the y data */
int i, j;
for (i=0; i<21; i++)
for (j=0; j<2; j++)
fin >> a[i][j];

    fout.open("output.dat");
    if (fout.fail())
    {
        cout<<"output file opening failed.\n";
        exit(1);
    }
  
// the least squares method 
double sumx=0, sumxy=0, st=0, sumy=0, sumx2=0, sr=0, a1, a0, r2, xm, ym, x[21], y[21];

for (i=0; i<21; i++)
{
x[i]=a[i][0];
y[i]=a[i][1];  
}

for (i=0; i<21; i++)
{
    sumx=sumx+x[i];
    sumy=sumy+y[i];
    sumxy=sumxy+x[i]*y[i];
    sumx2=sumx2+x[i]*x[i];
}

xm=sumx/21;
ym=sumy/21;
a1=(21*sumxy-sumx*sumy)/(21*sumx2-sumx*sumx);
a0=ym-a1*xm;

for (i=0; i<21; i++)
{
    st=st+(y[i]-ym)*(y[i]-ym);
    sr=sr+(y[i]-a1*x[i]-a0)*(y[i]-a1*x[i]-a0);
}

r2=(st-sr)/st;

cout<<r2<<"\n"<<a0<<"\n"<<a1<<"\n";

fout<<r2<<"\n"<<a0<<"\n"<<a1<<"\n";

    fin.close();
    fout.close();
   
    cout<<"end of program.\n";
    return 0;
}





