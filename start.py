import os
import msvcrt

# COLORS
SET_YELLOW_TEXT = "\u001b[33m"
SET_GREEN_TEXT = "\u001b[32m"
SET_BLUE_TEXT = "\u001b[34m"
SET_RESET_TEXT = "\u001b[0m"

# COMMANDS
COMMANDS = [
    'git init',
    'npm i express',
    'npm i --sav-dev nodemon',
    'npm i mysql2'
]

PACKAGE_JSON_TEMPLATE = """
{
  "name": "backend",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
"""

# TEMPLATES
SERVER_JS_TEMPLATE = """
const express = require('express');

// PORT NUMBER
const port = 3001;

// CREATE EXPRESS SERVER
const app = express();

// START SERVER
app.get('/', (req, res) => {
    console.log("Server has started");
    res.send("Server has started!");
})
        
// START ROUTERS
const usersRouter = require('./routes/users');
app.use('/users', usersRouter);

// START LISTENING ON PORT NUMBER
app.listen(port, () => {
    console.log(`Server now listening at port ${port}!`)
})
"""

CONNECTION_JS_TEMPLATE = """
const mysql = require('mysql2');

// DATABASE NAME
const database = "";

// DATABASE CONNECTION
const db = mysql.createConnection({
    host: 'localhost',
    user: 'root', 
    password: 'admin',
    database: database
});

// CONNECT TO DATABASE
db.connect(error => {
    if (error) throw error;
    console.log("mySQL connected!")
})

module.exports = db;
"""

ROUTE_TEMPLATE = """
const express = require('express');
const router = express.Router();
const usersController = require('../controllers/usersController')

router.get('/', usersController.get)

module.exports = router;
"""

CONTROLLER_TEMPLATE = """
const usersModel = require('../models/usersModel')

async function get(req, res) {
    let data = await usersModel.getUsers();
    res.json(data);
}

module.exports = {get};
"""

MODEL_TEMPLATE = """
const db = require('./connection');

const getUsers = () => {
    let query = 'SELECT * FROM *';
    return new Promise((resolve, reject) => {
        db.query(query, (error, result) => {
            if (error) return reject(error);
            return resolve(result);
        })
    })
}

module.exports = {getUsers}
"""

GIT_IGNORE_TEMPLATE = """
/node_modules
/build
"""

def initCommand(command):
    print(f'{SET_YELLOW_TEXT}INITIATING:{SET_RESET_TEXT} {command}\n')
    os.system(f'{command}')
    print(f"\n\n{SET_GREEN_TEXT}------------------------------ COMPLETE ------------------------------{SET_RESET_TEXT}\n\n")

def createFile(fileName, template):
    print(f"{SET_YELLOW_TEXT}CREATING:{SET_RESET_TEXT} {fileName}")
    os.makedirs(os.path.dirname(fileName), exist_ok=True)
    with open(fileName, 'a') as file:
        file.write(template.strip())
        file.truncate()
        file.close()
    print(f"\n\n{SET_GREEN_TEXT}------------------------------ FILE CREATION COMPLETE ------------------------------{SET_RESET_TEXT}\n\n")

def main():
    initCommand(COMMANDS[0])
    createFile('./package.json', PACKAGE_JSON_TEMPLATE)
    initCommand(COMMANDS[1])
    initCommand(COMMANDS[2])
    initCommand(COMMANDS[3])
    createFile('./server.js', SERVER_JS_TEMPLATE)
    createFile('./connection.js', CONNECTION_JS_TEMPLATE)
    createFile('./routes/users.js', ROUTE_TEMPLATE)
    createFile('./controllers/usersController.js', CONTROLLER_TEMPLATE)
    createFile('./models/usersModel.js', MODEL_TEMPLATE)
    createFile('./.gitignore', GIT_IGNORE_TEMPLATE)
    print('Press any key to quit...')
    input_char = msvcrt.getch()
    if input_char.upper() == '': 
        return

print(f"{SET_BLUE_TEXT}------------------------------ STARTING BACKEND BOILERPLATE CREATION ------------------------------{SET_RESET_TEXT}\n\n")
main()

if os.path.exists("./start.py"):
    os.remove("./start.py")