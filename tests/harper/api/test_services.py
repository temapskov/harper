import pytest

from actions_helper.coverage.api.v1.info.service import SVG_BANNER, svg_from_percent


@pytest.mark.parametrize(
    "percent, color",
    [
        (99, "#97CA00"),
        (94, "#a4a61d"),
        (89, "#dfb317"),
        (79, "#9f9f9f"),
        (100, "#4c1"),
    ],
)
def test_color_from_percent(percent: int, color: str):
    svg = svg_from_percent(percent)

    assert color in svg


@pytest.mark.parametrize(
    "percent",
    [100, 99, 94, 89, 79],
)
def test_svg_is_formated(percent: int):
    new_svg = svg_from_percent(percent)

    assert new_svg != SVG_BANNER
