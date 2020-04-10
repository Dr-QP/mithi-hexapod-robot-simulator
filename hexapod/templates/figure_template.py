from settings import (
    BODY_MESH_COLOR,
    BODY_MESH_OPACITY,
    BODY_COLOR,
    BODY_OUTLINE_WIDTH,
    COG_COLOR,
    COG_SIZE,
    HEAD_SIZE,
    LEG_COLOR,
    LEG_OUTLINE_WIDTH,
    SUPPORT_POLYGON_MESH_COLOR,
    SUPPORT_POLYGON_MESH_OPACITY,
    LEGENDS_BG_COLOR,
    AXIS_ZERO_LINE_COLOR,
    PAPER_BG_COLOR,
    GROUND_COLOR,
)

data = [
    {
        "name": "body mesh",
        "showlegend": True,
        "type": "mesh3d",
        "opacity": BODY_MESH_OPACITY,
        "color": BODY_MESH_COLOR,
        "uid": "1f821e07-2c02-4a64-8ce3-61ecfe2a91b6",
        "x": [100.0, 100.0, -100.0, -100.0, -100.0, 100.0, 100.0],
        "y": [0.0, 100.0, 100.0, 0.0, -100.0, -100.0, 0.0],
        "z": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    },
    {
        "line": {"color": BODY_COLOR, "opacity": 1.0, "width": BODY_OUTLINE_WIDTH},
        "name": "body",
        "showlegend": True,
        "type": "scatter3d",
        "uid": "1f821e07-2c02-4a64-8ce3-61ecfe2a91b6",
        "x": [100.0, 100.0, -100.0, -100.0, -100.0, 100.0, 100.0],
        "y": [0.0, 100.0, 100.0, 0.0, -100.0, -100.0, 0.0],
        "z": [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    },
    {
        "marker": {"color": COG_COLOR, "opacity": 1, "size": COG_SIZE},
        "mode": "markers",
        "name": "cog",
        "type": "scatter3d",
        "uid": "a819d0e4-ddaa-476b-b3e4-48fd766e749c",
        "x": [0.0],
        "y": [0.0],
        "z": [100.0],
    },
    {
        "marker": {"color": BODY_COLOR, "opacity": 1.0, "size": HEAD_SIZE},
        "mode": "markers",
        "name": "head",
        "type": "scatter3d",
        "uid": "508caa99-c538-4cb6-b022-fbbb31c2350b",
        "x": [0.0],
        "y": [100.0],
        "z": [100.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 1",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "f217db57-fe6e-4b40-90f8-4e1c20ef595e",
        "x": [100.0, 200.0, 300.0, 300.0],
        "y": [0.0, 0.0, 0.0, 0.0],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 2",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [100.0, 170.71067811865476, 241.4213562373095, 241.4213562373095],
        "y": [100.0, 170.71067811865476, 241.42135623730948, 241.42135623730948],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 3",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "9f13f416-f2b7-4eb7-993c-1e26e2e7a908",
        "x": [-100.0, -170.71067811865476, -241.42135623730948, -241.42135623730948],
        "y": [100.0, 170.71067811865476, 241.4213562373095, 241.4213562373095],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 4",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "0d426c49-19a4-4051-b938-81b30c962dff",
        "x": [-100.0, -200.0, -300.0, -300.0],
        "y": [
            0.0,
            1.2246467991473532e-14,
            2.4492935982947064e-14,
            2.4492935982947064e-14,
        ],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 5",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "5ba25594-2fb5-407e-a16f-118f12769e28",
        "x": [-100.0, -170.71067811865476, -241.42135623730954, -241.42135623730954],
        "y": [-100.0, -170.71067811865476, -241.42135623730948, -241.42135623730948],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "line": {"color": LEG_COLOR, "width": LEG_OUTLINE_WIDTH},
        "name": "leg 6",
        "showlegend": False,
        "type": "scatter3d",
        "uid": "fa4b5f98-7d68-4eb9-bd38-a6f8dabef8a4",
        "x": [100.0, 170.71067811865476, 241.42135623730948, 241.42135623730948],
        "y": [-100.0, -170.71067811865476, -241.42135623730954, -241.42135623730954],
        "z": [100.0, 100.0, 100.0, 0.0],
    },
    {
        "name": "support polygon mesh",
        "showlegend": True,
        "type": "mesh3d",
        "opacity": SUPPORT_POLYGON_MESH_OPACITY,
        "color": SUPPORT_POLYGON_MESH_COLOR,
        "uid": "1f821e07-2c02-4a64-8ce3-61ecfe2a91b6",
        "x": [
            300.0,
            241.4213562373095,
            -241.42135623730948,
            -300.0,
            -241.42135623730954,
            241.42135623730948,
        ],
        "y": [
            0.0,
            241.42135623730948,
            241.4213562373095,
            2.4492935982947064e-14,
            -241.42135623730948,
            -241.42135623730954,
        ],
        "z": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    },
    {
        "line": {"color": "#2f3640", "width": 2},
        "name": "hexapod x",
        "mode": "lines",
        "showlegend": False,
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0.0, 50.0],
        "y": [0.0, 0.0],
        "z": [100.0, 100.0],
    },
    {
        "line": {"color": "#e67e22", "width": 2},
        "name": "hexapod y",
        "mode": "lines",
        "showlegend": False,
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0.0, 0.0],
        "y": [0.0, 50.0],
        "z": [100.0, 100.0],
    },
    {
        "line": {"color": "#0097e6", "width": 2},
        "name": "hexapod z",
        "mode": "lines",
        "showlegend": False,
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0.0, 0.0],
        "y": [0.0, 0.0],
        "z": [100.0, 150.0],
    },
    {
        "line": {"color": "#2f3640", "width": 2},
        "name": "x direction",
        "showlegend": False,
        "mode": "lines",
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0, 50],
        "y": [0, 0],
        "z": [0, 0],
    },
    {
        "line": {"color": "#e67e22", "width": 2},
        "name": "y direction",
        "showlegend": False,
        "mode": "lines",
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0, 0],
        "y": [0, 50],
        "z": [0, 0],
    },
    {
        "line": {"color": "#0097e6", "width": 2},
        "name": "z direction",
        "showlegend": False,
        "mode": "lines",
        "opacity": 1.0,
        "type": "scatter3d",
        "uid": "d5690122-cd54-460d-ab3e-1f910eb88f0f",
        "x": [0, 0],
        "y": [0, 0],
        "z": [0, 50],
    },
]

