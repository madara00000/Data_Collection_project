const express = require('express');
const mysql = require('mysql');
const cors = require('cors')
const axios = require('axios');
const app = express();
const port = '3000'; // Set your desired port


app.use(cors());

const db = mysql.createConnection(  {
     host: "localhost",
     user: "root",
     password: "rootroot",
     database: "companies",
} );

db.connect((err) => {
  if (err) {console.log("error at connecting to the DB",err) ;}
  else console.log('Connected to MySQL database');
});




// API endpoint to fetch data from MySQL
app.get('/get-data', (req, res) => {
        db.query( 'SELECT * FROM offices' , (err, results) => {

      if (err) { console.log("error at fetching the data ",err);  } 
      
      else { res.send(results); }
    });
  });
  
  app.listen(port, (err) => {
    if (err){ console.log(err)}
    
    else{ console.log(`Server is running on port ${port}`);}
  });