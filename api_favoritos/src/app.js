const express = require('express');
const app = express();
const routes = require('./routes');

app.use(express.json());

app.use('/api', routes);

const port = 5002;
app.listen(port, () => {
  console.log(`API Favoritos rodando na porta ${port}`);
});
