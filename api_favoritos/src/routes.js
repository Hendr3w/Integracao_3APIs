// src/routes.js

const express = require('express');
const router = express.Router();
const favoritosController = require('./controllers/favoritosController');

// Rota para adicionar músicas aos favoritos
router.post('/favoritos', favoritosController.adicionarFavoritos);

// Rota para listar os favoritos de um usuário
router.get('/favoritos/:user_id', favoritosController.listarFavoritos);

module.exports = router;
