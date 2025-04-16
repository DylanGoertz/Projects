/*************
Name: Dylab Goertz
Program Name: Example7a
Date:10/4/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Example7a
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);
        String color1, color2, color3;

        out.print("\nEnter three colors: ");
        color1 = kb.next();
        color2 = kb.next();
        color3 = kb.next();

        out.println(color2+". "+color3+",");
        out.println("and "+color1+" were entered.\n");
    }
}
