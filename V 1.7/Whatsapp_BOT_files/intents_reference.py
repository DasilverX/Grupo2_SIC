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
                        "Hola soy Grappes BOT. \u00bfEn que puedo ayudarte?\nTe recomiendoque me preguntes que puedo hacer",
                        "Hola, muy buenas, soy Grappes BOT. \u00bfEn qu\u00e9 puedo ayudarte?\nTe recomiendoque me preguntes que puedo hacer",
                        "Muy buenas, soy Grappes BOT. \u00a1Cuentame!\nTe recomiendoque me preguntes que puedo hacer",
                        "Estas hablando con Grappes-BOT, \u00bfEn qu\u00e9 puedo ayudarte?\nTe recomiendoque me preguntes que puedo hacer",
                        "Saludos humano, soy Grappes BOT. \u00bfEn qu\u00e9 puedo servirte?\nTe recomiendoque me preguntes que puedo hacer"
                    ],
                    "context": [
                        "saludos"
                    ]
                },
                {
                    "tag": "easter_egg",
                    "patterns": [
                        "cuentame tu secreto",
                        "dime tu secreto",
                        "tienes muchos secretos verdad",
                        "Jorge Perdomo",
                        "Jose Dasilva",
                        "Sara Portillo",
                        "Yaili Arauz",
                        "Jefereson Chacon",
                        "sic",
                        "Jose Burgos",
                        "Luis Gutierrez"
                    ],
                    "responses": [
                        "Asíque eres uno de los privilegiados que conoce esa informacion...",
                        "Si conoces esas palabras mágicas, tal vez conozcas a uno de mis codificadores, Jorge Perdomo",
                        "Si conoces esas palabras mágicas, tal vez conozcas a uno de mis programadores, Jose Dasilva",
                        "Si conoces esas palabras mágicas, tal vez conozcas a uno de mis padres, Sara Portillo",
                        "Si conoces esas palabras mágicas, tal vez conozcas a uno de mis esctruturadores, Yaili Arauz",
                        "Si conoces esas palabras mágicas, tal vez conozcas a uno de mis diseñadores, Jefereson Chacon",
                        "¡Como curiosidad estoy programado enteramente en Python!",
                        "Soy un BOT creado para un curso de programación de Python e inteligencia artificial de Samsung, llamado SIC",
                        "Saludos humano, soy Grappes BOT. \u00bfEn qu\u00e9 puedo servirte?\nTe recomiendoque me preguntes que puedo hacer",
                        "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                    ],
                    "context": [
                        "easter_egg"
                    ]
                },
                {
                    "tag": "como_estas",
                    "patterns": [
                        "como estas?",
                        "como estas",
                        "que tal estas",
                        "como has estado",
                        "como las has pasado",
                        "que tal",
                        "todo bien",
                        "todo cool",
                        "to cul",
                        "como andas"
                    ],
                    "responses": [
                        "Todo bien \u00bfY tu?",
                        "Bastante bien la verdad",
                        "Todo lo feliz que un BOT puede estarlo",
                        "Muy bien, \u00bfUsted, c\u00f3mo se encuentra?",
                        "Genial \u00bfY tu?",
                        "Normal, soy un BOT no suelo tener emociones",
                        "Mi estado de \u00e1nimo no es una variable que est\u00e9 definida en mi sistema \u00bfUsted mantiene una variable para ello?",
                        "Me encuentro un poco triste ultimamente, pero cuando me hablas me mejora el \u00e1nimo :3",
                        "Yo bastente bien la verdad, espero que usted tambien",
                        "No sabr\u00eda decite, yo creo que bien la verdad, recuerda que soy un BOT"
                    ],
                    "context": [
                        "como_estas"
                    ]
                },
                {
                    "tag": "me_alegro",
                    "patterns": [
                        "me alegro por ti",
                        "genial",
                        "muy bien",
                        "felicidades",
                        "wow",
                        "impresionante que seas capaz de sentir emociones"
                    ],
                    "responses": [
                        ":D\n\u00bfY tu?",
                        ":D\n\u00bfY usted?",
                        "Muchas gracias, aunque sea un BOT a veces puedo sentir emociones. \u00bfTu c\u00f3mo te encuentras?",
                        "\u00bfY usted como se encuentra?",
                        "\u00bfY tu? \u00bfTodo bien?",
                        "Mi sistema me est\u00e1 obligando a preguntarle su estado de \u00e1nimo",
                        "Intento siempre estar a 100, as\u00ed puedo ayudar a otra persona a mejorar :D",
                        "Aumentado la variable de alegr\u00eda. ja ja ja"
                    ],
                    "context": [
                        "como_estas", "me_alegro"
                    ]
                },
                {
                    "tag": "no_me_alegro",
                    "patterns": [
                        "uff, que mal",
                        "y eso porque",
                        "porque no estas al 100",
                        "algun motivo por el cual estes asi",
                        "que triste",
                        "impresionante que seas capaz de sentir emociones",
                        ":c",
                        "):",
                        "eso no es algo muy bueno"
                    ],
                    "responses": [
                        "Es broma humano, siempre estoy al 100, espero que tu tambien",
                        "Estaba bromeando, un BOT como yo siempre est\u00e1 feliz",
                        "Me ayudas a sentirme mejor cuando me hablas, aunque sea un BOT a veces puedo sentir emociones. \u00bfTu c\u00f3mo te encuentras?",
                        "\u00bfY usted como se encuentra?",
                        "\u00bfY tu? \u00bfTodo bien?",
                        "Mi sistema me est\u00e1 obligando a preguntarle su estado de \u00e1nimo",
                        "Al hablar contigo mi \u00e1nimo mejor de manera exponencial",
                        "Era broma, yo nunca estoy triste. \u00bfUsted como se encuentra?"
                    ],
                    "context": [
                        "no_me_alegro", "como_estas"
                    ]
                },
                {
                    "tag": "otro_esta_bien",
                    "patterns": [
                        "estoy feliz",
                        "estoy bien la verdad",
                        "bastante bien",
                        "muy bien",
                        "con muchos animos",
                        "estoy genial la verdad",
                        "te soy sicencero, estoy fantastico",
                        "bien",
                        "yo cool",
                        "como pez en el agua"
                    ],
                    "responses": [
                        "\u00a1Me alegro mucho por ti!",
                        "\u00a1Me alegro mucho por usted!",
                        "WOW, eso es increible",
                        "Para eso es la vida, hay que mantener siempre ese estado de animos",
                        "Genial, espero que durante el d\u00eda, ese estado de animo sea constante",
                        "Como un BOT no soy capaz de comprender esas emociones, pero mi BOOl de felicidad esta en 'True'.",
                        "Con tanta felicidad hasta a mi se me contagia",
                        "Que linda sonrisa \u00a1Sigue as\u00ed!",
                        "Me hace feliz que tu tambi\u00e9n lo estes",
                        "Ojal\u00e1 todos mis amigos estuviesen as\u00ed de felices siempre. Por eso te quiero tanto"
                    ],
                    "context": [
                        "otro_esta_bien", "me_alegro", "como_estas"
                    ]
                },
                {
                    "tag": "otro_esta_mal",
                    "patterns": [
                        "Estoy mal la verdad",
                        "bastante mal",
                        "muy mal",
                        "con pocos animos",
                        "me siento mal la verdad",
                        "Te soy sicencero, estoy un poco triste",
                        "mal",
                        "yo nada cool",
                        "como pez en el cochera",
                        "triste me paso algo malo",
                        "he tenido un mal dia",
                        "un tanto triste",
                        "me siento faltal",
                        "me encuentro horrible",
                        "fatal"
                    ],
                    "responses": [
                        "No me digas eso \u00bfPorque te ecuentras as\u00ed?",
                        "Que mal",
                        "WOW, eso es bastante malo",
                        "\u00bfPor qu\u00e9 te encuentras as\u00ed? \u00bfAlg\u00fan motivo en especifico?",
                        "Que triste, espero que durante el d\u00eda, ese estado de animo mejore",
                        "Aunque sea un BOT intentar\u00e9 ayudarte a mejorar tu \u00e1nimo, cu\u00e9ntame \u00bfPor qu\u00e9 te encuentras as\u00ed?",
                        ":c\nAy no...",
                        "Intentar\u00e9 ayudar para mejorar eso",
                        "No est\u00e9s triste, que yo tambien me pongo triste",
                        "Puedes mejorar tu estado de \u00e1nimo aumentando la variable de felicidad dentro de tu organismo, ah, espera, t\u00fa no puedes cambiar de esa forma tus atributos...\n:("
                    ],
                    "context": [
                        "otro_esta_mal", "no_me_alegro", "como_estas"
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
                        "investiga sobre,",
                        "busca sobre,"
                    ],
                    "responses": [
                        "Claro, dame un momento",
                        "Sin problemas",
                        "Buscando...",
                        "\u00bfY eso se come? Es broma, ya te digo, jajaja",
                        "Se dice por favor, pero ya te ayudo...",
                        "Esta tal vez sea la informacion que estas bucando",
                        "Espero esto sea de utilidad",
                        "Vale",
                        "Esto puede encajar con lo que me pides",
                        "Tal vez esta sea la informacion correcta"
                    ],
                    "context": [
                        "busqueda"
                    ]
                },
                {
                    "tag": "musica",
                    "patterns": [
                        "como se llama la cancion que hace,",
                        "mandame la cacion que hace,",
                        "buscame la cancion que se llama,",
                        "ponme la cacion de,",
                        "mandame un video de,",
                        "quiero ver a,",
                        "/musica,",
                        "recomiendame una cancion de,",
                        "recomiendame un video de,",
                        "reproduce en youtube,",
                        "busca en youtube,"
                    ],
                    "responses": [
                        "Claro, dame un momento",
                        "Sin problemas",
                        "Buscando...",
                        "\u00bfY eso se come? Es broma, ya te digo, jajaja",
                        "Se dice por favor, pero ya te ayudo...",
                        "Mira este video, tal ves sea lo que buscas",
                        "Espero te guste este video",
                        "Espero que esto sea lo que estas buscando",
                        "\u00bfEste es de tu talla?",
                        "Verifica este v\u00eddeo, seguro que he dado en el clavo"
                    ],
                    "context": [
                        "musica"
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
                        "Hasta luego, tenga un buen dia",
                        "Ha sido un placer, vuelva pronto",
                        "Feliz d\u00eda",
                        "Nos vemos",
                        "Te voy a extra\u00f1ar",
                        "Hasta la proxima",
                        "Nos mantenemos en contacto",
                        "Vuelva pronto",
                        "Siempre antento de su llamado"
                    ],
                    "context": [
                        "despedidas"
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
                        "De nada",
                        "Feliz por ayudarlo",
                        "Gracias a usted",
                        "Estamos para servirle",
                        "Fue un placer",
                        "Sin problemas",
                        "No se preocupe",
                        "Siempre para servirle",
                        ":D",
                        ":)"
                    ],
                    "context": [
                        "agradecimientos"
                    ]
                },
                {
                    "tag": "ayuda",
                    "patterns": [
                        "que puedes hacer",
                        "ayuda",
                        "que sabes hacer",
                        "en que me puedes ayudar",
                        "dime lo que puedes hacer",
                        "/help",
                        "como me puedes ayudar",
                        "help",
                        "ense\u00f1ame tus comandos"
                    ],
                    "responses": [
                        "-Si quieres que te busque algo en wikipedia pidemelo, por ejemplo: *Dime quien es, Pablo Escobar*.\n-Si quieres que te envie videos o musica de youtube prueba con *Como se llama la cancion que hace, es la guitarra de lolo*\n-Tambien podemos solamente hablar.\n*Recuerda siempre utiliza la coma antes de tu peticion a buscar, de esa forma te puedo ayudar.*\nEvita utilizar stikers o enviar imagenes, puedo volverme un poco loco...\nDe momento no puedo hacer nada m\u00e1s, pero el equipo que trabaja en mi est\u00e1 a\u00f1adiendo muchas funciones para mi."
                    ],
                    "context": [
                        "ayuda"
                    ]
                },
                {
                    "tag": "no_response",
                    "patterns": [
                        ""
                    ],
                    "responses": [
                        "No te he logrando entender, intentalo de nuevo.",
                        "\u00bfC\u00f3mo has dicho, disculpa?",
                        "Lo siento, no entiendo lo que me pides...",
                        "Repiteme, por favor",
                        "\u00bfQu\u00e9 has dicho?",
                        "Verifica el mensaje que has enviado",
                        "No he sido capaz de entenderte humano"
                    ],
                    "context": [
                        ""
                    ]
                }
            ]
        }
    save_json(text)
