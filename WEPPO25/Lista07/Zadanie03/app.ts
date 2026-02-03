import express from "express";

const app = express();

app.set("view engine", "ejs");
app.set("views", "./views");
app.use(express.static("."));
app.use(express.urlencoded({ extended: true }));

let submittedData: Record<string, any> | null = null;

app.get("/", (req, res) => {
  res.render("form");
});

app.post("/submit", (req, res) => {
  submittedData = req.body;
  res.redirect("/print");
});

app.get("/print", (req, res) => {
  if (!submittedData) return res.redirect("/");
  res.render("print", { data: submittedData });
});

const PORT = 8080
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});