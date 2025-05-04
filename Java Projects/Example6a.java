/*************
Name: Dylab Goertz
Program Name: Example6a
Date:9/30/2022
*******************/
import java.util.Scanner;

public class Example6a
{
    public static void main(String[] args)
    {
        Scanner keyboard = new Scanner(System.in);

        System.out.print("\nWhat city is the capitol of France? ");
        keyboard.next(); //alows inout of a word

        System.out.print("what is 6 multiplied by 7? ");
        keyboard.next(); //alows inout of an integer

        System.out.print("Enter a number between 0.0 and 1.0: ");
        keyboard.next(); //alows inout of a fractional value

        System.out.println("\nI forgot what you typed in!");
    }
}
