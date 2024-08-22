import dash
from dash import Input, Output, callback, dcc, html

dash.register_page(
    __name__, path="/pagina-1", name="Pagina 1", title="Pagina 1"
)


def layout(**kwargs) -> html.Div:
    content_style = {
        "marginLeft": "16rem",
        "marginRight": "2rem",
        "padding": "2rem 1rem",
    }

    conteudo = html.Div(
        [
            html.H1("This is our Analytics page"),
            html.Div(
                [
                    "Select a city: ",
                    dcc.RadioItems(
                        options=["New York City", "Montreal", "San Francisco"],
                        value="Montreal",
                        id="analytics-input",
                    ),
                ]
            ),
            html.Br(),
            html.Div(id="analytics-output"),
        ],
        style=content_style,
    )
    return conteudo


@callback(
    Output("analytics-output", "children"), Input("analytics-input", "value")
)
def update_city_selected(input_value):
    return f"You selected: {input_value}"
