import bpy
from bpy.types import Panel

class SCV_PT_panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Shortcut VUr"
    bl_category = "Shortcut VUr"
    
    def draw(self, context):
        
        layout = self.layout
        scene = context.scene
                          
        row = layout.row()
        
        if(context.window_manager.SCV_started):
            row.operator('object.scv_ot_draw_operator', text="Stop Shortcut VUr", icon="CANCEL")
        else:
            row.operator('object.scv_ot_draw_operator', text="Start Shortcut VUr", icon="PLAY")