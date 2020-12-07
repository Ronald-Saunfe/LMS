# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks

block_cipher = None

#"C:\\Users\\CashIn\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site-packages\\reportlab\\graphics\\barcode" (hook)

a = Analysis(['main.py'],
             pathex=['E:\\Users\\cashin\\Desktop\\library_system'],
             binaries=[],
             datas=[('.','.')],
             hiddenimports=['win32timezone','pil'],
             hookspath=[],
             runtime_hooks=runtime_hooks(),
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Quora',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='pic_control\\icon.ico')

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
		*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               upx_exclude=[],
               name='main')
