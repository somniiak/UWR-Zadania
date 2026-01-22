import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class BoardPanel extends JPanel {
    private int CELL_SIZE = 60;
    private int PEG_RADIUS = 20;

    private int offsetX = 0;
    private int offsetY = 0;

    private Color ACTIVE_PEG_COLOR = Color.YELLOW;
    private Color DORMANT_PEG_COLOR = Color.BLUE;
    private Color CELL_COLOR = Color.DARK_GRAY;
    private Color OUTLINE_COLOR = Color.BLACK;

    public String boardType;
    public JLabel statusLabel;
    Game gameInstance;

    public BoardPanel(Game gameInstance, String boardType, JLabel statusLabel) {
        this.boardType = boardType;
        this.statusLabel = statusLabel;
        this.gameInstance = gameInstance;

        addMouseListener(new MouseAdapter() {
            public void mousePressed(MouseEvent e) {
                int mx = e.getX() - offsetX;
                int my = e.getY() - offsetY;

                if (mx < 0 || my < 0)
                    return;

                int col = mx / CELL_SIZE;
                int row = my / CELL_SIZE;

                handleClick(row, col);
            }
        });
    }

    public void handleClick(int row, int col) {
        if (gameInstance.isValidPosition(row, col)) {
            if (gameInstance.state.selectedRow == -1) {
                if (gameInstance.hasPeg(row, col)) {
                    gameInstance.state.selectedRow = row;
                    gameInstance.state.selectedCol = col;
                }
            } else {
                gameInstance.makeMove(gameInstance.state.selectedRow, gameInstance.state.selectedCol, row, col);
                gameInstance.state.selectedRow = -1;
                gameInstance.state.selectedCol = -1;
            }
        }

        repaint();

        if (SwingUtilities.getWindowAncestor(this) instanceof JFrame frame) {
            boolean status = !gameInstance.checkMoves();

            if (frame.getJMenuBar() instanceof MenuBar mb) {
                mb.boardTypeEnglish.setEnabled(status);
                mb.boardTypeEuropean.setEnabled(status);
            }

            if (status) {
                statusLabel.setVisible(true);

                if (gameInstance.hasWon())
                    statusLabel.setText("Wygrana! Pozostał jeden pionek w centrum.");
                else
                    statusLabel.setText("Porażka! Pozostałe pionki: " + gameInstance.countPegs());
            }
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        g2d.setRenderingHint(
            RenderingHints.KEY_ANTIALIASING,
            RenderingHints.VALUE_ANTIALIAS_ON
        );

        int size = Math.min(getHeight(), getWidth());
        CELL_SIZE = size / Game.COLS;
        PEG_RADIUS = CELL_SIZE / 3;

        int boardWidth = CELL_SIZE * Game.COLS;
        int boardHeight = CELL_SIZE * Game.ROWS;

        offsetX = (getWidth() - boardWidth) / 2;
        offsetY = (getHeight() - boardHeight) / 2;

        for (int r = 0; r < Game.ROWS; r++) {
            for (int c = 0; c < Game.COLS; c++) {
                if (!gameInstance.isValidPosition(r, c))
                    continue;

                int x = offsetX + c * CELL_SIZE;
                int y = offsetY + r * CELL_SIZE;

                // Tło pola
                g2d.setColor(CELL_COLOR);
                g2d.fillRect(x, y, CELL_SIZE, CELL_SIZE);

                g2d.setColor(OUTLINE_COLOR);
                g2d.drawRect(x, y, CELL_SIZE, CELL_SIZE);

                // Rysowanie pionka lub pustego pola
                if (gameInstance.hasPeg(r, c)) {
                    int centerX = x + CELL_SIZE / 2;
                    int centerY = y + CELL_SIZE / 2;

                    boolean selected = (r == gameInstance.state.selectedRow && c == gameInstance.state.selectedCol);
                    g2d.setColor(selected ? ACTIVE_PEG_COLOR : DORMANT_PEG_COLOR);
                    g2d.fillOval(centerX - PEG_RADIUS, centerY - PEG_RADIUS, PEG_RADIUS * 2, PEG_RADIUS * 2);
                }
            }
        }
    }

    public void setActivePegColor(Color color) {
        ACTIVE_PEG_COLOR = color;
    }

    public void setDormantPegColor(Color color) {
        DORMANT_PEG_COLOR = color;
    }

    public void setCellColor(Color color) {
        CELL_COLOR = color;
    }

    public void setOutlineColor(Color color) {
        OUTLINE_COLOR = color;
    }
}