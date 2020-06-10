#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Author: Joel Palmius

from .createprimarytarget import MHC_OT_CreatePrimaryTargetOperator
from .printprimarytarget import MHC_OT_PrintPrimaryTargetOperator
from .saveprimarytarget import MHC_OT_SavePrimaryTargetOperator
from .loadprimarytarget import MHC_OT_LoadPrimaryTargetOperator
from .symmetrizeleft import MHC_OT_SymmetrizeLeftOperator
from .symmetrizeright import MHC_OT_SymmetrizeRightOperator

T_OPERATOR_CLASSES = [
    MHC_OT_CreatePrimaryTargetOperator,
    MHC_OT_PrintPrimaryTargetOperator,
    MHC_OT_SavePrimaryTargetOperator,
    MHC_OT_LoadPrimaryTargetOperator,
    MHC_OT_SymmetrizeLeftOperator,
    MHC_OT_SymmetrizeRightOperator
]

__all__ = [
    "MHC_OT_CreatePrimaryTargetOperator",
    "MHC_OT_PrintPrimaryTargetOperator",
    "MHC_OT_SavePrimaryTargetOperator",
    "MHC_OT_LoadPrimaryTargetOperator",
    "MHC_OT_SymmetrizeLeftOperator",
    "MHC_OT_SymmetrizeRightOperator",
    "T_OPERATOR_CLASSES"
]
