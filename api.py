from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvenido a la API del curriculum vitae de Marisol Castilla.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes"
        ]
    }
    return jsonify(info)

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/mifoto.png"
    cv = {
        "nombre" : "Marisol",
        "apellido" : "Castilla",
        "residencia" : "Colombia",
        "experiencia" : [{
            "posicion" : "< Ingeniero desarrollador>",
            "empresa" : "< Tracker de Colombia >",
            "desde" : "< cuándo empezaste a trabajar >",
            "hasta" : "< si ya no trabajas más, cuándo >",
            "descripcion" : "< detalles >"
        }],
        "educación" : {
            "nivel" : "< Profesional >",
            "titulo" : "< Ingeniero de Sitemas >",
            "institucion" : "< Fundacion Universitaria Tecnologico comfenalco >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["python", "apis", "Deportes: Ciclismo"],
        "redes" : {
            "github" : "https://github.com/mcastillaz",
            "facebook" : "https://www.facebook.com/marisol.castillazambrano",
            "linkedin" : "https://www.linkedin.com/in/marisol-castilla-zambrano"
        },
        "foto" : url_imagen
    }
    return jsonify(cv)

    @app.route('/mensajes', methods=['POST'])
    def contacto():
        mensaje = request.get_data()
        if not mensaje:
            abort(400, description="Debe enviar su mensaje en el body del POST.")
        print("MENSAJE DE CONTACTO: " + str(mensaje))
        return "Gracias por su mensaje."



if __name__ == '__main__':
    ##app.run(debug=True)
    app.run()