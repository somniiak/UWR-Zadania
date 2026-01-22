import java.awt.*;
import java.awt.event.*;

public class Paint extends Frame {
    private Powierzchnia powierzchnia;
    private Panel panelBoczny;
    private CheckboxGroup grupaKolorow;

    public Paint() {
        // Tytuł okienka
        super("Kolorowy Rysunek");

        // Rozmiar okienka
        setSize(800, 600);

        // Powierzchnia kreślarska
        // (musi być center bo się zepsuje)
        powierzchnia = new Powierzchnia();
        add(powierzchnia, BorderLayout.CENTER);

        // Panel boczny
        panelBoczny = new Panel();
        panelBoczny.setLayout(new GridLayout(0,1));
        panelBoczny.setBackground(Color.LIGHT_GRAY);
        panelBoczny.add(new Label("Wybierz kolor:"));
        add(panelBoczny, BorderLayout.EAST);

        String[] kolory = {
            "Czarny",       "Szary",    "Czerwony",
            "Pomarańczowy", "Żółty",    "Zielony", 
            "Niebieski",    "Magenta",  "Różowy",
        };

        // Tworzenie przycisków radiowych
        grupaKolorow = new CheckboxGroup();
        for (int i = 0; i < kolory.length; i++) {
            var rb = new Checkbox(kolory[i], grupaKolorow, i == 0);

            rb.addItemListener(new ItemListener() {
                public void itemStateChanged(ItemEvent e) {
                    ustawKolorRadio();
                }
            });

            panelBoczny.add(rb);
        }

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                dispose();
            }
        });

        // Widoczność okienka
        setVisible(true);
    }

    public void ustawKolorRadio() {
        String kolor = grupaKolorow
                        .getSelectedCheckbox()
                        .getLabel();

        Color nowyKolor = switch(kolor) {
            case "Szary" -> Color.GRAY;
            case "Czerwony" -> Color.RED;
            case "Pomarańczowy" -> Color.ORANGE;
            case "Żółty" -> Color.YELLOW;
            case "Zielony" -> Color.GREEN;
            case "Niebieski" -> Color.BLUE;
            case "Magenta" -> Color.MAGENTA;
            case "Różowy" -> Color.PINK;
            default -> Color.BLACK;
        };

        powierzchnia.ustawKolor(nowyKolor);
    }

    public static void main(String[] args) {
        new Paint();
    }
}
