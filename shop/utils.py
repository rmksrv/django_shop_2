from dataclasses import dataclass, asdict, field
from typing import Dict, List, Tuple

from .models import Category
from .constants import FaIconSocialNetworks


@dataclass
class BaseContext:
    header_title_left: str = "Интернет магазин"
    header_title_right: str = "Кузьминка"
    menu_categories: List[Category] = Category.objects.all()
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


def with_base_context(d: Dict) -> Dict:
    return asdict(BaseContext()) | d
