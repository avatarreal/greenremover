from PIL import Image
from greenremover.core import remove_green


def test_remove_green(tmp_path):
    img = Image.new("RGB", (10, 10), (0, 255, 0))
    out = remove_green(img)
    assert out.mode == "RGBA"
    assert out.getpixel((5, 5))[3] == 0  # alpha 应该为 0
