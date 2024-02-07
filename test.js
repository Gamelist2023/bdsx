const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

// 静的ファイルをホストするディレクトリを設定
app.use('/', express.static(path.join(__dirname, 'home')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'home', 'index.html'));
});

app.get('/execute', (req, res) => {
    const command = req.query.command;
    const pass = req.query.pass;

    if (pass !== 'admin') {
        res.send('パスワードが違います');
        return;
    }

    exec(command, (error, stdout, stderr) => {
        if (error) {
            res.send(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            res.send(`stderr: ${stderr}`);
            return;
        }
        res.send(`stdout: ${stdout}`);
    });
});

const server = app.listen(port, '0.0.0.0', () => {
    console.log(`Server is running at http://0.0.0.0:${port}`);
});
