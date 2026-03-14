class Solution {
    public static int tribonacci(int n) {
        int f[]=new int[38];
        f[0]=0;
        f[1]=1;
        f[2]=1;
        int i=3;
        while(i<=n){
            f[i]=f[i-1] + f[i-2] + f[i-3];
            i+=1;
        }
        return f[n];
    }
}
