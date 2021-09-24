from src import app
import src

if __name__ == "__main__":
    app.register_error_handler(404, src.pagina_no_encontrada)
    app.run()
