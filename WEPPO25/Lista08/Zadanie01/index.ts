import express from "express";
import type { Request } from "express";
import multer from "multer";
import path from "path";
import fs from "fs";

const app = express();

if (!fs.existsSync("images")) {
    fs.mkdirSync("images");
}

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "images");
    },
    filename: (req, file, cb) => {
        const unique = Date.now() + '-' + file.originalname;
        const ext = path.extname(file.originalname);
        cb(null, unique + ext);
    }
});

// https://blog.logrocket.com/multer-nodejs-express-upload-file/
const fileFilter = (req: any, file: any, cb: any) => {
    const filetypes = /.jpg|.jpeg|.png/
    const extname = filetypes.test(path.extname(file.originalname).toLowerCase())

    if (extname)
        return cb(null, true);
    else
        cb('Error: Images Only!');
};


const upload = multer({ storage, fileFilter });

app.set("view engine", "ejs");
app.set("views", "./views");
app.use(express.static("."));

let lastUploadedFilename: string | null = null;

app.get("/", (req, res) => {
    res.render("main", { filename: lastUploadedFilename });
});

app.post("/upload", upload.single("icon"), (req, res) => {
    if (!req.file)
        return res.send("Nie wybrano!");

    lastUploadedFilename = req.file.filename;
    res.redirect("/");
});

const PORT = 8080
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});