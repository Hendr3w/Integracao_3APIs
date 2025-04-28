// Simulação do banco de dados em memória
let favoritos = [];

// Função para salvar favorito em memória
const salvarFavorito = (user_id, musica_id) => {
  const favorito = { user_id, musica_id };
  favoritos.push(favorito);  // Simula a inserção no banco
  return favorito;  // Retorna o objeto favoritado
};

// Função para buscar os favoritos de um usuário em memória
const buscarFavoritos = (user_id) => {
  return favoritos.filter(favorito => favorito.user_id === user_id);
};

module.exports = { salvarFavorito, buscarFavoritos };
