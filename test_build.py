import xml.etree.ElementTree as ET
from datetime import date

from build import THEMES, parse_contributions, svg, uptime


def test_uptime():
    assert uptime(date(2022, 1, 1), date(2026, 10, 1)) == "up 4 years, 9 months"
    assert uptime(date(2022, 1, 1), date(2023, 1, 1)) == "up 1 year"
    assert uptime(date(2022, 1, 15), date(2023, 1, 14)) == "up 11 months"
    assert uptime(date(2022, 1, 1), date(2022, 1, 1)) == "up 0 months"


def test_parse_contributions():
    assert parse_contributions('<h2 class="f4">\n      1,083\n      contributions\n        in the last year\n</h2>') == 1083
    assert parse_contributions("1 contribution in the last year") == 1
    try:
        parse_contributions("<html>page changed</html>")
    except ValueError:
        pass
    else:
        raise AssertionError("a missing total must fail loudly")


def test_svg_is_valid_xml():
    for theme in THEMES:
        root = ET.fromstring(svg(theme, date(2026, 10, 1), 1083))  # fails if "&" or "<" are not escaped
        text = ET.tostring(root, encoding="unicode")
        assert "4 years, 9 months" in text and "1,083 contributions" in text


if __name__ == "__main__":
    test_uptime()
    test_parse_contributions()
    test_svg_is_valid_xml()
    print("ok")
