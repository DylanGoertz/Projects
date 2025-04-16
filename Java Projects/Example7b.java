/*************
Name: Dylab Goertz
Program Name: Example7a=b
Date:10/4/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Example7a
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);
        double num1, num2, product;

        out.print("\nEnter two numbers: ");
        num1 = kb.nextDouble();
        num2 = kb.nextDouble();

        product = num1 * num2;

        out.println("The product of "+num1+" and "+num2+" is "+product+"\n");
    }
}