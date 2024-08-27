from dash import html

from dashboard import processamento_dados


def cabecalho() -> html.Div:
    conteudo = html.Div(
        [
            html.H1(
                "Pesquisa de Mercado: Tênis de Corrida no Mercado Livre",
                className="text-primary text-center fs-3",
                id="titulo-aplicacao",
            ),
            html.H4(
                f"Data Coleta: {processamento_dados.recuperar_data_coleta()}",
                className="text-center",
                id="data-coleta",
            ),
            html.Hr(),
        ],
        className="cabecalho",
    )

    return conteudo
