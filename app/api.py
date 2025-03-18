from flask import Flask, request, jsonify
from m_analyzer import contains_artifact_clue
from database import insert_manuscript,get_stats


app = Flask(__name__)

@app.route('/clue/', methods=['POST'])
def analyze_manuscript():
    """
      - HTTP 200 OK si hay una pista.
      - HTTP 403 Forbidden si no hay pista.
    """
    data = request.get_json()

    if not data or "manuscript" not in data:
        return jsonify({"error": "Falta el campo 'manuscript'"}), 400
    
    manuscript = data["manuscript"]

    if not isinstance(manuscript, list) or not all(isinstance(line, str) for line in manuscript):
        return jsonify({"error": "Formato incorrecto: 'manuscript' debe ser una lista de strings"}), 400
    
    has_clue = contains_artifact_clue(manuscript)

    try: 
        insert_manuscript(manuscript,has_clue)
    except Exception as e:
        return jsonify({"message": f"Error conectando base de datos: {str(e)}"}), 500

    if has_clue:
        return jsonify({"message": "Elowen el manuscrito contenia una pista"}), 200
    else:
        return jsonify({"message": "Lo siento Elowen no he encontrado ninguna pista"}), 403


@app.route('/stats/', methods=['GET'])
def get_statistics():

    try:
        stats = get_stats()
        return jsonify(stats), 200
    except Exception as e:
        return jsonify({"message": f"No se pueden traer las estadisticas en este momento {str(e)}"}), 503


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000 ,debug=True)