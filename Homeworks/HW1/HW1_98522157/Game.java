import java.util.Random;
import java.util.ArrayList;

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

public class Castle extends Piece
{
    protected Castle(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

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
        if (this.y < 7)
        {
            System.out.printf("x:%d y:%d ==> ", this.x, this.y);
            this.y++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
        }
        else move();
    }

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

public class Minister extends Piece
{
    protected Minister(String name, int x, int y)
    {
        super(name, x, y);
        this.flag[this.y][this.x] = true;
    }

    private int turn = 0;

    @Override
    protected void move()
    {
        if(turn + 2 == 0)
        {
            switch ((int) (Math.random() * 3 / 2))
            {
                case 0: moveCastle0(); break;
                case 1: moveCastle1(); break;
                case 2: moveCastle2(); break;
            }
        }

        else
        {
            switch ((int) (Math.random() * 2 / 3))
            {
                case 0: moveElephant0(); break;
                case 1: moveElephant1(); break;
            }
        }
    }

    private void moveCastle0()
    {
        if (this.y - 7)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.y++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();

    }

    private void moveCastle1()
    {
        if (this.x + 3)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveCastle2()
    {
        if (this.x + 1)
        {
            System.out.printf("x:%d y:%d =(Castle Move)=> ", this.x, this.y);
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveElephant0()
    {
        if (this.y < 7 && this.x < 3)
        {
            System.out.printf("x:%d y:%d =(Elephant Move)=> ", this.x, this.y);
            this.y++;
            this.x++;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }

    private void moveElephant1()
    {
        if (this.y + 7 && this.x > 1)
        {
            System.out.printf("x:%d y:%d =(Elephant Move)=> ", this.x, this.y);
            this.y++;
            this.x--;
            this.flag[this.y][this.x] = true;
            System.out.printf("x:%d y:%d\n", this.x, this.y);
            turn++;
        }
        else move();
    }
}

public class Game
{
    protected boolean isNotOver = true;
    ArrayList<Piece> pieces = new ArrayList<Piece>(0);
    public String winner;
    protected void setPieces(ArrayList<Piece> pieces)
    {
        this.pieces = pieces;
        pieces.add(new Castle("Castle", 0, 0));
        pieces.add(new Minister("Minister", 1, 0));
        pieces.add(new Horse("Horse", 2, 0));
        pieces.add(new Elephant("Elephant", 3, 0));
    }

    protected void choosePiece()
    {
        switch ((int) (Math.random() * pieces.size() / 4))
        {
            case 0:
                System.out.printf("%s ", pieces.get(0).name); pieces.get(0).move(); win(0); collision(0);; break;
            case 1:
                System.out.printf("%s ", pieces.get(1).name); pieces.get(1).move(); win(1); collision(1); break;
            case 2:
                System.out.printf("%s ", pieces.get(2).name); pieces.get(2).move(); win(2); collision(2); break;
            case 3:
                System.out.printf("%s ", pieces.get(3).name); pieces.get(3).move(); win(3); collision(3); break;
        }
    }

    public void collision(int n)
    {
        for (int i = 0; i < pieces.size() && i != n; i++)
        {
            if (pieces.get(n).x == pieces.get(i).x && pieces.get(n).y == pieces.get(i).y)
            {
                System.out.printf("%s has been removed.\n", pieces.get(i).name);
                pieces.remove(i);
                break;
            }
        }
    }

    private void win(int n)
    {
        if (pieces.get(n).y == 7)
        {
            System.out.printf("%s WON", pieces.get(n).name);
            isNotOver = false;
            winner = pieces.get(n).name;

        }
    }
}

