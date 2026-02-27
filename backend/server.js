const express = require("express");
const cors = require("cors");
const multer = require("multer");
const axios = require("axios");
const path = require("path");

const app = express();

app.use(cors());
app.use(express.json());

// ---------- Basic Route ----------
app.get("/", (req,res)=>{
    res.send("Resume Analyzer Backend Working");
});


// ---------- File Storage Setup ----------
const storage = multer.diskStorage({
    destination: function(req,file,cb){
        cb(null,"uploads/");
    },
    filename: function(req,file,cb){
        cb(null,file.originalname);
    }
});

const upload = multer({storage:storage});


// ---------- Resume Upload API ----------
app.post("/upload", upload.single("resume"), async(req,res)=>{

    try{

        const response = await axios.post(
            "http://127.0.0.1:5000/analyze",
            {
                fileName: req.file.path
            }
        );

        res.json(response.data);

    }catch(err){
        console.log(err);
        res.status(500).send(err.message);
    }

});
app.listen(5000, ()=>{
    console.log("🚀 Backend Server Running on port 5000");
});