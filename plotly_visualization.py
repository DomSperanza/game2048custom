import plotly.graph_objects as go
import numpy as np

def plot_board(board):
    size = board.shape[0]
    colors = {
        0: 'white',
        2: 'beige',
        4: 'lightgoldenrodyellow',
        8: 'khaki',
        16: 'darkkhaki',
        32: 'lemonchiffon',
        64: 'gold',
        128: 'orange',
        256: 'darkorange',
        512: 'orangered',
        1024: 'tomato',
        2048: 'red'
    }

    fig = go.Figure()

    for i in range(size):
        for j in range(size):
            fig.add_shape(
                type='rect',
                xref='x',
                yref='y',
                x0=j,
                y0=i,
                x1=j + 1,
                y1=i + 1,
                line=dict(color='black'),
                fillcolor=colors[board[i, j]]
            )
            if board[i, j] != 0:
                fig.add_annotation(
                    x=j + 0.5,
                    y=i + 0.5,
                    text=str(board[i, j]),
                    showarrow=False,
                    font=dict(size=16)
                )

    fig.update_layout(
        title='2048 Game',
        xaxis=dict(range=[0, size], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, size], showgrid=False, zeroline=False),
        width=400, height=400,
        margin=dict(l=50, r=50, b=50, t=50),
        paper_bgcolor='white',
        plot_bgcolor='white'
    )
    fig.update_yaxes(scaleanchor='x', scaleratio=1)
    return fig
