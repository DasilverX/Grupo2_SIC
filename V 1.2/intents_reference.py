import json

def save_json(data):
    file = open("intents.json","w")
    json.dump(data, file, indent=4)

def start_intents():
    text = {
                "intents": [
                    {
                        "tag": "saludos",
                        "patterns": [
                            "hola",
                            "buenos dias",
                            "buenas tardes",
                            "buenas noches",
                            "como estas",
                            "hay alguien ahi?",
                            "hey",
                            "saludos",
                            "que tal",
                            "que sopa",
                            "habla",
                            "hi",
                            "hello",
                            "q xopa"
                        ],
                        "responses": [
                            "ESTOY EN PRE-ALPHA/nhola soy Miguel BOT. ¿En que puedo ayudarte?"
                        ],
                        "context": [
                            ""
                        ]
                    },
                    {
                        "tag": "despedidas",
                        "patterns": [
                            "chao",
                            "adios",
                            "hasta luego",
                            "nos vemos",
                            "bye",
                            "hasta pronto",
                            "hasta la proxima"
                        ],
                        "responses": [
                            "hasta luego, tenga un buen dia",
                            "ha sido un placer, vuelva pronto"
                        ],
                        "context": [
                            ""
                        ]
                    },
                    {
                        "tag": "agradecimientos",
                        "patterns": [
                            "gracias",
                            "muchas gracias",
                            "mil gracias",
                            "muy amable",
                            "se lo agradezco",
                            "fue de ayuda",
                            "gracias por la ayuda",
                            "muy agradecido",
                            "gracias por su tiempo",
                            "ty"
                        ],
                        "responses": [
                            "de nada",
                            "feliz por ayudarlo",
                            "gracias a usted",
                            "estamos para servirle",
                            "fue un placer"
                        ],
                        "context": [
                            ""
                        ]
                    },
                    {
                        "tag": "norespuesta",
                        "patterns": [
                            ""
                        ],
                        "responses": [
                            "no se detecto una respuesta"
                        ],
                        "context": [
                            ""
                        ]
                    }
                ]
            }
    save_json(text)
