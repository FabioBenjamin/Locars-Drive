from flask import Blueprint, render_template, jsonify, request

veiculos_bp = Blueprint('veiculos', __name__)

VEICULOS_MOCK = [
    {
        'id': 1,
        'modelo': 'Honda Civic',
        'ano': 2022,
        'cor': 'Preto',
        'disponivel': True
    },
    {
        'id': 2,
        'modelo': 'Toyota Corolla',
        'ano': 2023,
        'cor': 'Branco',
        'disponivel': False
    },
    {
        'id': 3,
        'modelo': 'Ford Mustang',
        'ano': 2021,
        'cor': 'Vermelho',
        'disponivel': True
    },
    {
        'id': 4,
        'modelo': 'Chevrolet Camaro',
        'ano': 2020,
        'cor': 'Azul',
        'disponivel': True
    },
]

# Rotas para renderizar páginas HTML
@veiculos_bp.route('/')
def veiculos():
    return render_template('veiculos.html')

@veiculos_bp.route('/<int:veiculo_id>')
def detalhe_veiculo(veiculo_id):
    return render_template('detalhe_veiculo.html', veiculo_id=veiculo_id)

# Rotas de API REST
@veiculos_bp.route('/veiculos', methods=['GET'])
def listar_veiculos():
    return jsonify(VEICULOS_MOCK)

@veiculos_bp.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def obter_veiculo(veiculo_id):
    veiculo = next((v for v in VEICULOS_MOCK if v['id'] == veiculo_id), None)
    if veiculo:
        return jsonify(veiculo)
    return jsonify({'error': 'Veículo não encontrado'}), 404

@veiculos_bp.route('/veiculos', methods=['POST'])
def adicionar_veiculo():
    novo_veiculo = request.get_json(silent=True)
    if novo_veiculo:
        return jsonify(novo_veiculo), 201
    return jsonify({"erro": "O formato da requisição deve ser JSON"}), 400

@veiculos_bp.route('/veiculos/<int:veiculo_id>', methods=['PUT'])
def atualizar_veiculo(veiculo_id):
    veiculo = next((v for v in VEICULOS_MOCK if v['id'] == veiculo_id), None)
    if not veiculo:
        return jsonify({'error': 'Veículo não encontrado'}), 404

    dados_atualizados = request.get_json(silent=True)
    if dados_atualizados:
        veiculo.update(dados_atualizados)
        return jsonify(veiculo), 200
    return jsonify({"erro": "O formato da requisição deve ser JSON"}), 400

@veiculos_bp.route('/veiculos/<int:veiculo_id>', methods=['DELETE'])
def deletar_veiculo(veiculo_id):
    veiculo = next((v for v in VEICULOS_MOCK if v['id'] == veiculo_id), None)
    if not veiculo:
        return jsonify({'error': 'Veículo não encontrado'}), 404

    VEICULOS_MOCK.remove(veiculo)
    return jsonify({'message': 'Veículo deletado com sucesso'}), 200
