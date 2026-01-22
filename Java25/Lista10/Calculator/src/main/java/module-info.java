module org.calculator {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;

    opens org.calculator to javafx.fxml;
    exports org.calculator;
}