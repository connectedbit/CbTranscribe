# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

whisper_datas = collect_data_files('whisper')
whisper_hidden = collect_submodules('whisper')

a = Analysis(
    ['whispercli.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\six-1.17.0.dist-info', 'six-1.17.0.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\tqdm', 'tqdm\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\tqdm-4.68.3.dist-info', 'tqdm-4.68.3.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\regex', 'regex\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\regex-2026.6.28.dist-info', 'regex-2026.6.28.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\requests', 'requests\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\requests-2.34.2.dist-info', 'requests-2.34.2.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\packaging', 'packaging\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\packaging-26.2.dist-info', 'packaging-26.2.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\filelock', 'filelock\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\filelock-3.29.6.dist-info', 'filelock-3.29.6.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\numpy', 'numpy\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\numpy-2.3.4.dist-info', 'numpy-2.3.4.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\tokenizers', 'tokenizers\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\tokenizers-0.23.1.dist-info', 'tokenizers-0.23.1.dist-info\\'),
        ('C:\\Users\\Ronald\\AppData\\Roaming\\Python\\Python313\\site-packages\\torch', 'torch\\'),
    ] + whisper_datas,
    hiddenimports=['platform'] + whisper_hidden,
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