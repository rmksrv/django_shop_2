from dataclasses import asdict, dataclass, field
from typing import Dict, List

from django.utils import lorem_ipsum

from .constants import NO_IMAGE_URL, ExternalPage, EXTERNAL_PAGES_DATA
from .models import Category


@dataclass
class BaseContext:
    page_title: str = "Главная"
    header_title_left: str = "Интернет магазин"
    header_title_right: str = "Кузьминка"
    menu_categories: List[Category] = Category.objects.all()
    footer_external_pages: List[ExternalPage] = field(default_factory=lambda: EXTERNAL_PAGES_DATA)
    footer_copyright_label: str = "Интернет магазин Кузьминка"
    footer_site_made_by_label: str = "Roman Kosarev"
    footer_site_made_by_href: str = r"https://github.com/rmksrv"
    banner_image_url: str = NO_IMAGE_URL
    banner_header_text: str = "Интернет магазин Кузьминка"
    banner_content_html_text: str = lorem_ipsum.sentence()
    banner_with_button: bool = True
    banner_with_csrf: bool = True
    banner_button_text: str = "Перейти"
    banner_button_href: str = r"#main_section"
    banner_button_request_method: str = "get"
    cart_length: int = 0

    def concat_with(self, d: Dict) -> Dict:
        return asdict(self) | d
