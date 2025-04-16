/*************
Name:Dylab Goertz
Program Name:Lab13
Date:10/18/2022
*******************/
import static java.lang.System.*;
import java.util.Scanner;
public class Example9
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);
        double Volume, Lsa ;
        int height, radius ;

        out.print("\nEnter height of cylinder: ");
        height = kb.nextInt();
        out.print("Enter radius of cylinder: ");
        radius = kb.nextInt();

        Volume = Math.PI * Math.pow(radius , 2) * height;

        out.println("Volume of cylinder:" + Volume );

        Lsa = 2 * Math.PI * radius * height;
        
        out.println("Lateral surface of cylinder:" + Lsa +"\n");
    }
}
