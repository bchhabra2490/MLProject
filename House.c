

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

float hypo(float * newData,float * theta,int attr){
    float ans=theta[0];
    for(int i=0;i<attr;i++){
        ans+=newData[i]*theta[i+1];
    }
    return ans;
}

float normalise(float data[][9],int num, int attr){
    float mean[attr],std[attr],sigma;
    for(int i=0;i<attr;i++){
        mean[i]=0;
        for(int j=0;j<num;j++){
            mean[i]=mean[i]+data[j][i];
        }
        mean[i]=mean[i]/num;
    }
    for(int i=0;i<attr;i++){
        sigma=0;
        std[i]=0;
        for(int j=0;j<num;j++){
            sigma=sigma+pow(data[j][i]-mean[i],2);
        }
        sigma=sigma/num;
        std[i]=pow(sigma,0.5);
    }
    for(int i=0;i<num;i++){
        for(int j=0;j<attr;j++){
            data[i][j]=(data[i][j]-mean[j])/std[j];
        }
    }
    printf("Mean\tStandard Deviation\n");
    for(int i=0;i<attr;i++){
        printf("%f\t%f\n",mean[i],std[i]);
    }
    for(int i=0;i<num;i++){
        for(int j=0;j<attr;j++){
            printf("%f ",data[i][j]);
        }
        printf("\n");
    }
    return 0;
}

void updateTheta(float data[][9],float * theta,int attr,int m,float * price){
    float sigma=0;
    float alpha=0.001;
    for(int j=0;j<attr+1;j++){
        for(int i=0;i<m;i++){
            if(j!=0){
                sigma+=(hypo(data[i],theta,attr)-price[i])*data[i][j-1];
            }else{
                sigma+=(hypo(data[i],theta,attr)-price[i]);
            }
        }
        theta[j]=theta[j]-(alpha*sigma)/m;
    }
}

float costFunction(float data[][9],float * theta,float * price,int m,int attr){
    float sigma=0;
    for(int i=0;i<m;i++){
        sigma+=pow(hypo(data[i],theta,attr)-price[i],2);
    }
    float cost=sigma/(2*m);
    return cost;
}

void minCost(float data[][9],float * theta,float * price,float m,float attr){
    float lastCost=costFunction(data,theta,price,m,attr);
    updateTheta(data,theta,attr,m,price);
    float newCost=costFunction(data,theta,price,m,attr);
    while(lastCost>newCost){
        lastCost=costFunction(data,theta,price,m,attr);
        updateTheta(data,theta,attr,m,price);
        newCost=costFunction(data,theta,price,m,attr);
    }
}

int main() {
    int m,attr;
    printf("Enter the number of data sets.\n");
    scanf("%d",&m);
    printf("Enter the number of attributes(press 9).\n");
    scanf("%d",&attr);
    float data[m][attr],newData[attr],theta[attr+1],price[m];
    for(int i=0;i<m;i++){
        printf("Enter the data set.\n");
        for(int j=0;j<attr;j++){
            scanf("%f",&data[i][j]);
        }
        printf("Enter the price(y value)\n");
        scanf("%f",&price[i]);
    }
    normalise(data,m,attr);
    for(int i=0;i<attr+1;i++){
        theta[i]=1;
    }
    minCost(data,theta,price,m,attr);
    printf("The value of theta's is-");
    for(int i=0;i<attr+1;i++){
        printf("%f ",theta[i]);
    }
    printf("\n");
    printf("Enter the new attribute data set.\n");
    for(int i=0;i<attr;i++){
        scanf("%f",&newData[i]);
    }

    float ans=hypo(newData,theta,attr);
    printf("Price of the new property is %f\n",ans);
    return 0;
}
