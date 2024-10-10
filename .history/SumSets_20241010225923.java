public class SumSets {
    
    public static void main(String[] args) {
        boolean res;
        res = isSumStr("1212243660");
        System.out.println(res==true ? true : false);
    }

    private static boolean isSumStr(String s){
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

    private static boolean check(String s,int beg,int len1,int len2){
        String s1= s.substring(beg,beg+len1);
        String s2 = s.substring(beg+len1, beg+len1+len2);

        String s3 = sub_sum(s1,s2);

        int s3len = s3.length();

        if(s3len>s.length() -len1-len2 -beg)
          return false;
          
        
       if(s3.equals(s.substring(beg+len1+len2,beg+len1+len2+s3len))){
            if()
       }
    }
}
