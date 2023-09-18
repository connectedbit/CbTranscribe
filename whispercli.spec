# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['whispercli.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\six-1.16.0.dist-info', 'six-1.16.0.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\tqdm', 'tqdm\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\tqdm-4.64.1.dist-info', 'tqdm-4.64.1.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\regex', 'regex\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\regex-2022.9.13.dist-info', 'regex-2022.9.13.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\requests', 'requests\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\requests-2.28.1.dist-info', 'requests-2.28.1.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\packaging', 'packaging\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\packaging-21.3.dist-info', 'packaging-21.3.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\filelock', 'filelock\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\filelock-3.8.0.dist-info', 'filelock-3.8.0.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\numpy', 'numpy\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\numpy-1.23.3.dist-info', 'numpy-1.23.3.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\tokenizers', 'tokenizers\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\tokenizers-0.12.1.dist-info', 'tokenizers-0.12.1.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\torch', 'torch\\')

    ],
    hiddenimports=['platform'],
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
    exclude_binaries=True,
    name='whispercli',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='whispercli',
)
