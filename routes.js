

/**const express = require('express');
const bodyParser = require('body-parser')

const app = express();
const router = express.Router();



app.use(bodyParser.json());

router.get("/", function(req,res) {
    res.send("welcome to webhooks API")
});

router.post("/commit-messages" , function(req,res) {
    console.log(req.payload);
    res.send("github webhook successfully recieved");
});


app.use('/', router);

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});*/