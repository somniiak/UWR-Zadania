import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

public class Game {
    public static final int ROWS = 7;
    public static final int COLS = 7;
    public GameState state;


    public Game(String boardType) {
        boolean[][] board = createBoard(boardType);
        boolean[][] pegs = createBoard(boardType);
        pegs[3][3] = false;

        state = new GameState(boardType, board, pegs, -1, -1);
    }

    public Game(GameState loadedState) {
        this.state = loadedState;
    }

    public boolean isValidPosition(int row, int col) {
        return row >= 0 && row < ROWS &&
               col >= 0 && col < COLS &&
               state.board[row][col];
    }

    public boolean hasPeg(int row, int col) {
        return isValidPosition(row, col) && state.pegs[row][col];
    }

    public boolean isValidMove(int fromRow, int fromCol, int toRow, int toCol) {
        int r = Math.abs(fromRow - toRow);
        int c = Math.abs(fromCol - toCol);

        if (!((r == 2 && c == 0) || (r == 0 && c == 2)))
            return false;

        int midRow = (fromRow + toRow) / 2;
        int midCol = (fromCol + toCol) / 2;

        return (
            isValidPosition(fromRow, fromCol) &&
            isValidPosition(midRow, midCol) &&
            isValidPosition(toRow, toCol) &&
            state.pegs[fromRow][fromCol] &&
            state.pegs[midRow][midCol] &&
            !state.pegs[toRow][toCol]
        );
    }

    public void makeMove(int fromRow, int fromCol, int toRow, int toCol) {
        if (!isValidMove(fromRow, fromCol, toRow, toCol))
            return;

        int midRow = (fromRow + toRow) / 2;
        int midCol = (fromCol + toCol) / 2;

        state.pegs[fromRow][fromCol] = false;
        state.pegs[midRow][midCol] = false;
        state.pegs[toRow][toCol] = true;
    }

    public boolean canMove(int row, int col) {
        return (
            isValidMove(row, col, row - 2, col) ||
            isValidMove(row, col, row + 2, col) ||
            isValidMove(row, col, row, col - 2) ||
            isValidMove(row, col, row, col + 2)
        );
    }

    public boolean checkMoves() {
        for (int r = 0; r < ROWS; r++)
            for (int c = 0; c < COLS; c++)
                if (state.pegs[r][c] && canMove(r, c))
                    return true;
        return false;
    }

    public int countPegs() {
        int count = 0;
        for (int r = 0; r < ROWS; r++)
            for (int c = 0; c < COLS; c++)
                if (state.pegs[r][c]) count++;
        return count;
    }

    public boolean hasWon() {
        return !checkMoves() && countPegs() == 1 && state.pegs[3][3];
    }

    private boolean[][] createBoard(String boardType) {
        boolean[][] res = {
            {false, false, true,  true,  true,  false, false},
            {false, false, true,  true,  true,  false, false},
            {true,  true,  true,  true,  true,  true,  true},
            {true,  true,  true,  true,  true,  true,  true},
            {true,  true,  true,  true,  true,  true,  true},
            {false, false, true,  true,  true,  false, false},
            {false, false, true,  true,  true,  false, false}
        };

        // Jeśli plansza jest europejska dodajemy cztery bloczki
        if (boardType.equals("european"))
            res[1][1] = res[5][1] = res[1][5] = res [5][5] = true;

        return res;
    }

    public void saveStateToFile() {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream("solitaire.ser"))) {
            out.writeObject(state);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static GameState loadFromFile() {
        File f = new File("solitaire.ser");
        if (!f.exists())
            return null;

        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(f))) {
            GameState loaded = (GameState) in.readObject();
            f.delete();
            return loaded;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
