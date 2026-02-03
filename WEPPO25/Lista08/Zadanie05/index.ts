import express from "express";
import cookieParser from "cookie-parser";

const app = express();

app.set("view engine", "ejs");
app.set("views", "./views");
app.use(express.static("."));
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

var cookieValue : any | null;

app.get("/", (req, res) => {
    const cookieValue = req.cookies.mycookie || null;
    res.render("main", { cookieValue });
});

app.post("/setcookie", (req, res) => {
    const value = new Date().toString();
    res.cookie("mycookie", value);
    res.redirect("/");
});

app.post("/delcookie", (req, res) => {
    res.clearCookie("mycookie");
    res.redirect("/");
});

const PORT = 8080
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});