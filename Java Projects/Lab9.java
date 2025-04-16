/*************
Name: Dylab Goertz
Program Name: Lab9
Date:9/30/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Lab9
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);

        out.print("\nHello. What's your name?");
        String name = kb.next();

        out.print("Hi, "+name+". How old are you? ");
        int age = kb.nextInt();

        out.println("So you're "+age+",eh? That's not old at all!");

        out.println("How much do you make," +name+"?" );

        out.println("$8.50! I hope that's per hour and not per year! LOL!\n");
    }
}        