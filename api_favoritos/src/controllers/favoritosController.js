// src/controllers/favoritosController.js

const favoritos = []; // Um array para armazenar os favoritos (aqui você pode substituir por banco de dados ou outra coisa mais tarde)

// Função para adicionar músicas aos favoritos
exports.adicionarFavoritos = (req, res) => {
    const { user_id, musica_ids } = req.body;

    // Verificar se os dados necessários foram fornecidos
    if (!user_id || !Array.isArray(musica_ids) || musica_ids.length === 0) {
        return res.status(400).json({ mensagem: "É necessário fornecer um ID de usuário e um array de IDs de músicas." });
    }

    // Adicionar os favoritos
    musica_ids.forEach(musica_id => {
        favoritos.push({ user_id, musica_id });
    });

    return res.status(200).json({
        mensagem: "Músicas adicionadas aos favoritos!",
        favoritos
    });
};

// Função para listar os favoritos de um usuário
exports.listarFavoritos = (req, res) => {
    const { user_id } = req.params;

    // Filtrar favoritos pelo user_id
    const favoritosUsuario = favoritos.filter(fav => fav.user_id === parseInt(user_id));

    if (favoritosUsuario.length === 0) {
        return res.status(404).json({ mensagem: "Nenhum favorito encontrado para este usuário." });
    }

    return res.status(200).json(favoritosUsuario);
};
