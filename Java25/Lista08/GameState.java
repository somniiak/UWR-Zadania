import java.io.Serializable;

public class GameState implements Serializable {
    private static final long serialVersionUID = 1L;

    public boolean[][] board;
    public boolean[][] pegs;
    public int selectedRow;
    public int selectedCol;
    public String boardType;

    public GameState(String boardType, boolean[][] board, boolean[][] pegs, int selectedRow, int selectedCol) {
        this.boardType = boardType;
        this.board = board;
        this.pegs = pegs;
        this.selectedRow = selectedRow;
        this.selectedCol = selectedCol;
    }
}
