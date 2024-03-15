import bpy
import json
import os
import importlib

####记得要在插件的总__init__.py文件里添加下面几行翻译才有用
# from . import translations
# def register():
#     translations.register()
# def unregister():
#     translations.unregister()
####
#QuickMaterialColors全部替换为插件名

class TranslationHelper():
    def __init__(self, name: str, data: dict, lang='zh_CN'):
        self.name = name
        self.translations_dict = dict()

        for src, src_trans in data.items():
            key = ("Operator", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans
            key = ("*", src)
            self.translations_dict.setdefault(lang, {})[key] = src_trans

    def register(self):
        try:
            bpy.app.translations.register(self.name, self.translations_dict)
        except(ValueError):
            pass

    def unregister(self):
        bpy.app.translations.unregister(self.name)


# Set
############
from . import zh_CN#, ja_JP

QuickMaterialColors_zh_CN = TranslationHelper('QuickMaterialColors_zh_CN', zh_CN.data)
QuickMaterialColors_zh_HANS = TranslationHelper('QuickMaterialColors_zh_HANS', zh_CN.data, lang='zh_HANS')
#QuickMaterialColors_ja_JP = TranslationHelper('QuickMaterialColors_ja_JP', ja_JP.data, lang='ja_JP')


def register():
    #QuickMaterialColors_ja_JP.register()

    if bpy.app.version < (4, 0, 0):
        QuickMaterialColors_zh_CN.register()
    else:
        QuickMaterialColors_zh_CN.register()
        QuickMaterialColors_zh_HANS.register()


def unregister():
    #QuickMaterialColors_ja_JP.unregister()

    if bpy.app.version < (4, 0, 0):
        QuickMaterialColors_zh_CN.unregister()
    else:
        QuickMaterialColors_zh_CN.unregister()
        QuickMaterialColors_zh_HANS.unregister()
