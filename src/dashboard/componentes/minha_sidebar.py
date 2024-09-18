from dash import (
    Input,
    Output,
    clientside_callback,
    html,
)
from dash_bootstrap_components import Nav, NavLink


def botao_toggle() -> html.Div:
    conteudo = html.Div(
        html.I(className="fas fa-bars"),
        className="meu-toggle-navbar",
        id="meu-toggle-navbar",
    )

    return conteudo


def links_minhas_informacoes() -> html.Div:
    conteudo = html.Div(
        [
            html.A(
                [
                    html.Img(
                        src="/assets/images/portfolio.ico",
                        className="meu-icone",
                    ),
                    html.Label("Portfólio"),
                ],
                href="https://fenyx-forte.github.io/",
                target="_blank",
                rel="noreferrer",
            ),
            html.Br(),
            html.A(
                [
                    html.I(className="fa-brands fa-linkedin-in"),
                    html.Label("Linkedin"),
                ],
                href="https://www.linkedin.com/in/fenyxforte/",
                target="_blank",
                rel="noreferrer",
            ),
            html.Br(),
            html.A(
                [
                    html.I(className="fa-brands fa-github"),
                    html.Label("GitHub"),
                ],
                href="https://github.com/Fenyx-Forte",
                target="_blank",
                rel="noreferrer",
            ),
            html.Br(),
            html.A(
                [
                    html.I(className="fa-brands fa-google"),
                    html.Label("Gmail"),
                ],
                href="mailto:fenyxforte@gmail.com",
                target="_blank",
                rel="noreferrer",
            ),
        ],
    )

    return conteudo


def minhas_informacoes() -> html.Div:
    conteudo = html.Div(
        [
            html.H1("Fenyx Forte", className="text-primary"),
            html.Hr(),
            links_minhas_informacoes(),
        ]
    )

    return conteudo


def links_paginas() -> Nav:
    conteudo = Nav(
        [
            NavLink(
                html.Div("Home"),
                href="/",
                active="exact",
            ),
            NavLink(
                html.Div("KPI's"),
                href="/kpis",
                active="exact",
            ),
            NavLink(
                html.Div("Top 10 Marcas Atuais"),
                href="/top-10-marcas-atuais",
                active="exact",
            ),
            NavLink(
                html.Div("Top 10 Marcas Período"),
                href="/top-10-marcas-periodo",
                active="exact",
            ),
            NavLink(
                html.Div("Preço Médio"),
                href="/preco-medio",
                active="exact",
            ),
            NavLink(
                html.Div("Faixa Preço"),
                href="/faixa-preco",
                active="exact",
            ),
            NavLink(
                html.Div("Satisfação"),
                href="/satisfacao",
                active="exact",
            ),
            NavLink(
                html.Div("Promoções"),
                href="/promocoes",
                active="exact",
            ),
        ],
        vertical=True,
        pills=True,
    )

    return conteudo


def links_documentacao() -> html.Div:
    conteudo = html.Div(
        [
            html.A(
                [
                    html.I(className="fa-solid fa-code"),
                    html.Label("Repositório"),
                ],
                href="https://github.com/Fenyx-Forte/Analise-De-Dados",
                target="_blank",
                rel="noreferrer",
            ),
            html.Br(),
            html.A(
                [
                    html.I(className="fa-solid fa-book"),
                    html.Label(
                        "Documentação",
                        className="label-documentacao",
                    ),
                ],
                href="https://github.com/Fenyx-Forte",
                target="_blank",
                rel="noreferrer",
            ),
        ],
    )

    return conteudo


def sidebar() -> html.Div:
    conteudo = html.Div(
        [
            botao_toggle(),
            html.Div(
                [
                    minhas_informacoes(),
                    html.Hr(),
                    links_paginas(),
                    html.Hr(),
                    links_documentacao(),
                ],
            ),
        ],
        id="minha-sidebar",
        className="minha-sidebar",
    )

    return conteudo


clientside_callback(
    """
    function(n_clicks) {
        if (n_clicks % 2 == 1) {
            return "minha-sidebar-escondida"
        }
        else {
            return "minha-sidebar"
        }
    }
    """,
    Output("minha-sidebar", "className"),
    Input("meu-toggle-navbar", "n_clicks"),
    prevent_initial_call=True,
)
