import argparse
from pathlib import Path
from PIL import Image
from greenremover.core import remove_green


def main():
    parser = argparse.ArgumentParser(description="去除图片中的绿色背景")
    parser.add_argument("input", help="输入图片路径")
    parser.add_argument("output", help="输出图片路径 (自动保存为 PNG 支持透明通道)")

    args = parser.parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    img = Image.open(input_path)
    out = remove_green(img)
    out.save(output_path, "PNG")


if __name__ == "__main__":
    main()
