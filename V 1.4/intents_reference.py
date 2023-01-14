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
                        "Hola soy Miguel BOT. \u00bfEn que puedo ayudarte?",
                        "Hola, muy buenas, ¿En qué puedo ayudarte?",
                        "Muy buenas, ¡Cuentame!",
                        "Estas hablando con MIGUEL-BOT, ¿En qué puedo ayudarte?",
                        "Saludos humano, ¿En qué puedo servirte?"
                    ],
                    "context": [
                        "saludo",
                        "conociendo"
                        "desconocido"
                    ]
                },
                {
                    "tag": "busqueda",
                    "patterns": [
                        "busca,",
                        "dime quien es,",
                        "cuentame sobre,",
                        "/busca,",
                        "que es,",
                        "quien fue,",
                        "investiga sobre,"
                    ],
                    "responses": [
                        "Claro, dame un momento",
                        "Sin problemas",
                        "Buscando...",
                        "¿Y eso se come? Es broma, ya te digo, jajaja",
                        "Se dice por favor, pero ya te ayudo..."
                    ],
                    "context": [
                        "comando", 
                        "buscar",
                        "peticion"
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
                    "tag": "pregunta",
                    "patterns": [
                        "que puedes hacer",
                        "que haces",
                        "en que me puedes ayudar",
                        "dime lo que haces",
                        "ayudame",
                        "como me puedes ayudar",
                        "help"
                    ],
                    "responses": [
                        "-Si quieres que te busque algo en wikipedia pidemelo, por ejemplo: *Dime quien es, Pablo Escobar*. Con la coma, así puedo ayudarte /n De momento no puedo hacer nada más, pero el equipo que trabaja en mi est\u00e1 a\u00f1adiendo muchas funciones para mi."
                    ],
                    "context": [
                        ""
                    ]
                },
                {
                    "tag": "no_response",
                    "patterns": [
                        ""
                    ],
                    "responses": [
                        "No te he logrando entender, intentalo de nuevo.",
                        "¿Cómo has dicho, disculpa?",
                        "Lo siento, no entiendo lo que me pides...",
                        "Repiteme, por favor",
                        "¿Qué has dicho?"
                    ],
                    "context": [
                        ""
                    ]
                }
            ]
        }
    save_json(text)
