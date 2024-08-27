from dash import Dash, Input, Output, callback, page_container
from dash.dcc import Location
from dash_bootstrap_components import Col, Container, Row, Stack, icons, themes
from dashboard import cabecalho, minha_sidebar, processamento_dados
from modulos.uteis import carregar_env


def aplicacao():
    # Inicializacao dados
    ## Carregando env
    carregar_env.carregar_env()

    ## Query banco de dados
    global df
    df = processamento_dados.dados_mais_recentes()

    ## Processamento
    ### Cabecalho
    global data_coleta
    data_coleta = processamento_dados.data_coleta(df)

    ### Pagina 2
    global pagina_2_dag_dados
    pagina_2_dag_dados = processamento_dados.inicializacao_pagina_2(df)

    # Dashboard
    app = Dash(
        __name__,
        external_stylesheets=[themes.LUMEN, icons.FONT_AWESOME],
        update_title=None,
        assets_folder="../assets/",
        use_pages=True,
        pages_folder="./dashboard/paginas",
        suppress_callback_exceptions=True,
        meta_tags=[
            {
                "name": "viewport",
                "content": "width=device-width, initial-scale=1.0",
            },
            {
                "http-equiv": "Content-Language",
                "content": "pt-BR",
            },
            {
                "name": "author",
                "content": "Fenyx Forte",
            },
            {
                "name": "application-name",
                "content": "Pesquisa de Mercado: Tênis de Corrida no Mercado Livre",
            },
            {
                "name": "keywords",
                "content": "webscraping dashboard dados",
            },
            {
                "name": "google",
                "content": "notranslate",
            },
            {
                "name": "robots",
                "content": "index, follow",
            },
            {
                "name": "googlebot",
                "content": "index, follow",
            },
        ],
    )

    app.layout = Container(
        [
            Location(id="url"),
            Row(
                [
                    Col(minha_sidebar.sidebar(), width="auto"),
                    Col(
                        Stack(
                            [
                                cabecalho.cabecalho(data_coleta),
                                page_container,
                            ],
                        ),
                        width=True,
                    ),
                ],
            ),
        ],
        fluid=True,
    )

    server = app.server

    return server


# Callbacks
## Inicializacao
### Pagina 2
@callback(
    Output("meu-dag", "rowData"),
    Input("input-estatico", "children"),
)
def inicializacao_pagina_2(_):
    return pagina_2_dag_dados


## Pagina 2
@callback(
    Output("meu-dag", "exportDataAsCsv"),
    Input("botao-exportar-csv", "n_clicks"),
    prevent_initial_call=True,
)
def exportar_csv(n_clicks):
    if n_clicks:
        return True
    return False
