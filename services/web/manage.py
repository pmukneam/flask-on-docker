from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
    app.run(debug=True, host='0.0.0.0', port=988813)
