<br />
<p align="center">
  <h3 align="center">Folium-Vector</h3>

  <p align="center">
    VectorGrid plugin for Folium
    <br />
    <a href="https://github.com/iwpnd/folium-vector/issues">Report Bug</a>
    ·
    <a href="https://github.com/iwpnd/folium-vector/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This library fills a hole in foliums plugin eco-system. Wrapping [Leaflet.VectorGrid](https://github.com/Leaflet/Leaflet.VectorGrid/) into a folium plugin, users can now add vector tile layers (e.g. Mapbox, OpenMapTiles) to their folium maps.

### Built With

-   [folium](https://github.com/python-visualization/folium)
-   [Leaflet.VectorGrid](https://github.com/Leaflet/Leaflet.VectorGrid)

<!-- GETTING STARTED -->

## Getting Started

### Installation

1. Clone and install
    ```sh
    git clone https://github.com/iwpnd/folium-vector.git
    poetry install
    ```
2. Test it!
    ```sh
    poe test
    ```

## Usage

```python
from folium_vector import VectorGrid
import folium

url = "https://free-{s}.tilehosting.com/data/v3/{z}/{x}/{y}.pbf?token={token}"

m = folium.Map()
options = {
    "subdomain": "my_subdomain",
    "token": "my_token",
    "vectorTileLayerStyles": {
        "my_layer":{
            "fill": True,
            "weight": 1,
            "fillColor": 'green',
            "color": 'black',
            "fillOpacity":0.6,
            "opacity":0.6
        },
    }
}

vc = VectorGrid(url, "folium_layer_name", options)
m.add_child(vc)
m
```

Or with conditional styling

```python
import folium
from folium_vector import VectorGrid

m = folium.Map()
url = "https://free-{s}.tilehosting.com/data/v3/{z}/{x}/{y}.pbf?token={token}"

options = '''{
  "subdomain": "tilehosting",
  "token": "af6P2G9dztAt1F75x7KYt0Hx2DJR052G",
  "vectorTileLayerStyles": {
    "my_layer": function(f) {
      if (f.type === 'parks') {
        return {
          "fill": true,
          "weight": 1,
          "fillColor": 'green',
          "color": 'black',
          "fillOpacity":0.6,
          "opacity":0.6
        };
      }

      if (f.type === 'water') {
        return {
          "fill": true,
          "weight": 1,
          "fillColor": 'purple',
          "color": 'black',
          "fillOpacity":0.6,
          "opacity":0.6
        };
      }
    }
  }
}'''

VectorGrid(url,"layer_name",options).add_to(m)
m
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Benjamin Ramser - [@imwithpanda](https://twitter.com/imwithpanda) - ahoi@iwpnd.pw  
Project Link: [https://github.com/iwpnd/folium-vector](https://github.com/iwpnd/folium-vector)
