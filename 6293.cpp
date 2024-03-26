#include<stdio.h>

int N,S,P,A[55];

int main() {
    scanf("%d%d%d",&N,&S,&P);
    for(int i=1;i<=N;++i) scanf("%d",&A[i]);
    if(N==0){
        printf("1");
        return 0;
    }
    if(A[N]>=S){
        if(N==P){
            printf("-1");
            return 0;
        }
        int ans=N;
        while(A[ans]==S)ans--;
        printf("%d",ans+1);
        return 0;
    }
    for(int i=N-1;i>=1;--i){
        if(A[i]>S){
            printf("%d", i+1);
            return 0;
        }
    }
    printf("1");
}