HEXAPOD_FIGURE = {
    "data": data,
    "layout": {
        "paper_bgcolor": PAPER_BG_COLOR,
        "hovermode": "closest",
        "legend": {"x": 0, "y": 0, "bgcolor": LEGENDS_BG_COLOR},
        "margin": {"b": 20, "l": 10, "r": 10, "t": 20},
        "scene": {
            "aspectmode": "manual",
            "aspectratio": {"x": 1, "y": 1, "z": 1},
            "camera": {
                "center": {
                    "x": 0.0348603742736399,
                    "y": 0.16963779995083,
                    "z": -0.394903376555686,
                },
                "eye": {
                    "x": 0.193913968006015,
                    "y": 0.45997575676993,
                    "z": -0.111568465000231,
                },
                "up": {"x": 0, "y": 0, "z": 1},
            },
            "xaxis": {
                "nticks": 1,
                "range": [-600, 600],
                "zerolinecolor": AXIS_ZERO_LINE_COLOR,
                "showbackground": False,
            },
            "yaxis": {
                "nticks": 1,
                "range": [-600, 600],
                "zerolinecolor": AXIS_ZERO_LINE_COLOR,
                "showbackground": False,
            },
            "zaxis": {
                "nticks": 1,
                "range": [-600, -10],
                "zerolinecolor": AXIS_ZERO_LINE_COLOR,
                "showbackground": True,
                "backgroundcolor": GROUND_COLOR,
            },
        },
    },
}
