const express = require('express');
const app = express();
const routes = require('./routes');

// Middleware para permitir o parsing de JSON no corpo das requisições
app.use(express.json());

// Usando as rotas
app.use('/api', routes);

// Porta para a API
const port = 5002;
app.listen(port, () => {
  console.log(`API Favoritos rodando na porta ${port}`);
});
