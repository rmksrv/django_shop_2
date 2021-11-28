from dataclasses import dataclass
from django.conf import settings


@dataclass
class ExternalPage:
    name: str
    fa_icon: str
    link: str


PRODUCT_IMAGE_LOCATION = "products/%Y/%m/%d"
CATEGORIES_IMAGE_LOCATION = "categories"
NO_IMAGE_PATH = settings.BASE_DIR / "static" / "images" / "no_image.png"
NO_IMAGE_URL = settings.STATIC_URL + "images/no_image.png"

EXTERNAL_PAGES_DATA = [
    ExternalPage(name="VK", fa_icon="fa-vk", link=r"https://vk.com/"),
    ExternalPage(name="Facebook", fa_icon="fa-facebook", link=r"https://www.facebook.com/"),
    ExternalPage(name="Instagram", fa_icon="fa-instagram", link=r"https://www.instagram.com/"),
    ExternalPage(name="YouTube", fa_icon="fa-youtube", link=r"https://www.youtube.com/"),
    ExternalPage(name="YouTube", fa_icon="fa-twitter", link=r"https://twitter.com/"),
]
