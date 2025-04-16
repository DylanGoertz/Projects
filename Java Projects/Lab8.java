/*************
Name: Dylab Goertz
Program Name: Lab8
Date:9/30/2022
*******************/
import java.util.Scanner;

public class Lab8
{
    public static void main(String[] args)
    {
        Scanner keybaord = new Scanner(System.in);

        System.out.print("\nGive me a word! ");
        keybaord.next(); //alows inout of a word

        System.out.print("Give me a second word! ");
        keybaord.next(); //alows inout of an integer

        System.out.print("Great, now your favorite integer number? ");
        keybaord.next(); //alows inout of a fractional value

        System.out.print("And your favorite floating-point value... ");
        keybaord.next(); //alows inout of a word

        System.out.print("\nWhew! Wasn't that fun? ");
    }
}