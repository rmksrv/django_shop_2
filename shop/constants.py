from enum import Enum

from django.conf import settings

PRODUCT_IMAGE_LOCATION = "products/%Y/%m/%d"
CATEGORIES_IMAGE_LOCATION = "categories"
NO_IMAGE_PATH = settings.BASE_DIR / "static" / "images" / "no_image.png"
NO_IMAGE_URL = settings.STATIC_URL + "images/no_image.png"


class FaIconSocialNetworks(Enum):
    VK = "fa-vk"
    Facebook = "fa-facebook-f"
    Instagram = "fa-instagram"
    Twitter = "fa-twitter"
    YouTube = "fa-youtube"
