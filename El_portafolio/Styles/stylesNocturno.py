import reflex as rx


class ThemeState(rx.State):
    night_mode: bool = False

    @rx.event
    def toggle_theme(self):
        self.night_mode = not self.night_mode


THEME_COLORS = {
    "--portfolio-text-dark": ("#1e2f5d", "#e5e7eb"),
    "--portfolio-text-muted": ("#4b5563", "#cbd5e1"),
    "--portfolio-text-light": ("#f2f2f6", "#f8fafc"),
    "--portfolio-navbar-bg": ("#1e2f5d", "#111827"),
    "--portfolio-accent-gold": ("#c29435", "#e0b84f"),
    "--portfolio-border": ("#e5e7eb", "#374151"),
    "--portfolio-hover-light": ("#e5e7eb", "#374151"),
    "--portfolio-hover-blue": ("#234a73", "#334155"),
    "--portfolio-footer-bg": ("#f0f3fc", "#1f2937"),
    "--portfolio-footer-alt": ("#e2e8f4", "#374151"),
    "--portfolio-footer-text": ("#1f2937", "#e5e7eb"),
    "--portfolio-page-background": (
        "linear-gradient(135deg, rgba(250,250,255,1) 0%, "
        "rgba(240,243,252,1) 100%)",
        "linear-gradient(135deg, #111827 0%, #1f2937 100%)",
    ),
    "--portfolio-card-background": ("#ffffff", "#273449"),
    "--portfolio-input-background": ("#ffffff", "#1f2937"),
    "--portfolio-input-border": (
        "rgba(30, 47, 93, 0.18)",
        "rgba(203, 213, 225, 0.28)",
    ),
    "--portfolio-placeholder": ("#6b7280", "#9ca3af"),
    "--portfolio-navbar-shell": (
        "rgba(30, 47, 93, 0.96)",
        "rgba(17, 24, 39, 0.96)",
    ),
    "--portfolio-hero-mobile-overlay": (
        "linear-gradient(to bottom, rgba(250,250,255,0.02) 22%, "
        "rgba(250,250,255,0.35) 48%, rgba(250,250,255,0.98) 76%)",
        "linear-gradient(to bottom, rgba(17,24,39,0.08) 22%, "
        "rgba(17,24,39,0.5) 48%, rgba(17,24,39,0.98) 76%)",
    ),
    "--portfolio-hero-desktop-overlay": (
        "linear-gradient(to bottom, transparent, transparent)",
        "linear-gradient(to bottom, rgba(17,24,39,0.22), "
        "rgba(17,24,39,0.68))",
    ),
    "--portfolio-warning-text": ("#92400e", "#fcd34d"),
    "--portfolio-warning-bg": ("#fffbeb", "#422006"),
    "--portfolio-error-text": ("#b91c1c", "#fca5a5"),
    "--portfolio-error-bg": ("#fef2f2", "#450a0a"),
    "--portfolio-success-text": ("#0f766e", "#6ee7b7"),
    "--portfolio-success-bg": ("#ecfdf5", "#064e3b"),
}


def themed_page(content: rx.Component) -> rx.Component:
    theme_style = {
        variable: rx.cond(ThemeState.night_mode, night, day)
        for variable, (day, night) in THEME_COLORS.items()
    }
    return rx.box(
        content,
        style=theme_style,
        width="100%",
        min_height="100vh",
    )
