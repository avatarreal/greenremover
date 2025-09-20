from PIL import Image
import numpy as np


def remove_green(img: Image.Image) -> Image.Image:
    """去除图像绿幕 (RGB → RGBA)"""
    rgba = img.convert("RGBA")
    data = np.array(rgba)

    r = data[..., 0].astype(np.float32)
    g = data[..., 1].astype(np.float32)
    b = data[..., 2].astype(np.float32)
    a = data[..., 3].astype(np.float32)

    # 条件1：强绿 → 直接透明
    strong_green = g - 150 > (r + b)
    a[strong_green] = 0

    # 条件2：偏绿 → 调整颜色 & alpha
    weak_green = ((g * 2) > (r + b)) & (~strong_green)
    adjustment = (g - (r + b) / 2) / 3
    adjustment = np.clip(adjustment, 0, 255)

    r[weak_green] += adjustment[weak_green]
    g[weak_green] -= adjustment[weak_green] * 2
    b[weak_green] += adjustment[weak_green]
    a[weak_green] = np.maximum(0, 255 - adjustment[weak_green] * 4)

    # 合并结果
    out = np.dstack(
        [
            np.clip(r, 0, 255).astype(np.uint8),
            np.clip(g, 0, 255).astype(np.uint8),
            np.clip(b, 0, 255).astype(np.uint8),
            np.clip(a, 0, 255).astype(np.uint8),
        ]
    )
    return Image.fromarray(out).convert("RGBA")
