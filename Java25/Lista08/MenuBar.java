import javax.swing.*;
import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.InputEvent;

public class MenuBar extends JMenuBar {
    private JMenu gameMenu;
    private JMenu movesMenu;
    private JMenu settingsMenu;
    private JMenu helpMenu;

    public JRadioButton boardTypeEnglish;
    public JRadioButton boardTypeEuropean;

    private String boardType;
    private BoardPanel currentBoard;

    public MenuBar(BoardPanel board) {
        currentBoard = board;
        boardType = currentBoard.boardType;

        createGameMenu();
        createMovesMenu();
        createSettingsMenu();
        // https://stackoverflow.com/a/8560857 nie wiem jak ale działa i przesuwa "Pomoc" na prawo
        add(Box.createHorizontalGlue());
        createHelpMenu();
    }

    private void createGameMenu() {
        gameMenu = new JMenu("Gra");

        JMenuItem newGame = new JMenuItem("Nowa");
        newGame.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_N, InputEvent.CTRL_DOWN_MASK));

        newGame.addActionListener(e -> {
            currentBoard.gameInstance = new Game(boardType);
            currentBoard.statusLabel.setVisible(false);
            boardTypeEnglish.setEnabled(true);
            boardTypeEuropean.setEnabled(true);
            currentBoard.repaint();
        });

        JMenuItem endGame = new JMenuItem("Koniec");
        endGame.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_K, InputEvent.CTRL_DOWN_MASK));

        endGame.addActionListener(e -> {
            System.exit(ABORT);
        });

        gameMenu.add(newGame);
        gameMenu.addSeparator();
        gameMenu.add(endGame);

        add(gameMenu);
    }

    private void createMovesMenu() {
        movesMenu = new JMenu("Ruchy");

        JMenuItem moveUp = new JMenuItem("Góra");
        moveUp.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_UP, InputEvent.CTRL_DOWN_MASK));

        moveUp.addActionListener(e -> {
            int row = currentBoard.gameInstance.state.selectedRow;
            int col = currentBoard.gameInstance.state.selectedCol;

            if (currentBoard.gameInstance.isValidMove(row, col, row - 2, col)) {
                currentBoard.handleClick(row - 2, col);

                if (currentBoard.gameInstance.canMove(row - 2, col)) {
                    currentBoard.gameInstance.state.selectedRow = row - 2;
                    currentBoard.gameInstance.state.selectedCol = col;
                }
            }

            currentBoard.repaint();
        });

        JMenuItem moveDown = new JMenuItem("Dół");
        moveDown.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_DOWN, InputEvent.CTRL_DOWN_MASK));

        moveDown.addActionListener(e -> {
            int row = currentBoard.gameInstance.state.selectedRow;
            int col = currentBoard.gameInstance.state.selectedCol;

            if (currentBoard.gameInstance.isValidMove(row, col, row + 2, col)) {
                currentBoard.handleClick(row + 2, col);

                if (currentBoard.gameInstance.canMove(row + 2, col)) {
                    currentBoard.gameInstance.state.selectedRow = row + 2;
                    currentBoard.gameInstance.state.selectedCol = col;
                }
            }

            currentBoard.repaint();
        });

        JMenuItem moveLeft = new JMenuItem("Lewo");
        moveLeft.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_LEFT, InputEvent.CTRL_DOWN_MASK));

        moveLeft.addActionListener(e -> {
            int row = currentBoard.gameInstance.state.selectedRow;
            int col = currentBoard.gameInstance.state.selectedCol;

            if (currentBoard.gameInstance.isValidMove(row, col, row, col - 2)) {
                currentBoard.handleClick(row, col - 2);

                if (currentBoard.gameInstance.canMove(row, col -2)) {
                    currentBoard.gameInstance.state.selectedRow = row;
                    currentBoard.gameInstance.state.selectedCol = col - 2;
                }
            }

            currentBoard.repaint();
        });

        JMenuItem moveRight = new JMenuItem("Prawo");
        moveRight.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_RIGHT, InputEvent.CTRL_DOWN_MASK));

        moveRight.addActionListener(e -> {
            int row = currentBoard.gameInstance.state.selectedRow;
            int col = currentBoard.gameInstance.state.selectedCol;

            if (currentBoard.gameInstance.isValidMove(row, col, row, col + 2)) {
                currentBoard.handleClick(row, col + 2);
                
                if (currentBoard.gameInstance.canMove(row, col + 2)) {
                    currentBoard.gameInstance.state.selectedRow = row;
                    currentBoard.gameInstance.state.selectedCol = col + 2;
                }
            }

            currentBoard.repaint();
        });

        movesMenu.add(moveUp);
        movesMenu.add(moveDown);
        movesMenu.add(moveLeft);
        movesMenu.add(moveRight);

        add(movesMenu);
    }

    private void createSettingsMenu() {
        settingsMenu = new JMenu("Ustawienia");

        JMenu boardTypeMenu = genBoardTypeSubmenu();
        JMenu boardColorMenu = genBoardColorSubmenu();
        JMenu pegDormantColorMenu = genPegDormantColorMenu();
        JMenu pegActiveColorMenu = genPegActiveColorMenu();

        settingsMenu.add(boardTypeMenu);
        settingsMenu.add(boardColorMenu);
        settingsMenu.add(pegDormantColorMenu);
        settingsMenu.add(pegActiveColorMenu);

        add(settingsMenu);
    }

    private JMenu genBoardTypeSubmenu() {
        JMenu boardTypeMenu = new JMenu("Typ planszy");
        ButtonGroup boardTypeGroup = new ButtonGroup();

        boardTypeEnglish = new JRadioButton("Brytyjska", true);
        boardTypeEuropean = new JRadioButton("Europejska", false);

        boardTypeEnglish.addActionListener(e -> {
            boardType = "english";
        });

        boardTypeEuropean.addActionListener(e -> {
            boardType = "european";
        });

        boardTypeGroup.add(boardTypeEnglish);
        boardTypeGroup.add(boardTypeEuropean);

        boardTypeMenu.add(boardTypeEnglish);
        boardTypeMenu.add(boardTypeEuropean);

        return boardTypeMenu;
    }

    private JMenu genBoardColorSubmenu() {
        JMenu boardColorMenu = new JMenu("Kolor planszy");
        ButtonGroup boardColorGroup = new ButtonGroup();

        JRadioButton boardColorWhite = new JRadioButton("Biały", false);

        boardColorWhite.addActionListener(e -> {
            currentBoard.setCellColor(Color.WHITE);
            currentBoard.setOutlineColor(Color.DARK_GRAY);
            currentBoard.repaint();
        });

        boardColorGroup.add(boardColorWhite);
        boardColorMenu.add(boardColorWhite);

        JRadioButton boardColorLightGray = new JRadioButton("Jasny szary", false);

        boardColorLightGray.addActionListener(e -> {
            currentBoard.setCellColor(Color.LIGHT_GRAY);
            currentBoard.setOutlineColor(Color.BLACK);
            currentBoard.repaint();
        });

        boardColorGroup.add(boardColorLightGray);
        boardColorMenu.add(boardColorLightGray);

        JRadioButton boardColorDarkGray = new JRadioButton("Ciemny szary", true);

        boardColorDarkGray.addActionListener(e -> {
            currentBoard.setCellColor(Color.DARK_GRAY);
            currentBoard.setOutlineColor(Color.BLACK);
            currentBoard.repaint();
        });

        boardColorGroup.add(boardColorDarkGray);
        boardColorMenu.add(boardColorDarkGray);

        JRadioButton boardColorBlack = new JRadioButton("Czarny", false);

        boardColorBlack.addActionListener(e -> {
            currentBoard.setCellColor(Color.BLACK);
            currentBoard.setOutlineColor(Color.DARK_GRAY);
            currentBoard.repaint();
        });

        boardColorGroup.add(boardColorBlack);
        boardColorMenu.add(boardColorBlack);

        return boardColorMenu;
    }

    private JMenu genPegDormantColorMenu() {
        JMenu pegDormantColorMenu = new JMenu("Kolor pionków");
        ButtonGroup pegDormantColorGroup = new ButtonGroup();

        JRadioButton[] pegDormantColorButtons = {
            new JRadioButton("Czerwony"),
            new JRadioButton("Pomarańczowy"),
            new JRadioButton("Żółty"),
            new JRadioButton("Zielony"),
            new JRadioButton("Niebieski"),
            new JRadioButton("Różowy"),
        };

        pegDormantColorButtons[4].setSelected(true);

        for (JRadioButton pegDormantColor : pegDormantColorButtons) {
            pegDormantColor.addActionListener(e -> {
                Color color = switch(pegDormantColor.getText()) {
                    case "Czerwony" -> Color.RED;
                    case "Pomarańczowy" -> Color.ORANGE;
                    case "Żółty" -> Color.YELLOW;
                    case "Zielony" -> Color.GREEN;
                    case "Niebieski" -> Color.BLUE;
                    case "Różowy" -> Color.PINK;
                    default -> Color.BLUE;
                };

                currentBoard.setDormantPegColor(color);
                currentBoard.repaint();
            });

            pegDormantColorGroup.add(pegDormantColor);
            pegDormantColorMenu.add(pegDormantColor);
        }

        return pegDormantColorMenu;
    }

    private JMenu genPegActiveColorMenu() {
        JMenu pegActiveColorMenu = new JMenu("Kolor wybranego pionka");
        ButtonGroup pegActiveColorGroup = new ButtonGroup();

        JRadioButton[] pegActiveColorButtons = {
            new JRadioButton("Czerwony"),
            new JRadioButton("Pomarańczowy"),
            new JRadioButton("Żółty"),
            new JRadioButton("Zielony"),
            new JRadioButton("Niebieski"),
            new JRadioButton("Różowy"),
        };

        pegActiveColorButtons[2].setSelected(true);

        for (JRadioButton pegActiveColor : pegActiveColorButtons) {
            pegActiveColor.addActionListener(e -> {
                Color color = switch(pegActiveColor.getText()) {
                    case "Czerwony" -> Color.RED;
                    case "Pomarańczowy" -> Color.ORANGE;
                    case "Żółty" -> Color.YELLOW;
                    case "Zielony" -> Color.GREEN;
                    case "Niebieski" -> Color.BLUE;
                    case "Różowy" -> Color.PINK;
                    default -> Color.BLUE;
                };

                currentBoard.setActivePegColor(color);
                currentBoard.repaint();
            });

            pegActiveColorGroup.add(pegActiveColor);
            pegActiveColorMenu.add(pegActiveColor);
        }

        return pegActiveColorMenu;
    }

    private void createHelpMenu() {
        helpMenu = new JMenu("Pomoc");

        JMenuItem aboutGame = new JMenuItem("O grze");

        aboutGame.addActionListener(e -> {
            JOptionPane.showMessageDialog(null,
                "Samotnik to gra logiczna której celem jest zostawienie na" +
                "planszy\njak najmniejszej liczby pionków. Idealnym rozwiązaniem " +
                "jest\npozostawienie jednego pionka, najlepiej w centrum. Pionka\n" +
                "bije się przeskakując go w pionie lub poziomie. Nie można\nporuszać " +
                "się na ukos oraz nie można bić kilku pionków w\njednym ruchu.",
                "O grze",
                JOptionPane.INFORMATION_MESSAGE
            );
        });

        JMenuItem aboutApp = new JMenuItem("O aplikacji");

        aboutApp.addActionListener(e -> {
            JOptionPane.showMessageDialog(null,
                "Wersja: 1.0.0\n" +
                "Data wydania: 07/12/2025\n" +
                "Autor: Artur Dzido\n",
                "O aplikacji",
                JOptionPane.INFORMATION_MESSAGE
            );
        });

        helpMenu.add(aboutGame);
        helpMenu.add(aboutApp);

        add(helpMenu);
    }
}
