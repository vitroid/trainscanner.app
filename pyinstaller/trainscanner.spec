# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
import pkg_resources

block_cipher = None

# trainscannerのバージョンを取得
trainscanner_version = pkg_resources.get_distribution('trainscanner').version

# trainscannerパッケージの全モジュールを収集
trainscanner_hidden_imports = collect_submodules('trainscanner')

a = Analysis(
    ['run_trainscanner.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL', 'numpy', 'cv2', 'PyQt6',
        'trainscanner',
    ] + trainscanner_hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,  # バイナリを除外
    name='trainscanner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS用の.appバンドルを生成
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=True,
    upx=True,
    upx_exclude=[],
    name='trainscanner',
)

app = BUNDLE(
    coll,
    name=f'trainscanner-{trainscanner_version}-arm64.app',
    icon=None,
    bundle_identifier='com.vitroid.trainscanner',
    info_plist={
        'CFBundleShortVersionString': trainscanner_version,
        'CFBundleVersion': trainscanner_version,
        'NSHighResolutionCapable': 'True',
    },
) 