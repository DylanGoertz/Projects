/*************
Name:Dylab Goertz
Program Name:Lab 10
Date:10/4/2022
*******************/
import java.util.Scanner;
import static java.lang.System.*;

public class Lab10
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);
        String adj1, adj2, pn1, pn2, adj3, noun1, noun2, pn3;

        out.print("\nGive me three adjectives, 3 plural nouns, and 2 nouns in that order.");
        adj1 = kb.next();
        adj2 = kb.next();
        adj3 = kb.next();
        pn1 = kb.next();
        pn2 = kb.next();
        pn3 = kb.next();
        noun1 = kb.next();
        noun2 = kb.next();
  
        out.print("\nLaides and gentlemen, on this" +adj1+ "occasion it is a privilage to adress such a/an" +adj2+ "-looking group of" +pn1+ ". I can tell from your smiling" +pn2+ "that you will support my" +adj3+ "program in the coming election. I pro,ise that, if elected, there will be a/an" +noun1+ "in every" +noun2+ "and two" +pn3+ "in every garage.\n");
    }
}