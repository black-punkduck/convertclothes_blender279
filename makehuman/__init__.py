#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Authors: Joel Palmius
#           black-punkduck

from bpy.utils import register_class, unregister_class
from .extraproperties import extraProperties
from .makeclothes2 import MHC_PT_MakeClothesPanel
from .maketarget2 import MHC_PT_MakeTarget_Panel
from .infobox import MHC_OT_InfoBox,MHC_WarningBox
from .operators import *
from .t_operators import *

bl_info = {
    "name": "ConvertClothes",
    "author": "Joel Palmius, black-punkduck",
    "version": (2,1,0),
    "blender": (2,79,0),
    "location": "View3D > Properties > Make Target",
    "description": "Create Meshes to be used as clothes and proxies in Makehuman",
    'wiki_url': "http://www.makehumancommunity.org/",
    "category": "MakeHuman"}


MAKECLOTHES2_CLASSES = []
MAKECLOTHES2_CLASSES.extend(OPERATOR_CLASSES)
MAKECLOTHES2_CLASSES.append(MHC_PT_MakeClothesPanel)
MAKECLOTHES2_CLASSES.append(MHC_OT_InfoBox)
MAKECLOTHES2_CLASSES.append(MHC_WarningBox)

MAKETARGET2_CLASSES = []
MAKECLOTHES2_CLASSES.extend(T_OPERATOR_CLASSES)
MAKECLOTHES2_CLASSES.append(MHC_PT_MakeTarget_Panel)

__all__ = [
    "MHC_PT_MakeClothesPanel",
    "MHC_OT_InfoBox",
    "MHC_WarningBox",
    "MAKECLOTHES2_CLASSES",
    "MHC_PT_MakeTarget_Panel",
    "MAKETARGET2_CLASSES",
]

def register():
    extraProperties()
    for cls in MAKECLOTHES2_CLASSES:
        register_class(cls)
    for cls in MAKETARGET2_CLASSES:
        register_class(cls)

def unregister():
    for cls in reversed(MAKECLOTHES2_CLASSES):
        unregister_class(cls)
    for cls in reversed(MAKETARGET2_CLASSES):
        unregister_class(cls)

if __name__ == "__main__":
    register()
    print("MakeClothes2 loaded")

