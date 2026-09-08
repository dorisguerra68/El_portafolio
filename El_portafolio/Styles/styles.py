from enum import Enum


class FontFamily(Enum):
    TITLE = "'Emilys Candy','Noto Sans', cursive"
    SUBTITLE = "'Agbalumo', system-ui"
    HEADING_3 = "'Chicle', serif"


TITLE_STYLE = {
    "font_family": FontFamily.TITLE.value,
    "size": "9",
    "weight": "bold",
}


SUBTITLE_STYLE = {
    "font_family": FontFamily.SUBTITLE.value,
    "size": "7",
    "weight": "medium",
}


HEADING_3_STYLE = {
    "font_family": FontFamily.HEADING_3.value,
    "size": "5",
    "weight": "normal",
}


class Size(Enum):
    VERY_SMALL = "0.5em"
    SMALL = "1em"
    MEDIUM = "2em"
    LARGE = "3em"
    BIG = "4em"
    NAVBAR_HEIGHT = "0.8em 2.5em"
    PILL_RADIUS = "999px"
    AVATAR_SIZE = "2"
    LOGO_SIZE = "2rem"


class Color(Enum):
    TEXT_DARK = "#1e2f5d"
    TEXT_MUTED = "#4B5563"
    TEXT_LIGHT = "#f2f2f6"
    NAVBAR_BG = "#1e2f5d"
    ACCENT_GOLD = "#c29435"
    BORDER_GRAY = "#e5e7eb"
    HOVER_LIGHT = "#e5e7eb"
    HOVER_BLUE = "#234a73"
    FOOTER_BG = "#f0f3fc"
    FOOTER_ALT = "#e2e8f4"
    FOOTER_TEXT = "#1f2937"


LAYOUT_SECTION_BASE = {
    "width": "100%",
    "align_items": "start",
    "justify_content": "center",
}


NAVBAR_LINK_STYLE = {
    "color": Color.TEXT_LIGHT.value,
    "font_weight": "600",
    "padding": "0.75em 1.2em",
    "border_radius": "16px",
    "transition": "all 0.2s ease",
    "_hover": {
        "background_color": Color.HOVER_LIGHT.value,
        "color": Color.TEXT_DARK.value,
        "box_shadow": "0 4px 10px rgba(17, 24, 39, 0.08)",
    },
}


BUTTON_PRIMARY_STYLE = {
    "background_color": Color.ACCENT_GOLD.value,
    "color": Color.TEXT_LIGHT.value,
    "variant": "solid",
    "cursor": "pointer",
    "border_radius": "18px",
    "padding_x": "1.4em",
    "padding_y": "0.9em",
    "border": f"1px solid {Color.BORDER_GRAY.value}",
    "box_shadow": "0 6px 14px rgba(194, 148, 53, 0.25)",
    "transition": "all 0.2s ease",
    "_hover": {
        "background_color": Color.HOVER_BLUE.value,
        "border_color": Color.HOVER_LIGHT.value,
        "box_shadow": "0 8px 18px rgba(35, 74, 115, 0.25)",
        "transform": "translateY(-1px)",
    },
}
