package org.calculator;

import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.HashMap;

public class CalculatorController {
    @FXML private TextField baseTwoTextField;
    @FXML private TextField baseThreeTextField;
    @FXML private TextField baseFourTextField;
    @FXML private TextField baseFiveTextField;
    @FXML private TextField baseSixTextField;
    @FXML private TextField baseSevenTextField;
    @FXML private TextField baseEightTextField;
    @FXML private TextField baseNineTextField;
    @FXML private TextField baseTenTextField;
    @FXML private TextField baseElevenTextField;
    @FXML private TextField baseTwelveTextField;
    @FXML private TextField baseThirteenTextField;
    @FXML private TextField baseFourteenTextField;
    @FXML private TextField baseFifteenTextField;
    @FXML private TextField baseSixteenTextField;

    private final char[] VALUES = {
      '0', '1', '2', '3', '4', '5', '6', '7',
      '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
    };

    private String focusedFieldText;
    protected HashMap<TextField, Integer> baseTextFields;

    public void initialize() {
        baseTextFields = new HashMap<TextField, Integer>() {{
            put(baseTwoTextField, 2);       put(baseThreeTextField, 3);     put(baseFourTextField, 4);
            put(baseFiveTextField, 5);      put(baseSixTextField, 6);       put(baseSevenTextField, 7);
            put(baseEightTextField, 8);     put(baseNineTextField, 9);      put(baseTenTextField, 10);
            put(baseElevenTextField, 11);   put(baseTwelveTextField, 12);   put(baseThirteenTextField, 13);
            put(baseFourteenTextField, 14); put(baseFifteenTextField, 15); put(baseSixteenTextField, 16);
        }};

        // https://stackoverflow.com/a/13881757
        for (TextField field : baseTextFields.keySet()) {
            field.setOnKeyPressed(e -> {
                if (e.getCode().equals(KeyCode.ENTER)) {
                    updateText(field);
                    focusedFieldText = field.getText();
                }
            });

            field.focusedProperty().addListener((obs, oldVal, newVal) -> {
                    if (newVal) focusedFieldText = field.getText();
                    else field.setText(focusedFieldText);
                });
        }
    }

    private String cleanupInput(String input, int base) {
        StringBuilder res = new StringBuilder();

        for (char c : input.toCharArray())
            if (Character.digit(c, base) != -1)
                res.append(c);

        return res.toString();
    }

    private String convertBase(String number, int fromBase, int toBase) {
        return new BigInteger(number, fromBase).toString(toBase);
    }

    @FXML
    protected void updateText(TextField inputTextField) {
        int inputBase = baseTextFields.get(inputTextField);
        String inputText = cleanupInput(inputTextField.getText(), inputBase);

        for (TextField field : baseTextFields.keySet()) {
            int targetBase = baseTextFields.get(field);
            field.setText(inputText.isEmpty() ? "" : convertBase(inputText, inputBase, targetBase));
        }

        inputTextField.end();
    }
}
