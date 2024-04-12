SVG_BANNER = """
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="99" height="20">
    <linearGradient id="b" x2="0" y2="100%">
        <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
        <stop offset="1" stop-opacity=".1"/>
    </linearGradient>
    <mask id="a">
        <rect width="99" height="20" rx="3" fill="#fff"/>
    </mask>
    <g mask="url(#a)">
        <path fill="#555" d="M0 0h63v20H0z"/>
        <path fill="{color}" d="M63 0h36v20H63z"/>
        <path fill="url(#b)" d="M0 0h99v20H0z"/>
    </g>
    <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
        <text x="31.5" y="15" fill="{color}" fill-opacity=".6">coverage</text>
        <text x="31.5" y="14">coverage</text>
        <text x="80" y="15" fill="{color}" fill-opacity=".6">{count}%</text>
        <text x="80" y="14">{count}%</text>
    </g>
</svg>
"""


def svg_from_percent(count: int) -> str:
    color = "#4c1"
    if count < 80:
        color = "#9f9f9f"
    elif count < 90:
        color = "#dfb317"
    elif count < 95:
        color = "#a4a61d"
    elif count < 100:
        color = "#97CA00"

    return SVG_BANNER.format(count=count, color=color)
