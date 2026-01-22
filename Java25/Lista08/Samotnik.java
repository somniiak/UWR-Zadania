import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.*;

public class Samotnik extends JFrame {
    private final String APP_TITLE = "Samotnik";
    private final int APP_HEIGHT = 700;
    private final int APP_WIDTH = 700;

    public Samotnik() {
        setTitle(APP_TITLE);
        setSize(APP_WIDTH, APP_HEIGHT);
        setLocationRelativeTo(null); // jakimś cudem to wyśrodkowuje okienko
        setLayout(new BorderLayout());

        JLabel gameStatus = new JLabel();
        gameStatus.setVisible(false);
        gameStatus.setPreferredSize(new Dimension(0, 60)); // Jakaś przerwa między planszą
        gameStatus.setHorizontalAlignment(SwingConstants.CENTER); // Wyśrodkowanie

        Game game;
        GameState loadedState = Game.loadFromFile();

        if (loadedState != null)
            game = new Game(loadedState);
        else
            game = new Game("english");


        BoardPanel boardPanel = new BoardPanel(game, "english", gameStatus);

        add(boardPanel, BorderLayout.CENTER);
        add(gameStatus, BorderLayout.SOUTH);

        setJMenuBar(new MenuBar(boardPanel));

        setDefaultCloseOperation(EXIT_ON_CLOSE);

        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                boardPanel.gameInstance.saveStateToFile();
                System.exit(0);
            }
        });
    }

    public static void main(String[] args) {
        Samotnik frame = new Samotnik();
        frame.setVisible(true);
    }
}