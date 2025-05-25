from trainscanner.converter.gui import main
import sys
import os


def resource_path(relative_path):
    """PyInstallerでビルドされた際のリソースパスを取得するための関数"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    main()
