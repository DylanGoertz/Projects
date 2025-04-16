/*************
Name:Dylab Goertz
Program Name:Lab11
Date:10/4/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Lab11
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);
        double num1, num2, num3, avg;

        out.print("\nGive me three grades: ");
        num1 = kb.nextDouble();
        num2 = kb.nextDouble();
        num3 = kb.nextDouble();
        avg = num1 + num2 + num3 / 3;

        out.println("The average of " +num1+ ", " +num2+ ", and " +num3+ " = " +avg+"\n");
    }
}


