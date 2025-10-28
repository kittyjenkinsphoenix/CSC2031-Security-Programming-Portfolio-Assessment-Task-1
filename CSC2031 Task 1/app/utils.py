from typing import Optional
import bleach
from markupsafe import Markup, escape
from jinja2 import Environment, FileSystemLoader, select_autoescape

try:
except Exception:  
    bleach = None

ALLOWED_TAGS = ["b", "i", "u", "em", "strong", "a", "p", "ul", "ol", "li"]
ALLOWED_ATTRIBUTES = {"a": ["href", "title"]}
ALLOWED_PROTOCOLS = ["http", "https", "mailto"]


def sanitize_html(raw_html: Optional[str]) -> Markup:
    if not raw_html:
        return Markup("")

    if bleach is None:
        return Markup(escape(raw_html))

    cleaned = bleach.clean(
        raw_html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True,
    )

    linker = bleach.linkifier.Linker(callbacks=[bleach.callbacks.nofollow, bleach.callbacks.target_blank])
    cleaned = linker.linkify(cleaned)

    return Markup(cleaned)


def sanitize_bio(bio_text: Optional[str]) -> Markup:
    return sanitize_html(bio_text)


def create_jinja_environment(template_folder: str) -> Environment:
    loader = FileSystemLoader(template_folder)
    env = Environment(
        loader=loader,
        autoescape=select_autoescape(enabled_extensions=("html", "htm", "xml")),
    )
    return env