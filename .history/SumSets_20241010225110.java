public class SumSets {
    
    public static void main(String[] args) {
        boolean res;
        res = isSumStr("1212243660");
        System.out.println(res==true ? true : false);
    }

    private void isSumStr(String s){
        int n = s.length();

        for(int i =0;i<n;i++){
            for(int  j=0;i+j<n;j++){
                if(check(s,0,i,j)){
                    return true;
                }
            }
        }
        return false;
    }
}
