#!/usr/bin/python
# -*- coding: utf-8 -*-

import bpy

class MHC_OT_MarkAsHumanOperator(bpy.types.Operator):
    """Mark this object to be used as human basemesh"""
    bl_idname = "makeclothes.mark_as_human"
    bl_label = "Mark selected object as human"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return context.active_object is not None and context.active_object.type == 'MESH'

    def getMeshType(self, humanObj):
        for group in humanObj.vertex_groups:
            if group.name.startswith('_mesh_'):
                return group.name[6:]
        return "hm08"

    def execute(self, context):
        context.active_object.MhObjectType = "Basemesh"
        context.active_object.MhMeshType = self.getMeshType(context.active_object)
        self.report({'INFO'}, "Object marked as human, mesh type is " + context.active_object.MhMeshType)
        return {'FINISHED'}
