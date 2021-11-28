from dataclasses import asdict, dataclass, field
from typing import Dict, List, Tuple

from django.utils import lorem_ipsum

from .constants import FaIconSocialNetworks, NO_IMAGE_URL
from .models import Category


@dataclass
class BaseContext:
    page_title: str = "Главная"
    header_title_left: str = "Интернет магазин"
    header_title_right: str = "Кузьминка"
    menu_categories: List[Category] = Category.objects.all()
    # TODO: incapsulate links to FaIconSocialNetworks
    footer_social_networks_refs: List[Tuple[FaIconSocialNetworks, str]] = field(
        default_factory=lambda: [
            (FaIconSocialNetworks.VK.value, r"https://vk.com/"),
            (FaIconSocialNetworks.Facebook.value, r"https://www.facebook.com/"),
            (FaIconSocialNetworks.Instagram.value, r"https://www.instagram.com/"),
            (FaIconSocialNetworks.Twitter.value, r"https://twitter.com/"),
            (FaIconSocialNetworks.YouTube.value, r"https://www.youtube.com/"),
        ]
    )
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
