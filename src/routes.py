from flask import render_template, request, redirect
from src.tarefas import tarefas


def configurar_rotas(app):

    @app.route("/")
    def home():
        return render_template("index.html", tarefas=tarefas)

    @app.route("/adicionar", methods=["POST"])
    def adicionar():

        tarefa = request.form.get("tarefa")

        if tarefa:
            tarefas.append(tarefa)

        return redirect("/")

    @app.route("/editar/<int:id>")
    def editar(id):

        return render_template(
            "editar.html",
            id=id,
            tarefa=tarefas[id]
        )

    @app.route("/atualizar/<int:id>", methods=["POST"])
    def atualizar(id):

        tarefas[id] = request.form.get("tarefa")

        return redirect("/")

    @app.route("/excluir/<int:id>")
    def excluir(id):

        tarefas.pop(id)

        return redirect("/")