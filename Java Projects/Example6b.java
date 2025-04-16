/*************
Name: Dylab Goertz
Program Name: Example6b
Date:9/30/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Example6b
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);

        out.print("\nHello. What's your first name/");
        String name = kb.next(): // next() only allows input of a word

        out.print("Hi, "+name+". How many people live in your house? ");
        int people = kb.nextInt();

        out.println(people +" people is a full house. ");

        out.println(name +", how many fluid ounces of water do you drink? ");
        double fl_oz = kb.nextDouble();

        out.println("Hopefully that is "+fl_oz+" fluid ounces per hour\n");
    }
}