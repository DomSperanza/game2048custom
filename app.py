import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State
from game_logic import initialize_game, slide_board, is_game_over
from plotly_visualization import plot_board
import numpy as np

def create_app():
    app = dash.Dash(__name__)
    initial_board = initialize_game()

    app.layout = html.Div([
        html.H1("2048 Game"),
        dcc.Dropdown(
            id='board-size-dropdown',
            options=[{'label': f'{i}x{i}', 'value': i} for i in [3, 4, 5, 6, 7, 8]],
            value=4,
            style={'width': '50%'}
        ),
        dcc.Graph(id='game-board', figure=plot_board(initial_board)),
        dcc.Store(id='game-board-state', data=initial_board.tolist()), # Hidden component to store the board state
        html.Div([
            html.Button('Left', id='button-left', n_clicks=0),
            html.Button('Right', id='button-right', n_clicks=0),
            html.Button('Up', id='button-up', n_clicks=0),
            html.Button('Down', id='button-down', n_clicks=0),
            html.Button('Restart', id='button-restart', n_clicks=0),
        ]),
        html.Div(id='game-over-text'),
    ])

    @app.callback(
        [Output('game-board', 'figure'),
         Output('game-over-text', 'children'),
         Output('game-board-state', 'data')],
        [Input('button-left', 'n_clicks'),
         Input('button-right', 'n_clicks'),
         Input('button-up', 'n_clicks'),
         Input('button-down', 'n_clicks'),
         Input('button-restart', 'n_clicks'),
         Input('board-size-dropdown', 'value')],
        [State('game-board-state', 'data')])
    def update_game(n_left, n_right, n_up, n_down, n_restart, board_size, current_board_data):
        ctx = dash.callback_context
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'button-restart':
            new_board = initialize_game(board_size)
        else:
            new_board = np.array(current_board_data)
            if button_id == 'button-left':
                slide_board(new_board, 'left')
            elif button_id == 'button-right':
                slide_board(new_board, 'right')
            elif button_id == 'button-up':
                slide_board(new_board, 'up')
            elif button_id == 'button-down':
                slide_board(new_board, 'down')

        game_over_text = "Game Over!" if is_game_over(new_board) else ""
        return plot_board(new_board), game_over_text, new_board.tolist()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run_server(debug=True)