import express from "express";
import expressLayouts from "express-ejs-layouts";

const app = express();

app.set("view engine", "ejs");
app.set("views", "./views");
app.use(expressLayouts);

app.set("layout", "./layouts/main");

app.get("/", (req, res) => {
    res.render("home", { title: "Strona główna" });
});

app.get("/about", (req, res) => {
    res.render("about", { title: "WEPPO25" });
});

const PORT = 8080
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});