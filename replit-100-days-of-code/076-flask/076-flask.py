from flask import Flask

app = Flask(__name__,static_url_path="/static")

@app.route("/")
def index():
    page = """
    <p><a href="/portfolio">Mi Portafolio</a></p>
    <p><a href="/linktree">Link Tree</a></p>
    """
    return page


@app.route("/portfolio")
def portfolio():
    page = """
<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Portafolio</title>
  <link rel="stylesheet" href="static/css/portfolio-style.css">
</head>

<body>
  <header>
    <h1>Portafolio de Agustín</h1>
  </header>
  <main>
    <section id="introduction">
      <h2>¡Bienvenido a mi portafolio!</h2>
      <p>
        En este sitio web podrás encontrar una muestra de mis proyectos más recientes escritos en Python. Desde
        juegos hasta aplicaciones utilitarias, aquí encontrarás una variedad de proyectos interesantes y útiles.
      </p>
    </section>
    <section id="project-section">
      <h2>Ahorcado</h2>
      <p>
        Este proyecto es el juego del ahorcado escrito en Python. El juego elige una palabra al azar de una lista de
        palabras y luego pide al usuario que adivine las letras una por una. Si el usuario adivina una letra
        correctamente,
        se muestra la letra en su lugar en la palabra oculta. Si el usuario elige una letra incorrecta, se le resta una
        vida. El juego continúa hasta que el usuario adivine la palabra o se quede sin vidas.
      </p>
      <div>
        <a href="https://replit.com/@agustin-comolli/Dia-39-de-100?v=1">
          <img src="static/images/hangman.png" alt="Ahorcado" id="hangman">
        </a>
      </div>

      <h2>Star Wars</h2>
      <p>
        Este proyecto es un juego que permite a los usuarios comparar personajes de Star Wars utilizando diferentes
        estadísticas. El juego muestra un menú con una lista de personajes y luego permite al usuario elegir dos
        personajes
        para comparar. Luego, se le pide al usuario que elija una estadística para comparar y el juego muestra una
        pantalla
        con las estadísticas de cada personaje. Al final, el juego muestra quién es el ganador de la comparación.
      </p>
      <div>
        <a href="https://replit.com/@agustin-comolli/Dia-47-de-100?v=1">
          <img src="static/images/star-wars.png" alt="Star Wars" id="star-wars">
        </a>
      </div>

      <h2>Caculadora</h2>
      <p>
        Este proyecto es una calculadora escrita en Python utilizando la librería gráfica Tkinter. La calculadora tiene
        una
        interfaz gráfica y permite al usuario realizar operaciones matemáticas básicas como sumar, restar, multiplicar y
        dividir. También tiene una función de reinicio y una función que muestra un mensaje de error si se intenta
        dividir
        por cero. La calculadora también tiene la capacidad de manejar decimales y puede realizar operaciones
        consecutivas
        utilizando el operador "=".
      </p>
      <div>
        <a href="https://replit.com/@agustin-comolli/Dia-66-de-100?v=1">
          <img src="static/images/calculator.png" alt="Caculadora" id="calculator">
        </a>
      </div>

      <h2>¿Quién es Quién?</h2>
      <p>
        Este proyecto es un juego que consiste en adivinar qué imagen se está mostrando en la pantalla. El usuario debe
        ingresar el nombre de la imagen en una caja de texto y presionar el botón "Buscar". Si la entrada del usuario es
        correcta, se mostrará una nueva imagen y el usuario debe seguir adivinando. Si la entrada es incorrecta o si el
        usuario llega a la última imagen y no ha adivinado correctamente, se mostrará un mensaje de que ha perdido y se
        habilitará un botón para reiniciar el juego. Si el usuario adivina correctamente la última imagen, se mostrará
        un
        mensaje de que ha ganado y también se habilitará un botón para reiniciar el juego.
      </p>
      <div>
        <a href="https://replit.com/@agustin-comolli/Dia-67-de-100?v=1">
          <img src="static/images/who-is-who.png" alt="¿Quién es Quién?" id="who-is-who">
        </a>
      </div>

      <h2>Diario Secreto Seguro</h2>
      <p>
        Este proyecto es una aplicación que permite crear un diario personal con contraseña. Cuenta con las siguientes
        funciones:
      </p>
      <ul>
        <li>Agregar una entrada al diario</li>
        <li>Ver las entradas del diario, permitiendo ver una entrada a la vez y preguntando si se desea ver la siguiente
        </li>
        <li>Iniciar sesión, verificando el nombre de usuario y la contraseña encriptada</li>
        <li>Crear un usuario para acceder al diario, encriptando la contraseña y guardando los datos en un archivo</li>
        <li>Borrar todas las entradas del diario</li>
        <li> Salir de la aplicación.</li>
      </ul>
      <div>
        <a href="https://replit.com/@agustin-comolli/Dia-72-de-100?v=1">
          <img src="static/images/secured-secret-diary.png" alt="Diario Secreto Seguro" id="secret-diary">
        </a>
      </div>
    </section>
  </main>
  <footer>
    <h3>Contacto</h3>
    <p>Si tienes alguna pregunta o comentario acerca de mis proyectos, no dudes en ponerte en contacto
      conmigo. <br>
      <a href="mailto:agustincomolli@gmail.com">agustincomolli@gmail.com</a>
    </p>
  </footer>
</body>

</html>    
    """
    return page


@app.route("/linktree")
def linktree():
    page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Link Tree</title>
    <link rel="stylesheet" href="static/css/linktree-style.css">
</head>
<body>
    <header>
        <img src="static/images/logo.png" alt="Logotipo de Agustín">
        <h1>Agustín Comolli</h1>
        <p>Soporte técnico IT</p>
    </header>
    <main>
        <h3>Redes Sociales</h3>
        <ul>
            <li><a href="">GitHub</a></li>
            <li><a href="">Replit</a></li>
            <li><a href="">Facebook</a></li>
        </ul>
    </main>
    <footer></footer>
</body>
</html>    
    """
    return page


app.run(host='0.0.0.0', port=81)