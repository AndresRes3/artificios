from flask import Flask, request, jsonify
from m_analyzer import contains_artifact_clue
from database import insert_manuscript,get_stats


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


    # res = ' '.join([str(manuscript[i][j]) for i in range(len(manuscript)) for j in range(len(manuscript[i]))])
    # Ejecutar la función
    has_clue = contains_artifact_clue(manuscript)

    #Guardar BD
    try: 
        # print(res)
        # print()
        insert_manuscript(manuscript,has_clue)
    except Exception as e:
        print('HOLA ')
        print(f'{e}')
        return jsonify({"message": f"Error conectando base de datos: {str(e)}"}), 500

    if has_clue:
        return jsonify({"message": "Pista encontrada"}), 200
    else:
        return jsonify({"message": "No se encontró pista"}), 403


@app.route('/stats/', methods=['GET'])
def get_statistics():
    """Retorna estadísticas de los manuscritos analizados."""
    stats = get_stats()
    return jsonify(stats), 200


if __name__ == '__main__':
    app.run(debug=True)