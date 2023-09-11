import java.util.Random;
import java.util.ArrayList;

//first line comment
//second line comment
//third line comment
//fourth line comment
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

/* block comment line 1
block comment line 2
block comment line 3
*/

public class Castle extends Piece
{
    protected Castle(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

    /* block comment */
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
        // line comment
        if (this.y < 7)
        {
            Move = String.format("x:%d y:%d ==> {0}, {1}", this.x + this.y);
        }
        else 
        {
            Move = move();
        }
        System.out.printf(Move);
    }

    /* block comment line 1
    block comment line 2
    block comment line 3
    */
    // line comment
    private void move1()
    {
        if (this.x < 3)
        {
            X = x++;
        }
        else 
        {
            X = String.format("x:%d y:%d ==> {0}, {1}", this.x + this.y);
        }
        System.out.printf(X);
    }

    // line comment
    /* block comment */
    private void move2()
    {
        if (this.x > 1)
        {
            Y = this.flag[this.y][this.x];
        }
        else 
        {
            Y = x--;
        }
    }
}


