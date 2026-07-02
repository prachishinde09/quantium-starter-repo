import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from task3 import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods Sales Dashboard"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region = dash_duo.find_element("#region-filter")
    assert region is not None