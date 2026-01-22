import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class Powierzchnia extends Canvas {
    private ArrayList<Kreska> kreski;
    private Point tempPoczatek;
    private Point tempKoniec;
    private Color biezacyKolor;
    private boolean rysowanie;

    public Powierzchnia() {
        kreski = new ArrayList<Kreska>();
        biezacyKolor = Color.BLACK;
        rysowanie = false;
        setBackground(Color.WHITE);
        
        // Obsługa myszki (rysowanie)
        addMouseListener(new MouseAdapter() {
            // Kliknięto myszkę
            public void mousePressed(MouseEvent e) {
                tempPoczatek = e.getPoint();
            }

            // Zwolniono myszkę
            public void mouseReleased(MouseEvent e) {
                if (getBounds().contains(e.getPoint()) && rysowanie) {
                    dodajKreske(
                        new Kreska(
                            tempPoczatek,
                            tempKoniec,
                            biezacyKolor
                        )
                    );
                }

                rysowanie = false;
                repaint();
            }
        });

        // Aktualizacja rysowanej kreski
        addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                if (getBounds().contains(e.getPoint())) {
                    rysowanie = true;
                    tempKoniec = e.getPoint();
                    repaint();
                }
            }
        });

        // Obsługa klawiatury
        addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) {
                switch(e.getKeyCode()) {
                    case KeyEvent.VK_BACK_SPACE -> usunWszystkieKreski();
                    case KeyEvent.VK_B, KeyEvent.VK_L -> usunOstaniaKreske();
                    case KeyEvent.VK_F -> usunPierwszaKreske();
                }
            }
        });
    }

    // Ustawienie koloru malowania
    public void ustawKolor(Color c) {
        biezacyKolor = c;
    }

    // Dodanie kreski
    public void dodajKreske(Kreska k) {
        kreski.add(k);
        repaint();
    }

    // Usunięcie pierwszej kreski
    public void usunPierwszaKreske() {
        if (!kreski.isEmpty())
            kreski.remove(0);
        repaint();
    }

    // Usunięcie ostaniej kreski
    public void usunOstaniaKreske() {
        if (!kreski.isEmpty())
            kreski.remove(kreski.size() - 1);
        repaint();
    }

    // Usunięcie wszystkich kresek
    public void usunWszystkieKreski() {
        kreski.clear();
        repaint();
    }

    // Rysowanie zapisanych kresek (+ bieżącej)
    public void paint(Graphics gr) {
        for (Kreska k : kreski) {
            gr.setColor(k.kolor);
            gr.drawLine(
                k.poczatek.x, k.poczatek.y,
                k.koniec.x, k.koniec.y
            );
        }

        if (rysowanie && tempPoczatek != null && tempKoniec != null) {
            gr.setColor(Color.LIGHT_GRAY);
            gr.drawLine(
                tempPoczatek.x, tempPoczatek.y,
                tempKoniec.x, tempKoniec.y
            );
        }
    }
}
