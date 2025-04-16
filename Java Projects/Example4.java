/*
Example4.java
A variable is a name that refers
to a location that holds a value.
the value of a variable can change
but not the type of value it holds.
*/

//with this import you don't have to type system.
// on the print lines
import static java.lang.System.*;

public class Example4
{
    public static void main(String[] args)
    {
        //declare variables
        int x, y, age;
        double seconds, e, checking;
        String forname, sur_name, title, star;

         //assign values
         x= -10;
         y= 400;
         age= 39;

         seconds= 4.71;
         e= 2.718281828459;
         checking= 1435.67;
         forname= "Dylan";
         sur_name= "Goertz";
         title= "Mr.";
         star= title + " "+forname+" "+sur_name;

         out.println("\nThe variable x contains " + x );
         out.println("The value " + y + " is stored in the variable y." );
         out.println("The experiment took " + seconds + "seconds." );
         out.println("Euler's number: " + e + "is an irrational number");
         out.println("Hi "+forname+", your checking account has $" +checking);
         out.println(star+" is a famous NFL player. \n" );
         
    }
}