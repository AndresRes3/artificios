from flask import Flask, request, jsonify
from m_analyzer import contains_artifact_clue

app = Flask(__name__)

@app.route('/clue/', methods=['POST'])
def analyze_manuscript():
    """
    Recibe un manuscrito en formato JSON y determina si contiene una pista.
    Retorna:
      - HTTP 200 OK si hay una pista.
      - HTTP 403 Forbidden si no hay pista.
    """
    data = request.get_json()

    # Validar que cumpla con la clave "manuscript"
    if not data or "manuscript" not in data:
        return jsonify({"error": "Falta el campo 'manuscript'"}), 400
    
    manuscript = data["manuscript"]

    # Validar que manuscript sea una lista de strings
    if not isinstance(manuscript, list) or not all(isinstance(line, str) for line in manuscript):
        return jsonify({"error": "Formato incorrecto: 'manuscript' debe ser una lista de strings"}), 400

    # Ejecutar la función
    has_clue = contains_artifact_clue(manuscript)

    if has_clue:
        return jsonify({"message": "Pista encontrada"}), 200
    else:
        return jsonify({"message": "No se encontró pista"}), 403

if __name__ == '__main__':
    app.run(debug=True)