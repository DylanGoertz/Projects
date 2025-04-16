/*************
Name:Dylab Goertz
Program Name:Example8
Date:10/14/2022
*******************/
import static java.lang.System.*;
public class Example8
{
    public static void main(String[] args)
    {
        int y;
        double x1, x2, x3, x4;

        x1 = 2 * Math.sqrt( 3 * Math.E);
        x2 = Math.abs(-15.29) + 2 * Math.ceil(7.7) * Math.floor(-2.3);

        y = 5;

        x3 = Math.pow( 2.4 , 1.2 ) - Math.exp( 3 * y );

        x4 = 2 * Math.sin(Math.toRadians(30) ) - 3 * Math.cos( Math.toRadians(45) );

        out.println("\n x1 = " + x1 );
        out.println(" x2 = " + x2 );
        out.println(" x3 = " + x3 );
        out.println(" x4 = " + x4 +"\n");
    }
}