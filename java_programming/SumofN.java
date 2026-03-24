import java.util.Scanner;
public class SumofN{
    public static int sum(int k){
        if(k==0 || k==1)
            return k;
        else{
            return k+sum(k-1);
        }
    }
    public static void main(String[] args){
        int k;
        System.out.println("Enter the number: ");
        Scanner sc=new Scanner(System.in);
        k=sc.nextInt();
        int sum= sum(k);
        System.out.println("The sum of "+k+" numbers is: "+sum);
        sc.close();

    }
}