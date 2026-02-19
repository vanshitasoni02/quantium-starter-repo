import app

def test_header_present():
    layout = app.app.layout
    # Check that the title text exists somewhere in layout
    layout_str = str(layout)
    assert "Pink Morsel" in layout_str

def test_graph_present():
    layout = app.app.layout
    layout_str = str(layout)
    # Check that the graph id is present
    assert "sales-graph" in layout_str

def test_region_picker_present():
    layout = app.app.layout
    layout_str = str(layout)
    # Check that the radio button id is present
    assert "region-radio" in layout_str
