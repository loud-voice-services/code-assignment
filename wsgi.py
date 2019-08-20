from app import api

app=api.get_api()


@app.route("/")
def hello():
    return "<a href='/ui/'> Acesse a documentacao aqui. </a>"


if __name__ == "__main__":
    app.run()