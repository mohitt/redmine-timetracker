# -*- mode: python -*-
a = Analysis(['.\\First.py'],
             pathex=['M:\\projects\\rm.helpmetrack'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
a.datas += [('redmine_fluid_icon.gif','redmine_fluid_icon.gif','DATA')]
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='RmHelpMeTrack.exe',
          icon='appicon.ico',
          debug=False,
          strip=None,
          upx=True,
          console=False , version='file_version_info.txt')
