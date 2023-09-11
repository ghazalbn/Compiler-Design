import java.util.Random;
import java.util.ArrayList;

//it was a line comment
public abstract class Piece
{
    protected String name;
    protected int x;
    protected int y;
    protected boolean[][] flag = new boolean[8][4];

    protected Piece(String name, int x, int y)
    {
        this.name = name;
        this.x = x;
        this.y = y;
    }

    protected abstract void move();
}

/* it was 
a block comment
*/

public class Castle extends Piece
{
    protected Castle(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

    /* override method move
    use switch case
    move0
    move1
    move2
    */
    @Override
    protected void move()
    {
        switch ((int) (Math.random() * 3))
        {
            case 0: move0(); break;
            case 1: move1(); break;
            case 2: move2(); break;
        }
    }

    private void move0()
    {
        // check if y < 7
        if (this.y < 7)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.y++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }

    // it was a line comment before move1
    private void move1()
    {
        if (this.x < 3)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }
    /* it was a block commrnt
    bellow is move2 method
    */
    private void move2()
    {
        if (this.x > 1)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }
}


