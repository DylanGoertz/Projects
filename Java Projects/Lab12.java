/*************
Name:Dylab Goertz
Program Name:Lab12
Date:10/14/2022
*******************/
import static java.lang.System.*;
import java.util.Scanner;
public class Lab12
{
    public static void main(String[] args)
    {
        double r, x, w, y;
        double r1, r2, r3, r4, r5, r6, r7, r8;

        r1 = Math.abs(-127.5) - 2 * Math.abs(-34.2);
        r2 = -3 * Math.sqrt(2 * 3.14);
        r3 = Math.floor(-19.6) - Math.ceil(-45.8);
        r4 = 5 + Math.sin(Math.toRadians(26) ) + Math.cos(Math.toRadians(56) );

        r = 2.45;

        r5 = 4/3 * 3.14 * Math.pow( r, 3 );

        x = -5.2;

        r6 = 3 * x - 4 * Math.pow( x, 2 );

        w = 9.4;

        r7 = 7 * Math.E - 1 / w;

        y = 3.2;

        r8 = 2 * Math.exp(y);

        System.out.println("\nResult1: "+ r1);
        System.out.println("Result2: "+ r2);
        System.out.println("Result3: "+ r3);
        System.out.println("Result4: "+ r4);
        System.out.println("Result5: "+ r5);
        System.out.println("Result6: "+ r6);
        System.out.println("Result7: "+ r7);
        System.out.println("Result8: "+ r8 +"\n");
    }
}
