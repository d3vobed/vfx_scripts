import bpy

def batch_parent_and_apply_mod(parent_name="Parent_Empty", modifier_type="SUBSURF"):
    sel = bpy.context.selected_objects
    if not sel:
        print("No objects selected")
        return
    bpy.ops.object.empty_add(type="PLAIN_AXES")
    parent = bpy.context.active_object
    parent.name = parent_name

    # parent selected (excluding the empty) to this new empty
    for obj in sel:
        if obj == parent:
            continue
        obj.parent = parent

    for obj in sel:
        if obj == parent:
            continue
        mod = obj.modifiers.new(name=f"{modifier_type}_mod", type=modifier_type)
        if modifier_type == "SUBSURF":
            mod.levels = 2
            mod.render_levels = 2
        elif modifier_type == "BEVEL":
            mod.width = 0.1
            mod.segments = 3

    print(f"Parent '{parent.name}' created, modifiers applied.")

if __name__ == "__main__":
    # Example
    batch_parent_and_apply_mod(parent_name="MyGroup", modifier_type="BEVEL")
