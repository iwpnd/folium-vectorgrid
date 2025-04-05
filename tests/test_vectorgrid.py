"""
Test VectorGridProtobuf
---------------
"""

import json
from typing import Any

import folium
from folium.utilities import normalize

from folium_vectorgrid import VectorGridProtobuf


def test_vectorgrid() -> None:
    m = folium.Map(location=(30, 20), zoom_start=4)
    url = "https://free-{s}.tilehosting.com/data/v3/{z}/{x}/{y}.pbf?token={token}"
    vc = VectorGridProtobuf(url, "test").add_to(m)
    out = normalize(m._parent.render())

    expected = normalize(VectorGridProtobuf._template.render(this=vc))
    assert expected in out

    script = f'<script src="{VectorGridProtobuf.default_js[0][1]}"></script>'
    assert script in out
    assert url in out
    assert "L.vectorGrid.protobuf" in out


def test_vectorgrid_str_options() -> None:
    m = folium.Map(location=(30, 20), zoom_start=4)
    url = "https://free-{s}.tilehosting.com/data/v3/{z}/{x}/{y}.pbf?token={token}"
    options = """{
        "subdomain": "test",
        "token": "test_token",
        "vectorTileLayerStyles": {
            "all": {
                "fill": true,
                "weight": 1,
                "fillColor": "green",
                "color": "black",
                "fillOpacity": 0.6,
                "opacity": 0.6
                }
            }
        }"""

    vc = VectorGridProtobuf(url, "test", options)
    m.add_child(vc)

    dict_options = json.loads(options)

    out = normalize(m._parent.render())
    script = f'<script src="{VectorGridProtobuf.default_js[0][1]}"></script>'

    assert script in out
    assert url in out
    assert "L.vectorGrid.protobuf" in out
    assert '"token": "test_token"' in out
    assert '"subdomain": "test"' in out

    for k, v in dict_options["vectorTileLayerStyles"]["all"].items():
        if isinstance(v, bool):
            assert f'"{k}": {str(v).lower()}' in out
            continue
        if isinstance(v, str):
            assert f'"{k}": "{v}"' in out
            continue

        assert f'"{k}": {v}' in out


def test_vectorgrid_dict_options() -> None:
    m = folium.Map(location=(30, 20), zoom_start=4)
    url = "https://free-{s}.tilehosting.com/data/v3/{z}/{x}/{y}.pbf?token={token}"
    options: dict[str, Any] = {
        "subdomain": "test",
        "token": "test_token",
        "vectorTileLayerStyles": {
            "all": {
                "fill": True,
                "weight": 1,
                "fillColor": "grey",
                "color": "purple",
                "fillOpacity": 0.3,
                "opacity": 0.6,
            }
        },
    }

    vc = VectorGridProtobuf(url, "test", options)
    m.add_child(vc)

    out = normalize(m._parent.render())
    script = f'<script src="{VectorGridProtobuf.default_js[0][1]}"></script>'

    assert script in out
    assert url in out
    assert "L.vectorGrid.protobuf" in out
    assert '"token": "test_token"' in out
    assert '"subdomain": "test"' in out

    for k, v in options["vectorTileLayerStyles"]["all"].items():
        if isinstance(v, bool):
            assert f'"{k}": {str(v).lower()}' in out
            continue
        if isinstance(v, str):
            assert f'"{k}": "{v}"' in out
            continue

        assert f'"{k}": {v}' in out
