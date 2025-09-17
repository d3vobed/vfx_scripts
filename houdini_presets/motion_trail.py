import hou

def create_motion_trail(obj_path):
    obj = hou.node(obj_path)
    if not obj:
        hou.ui.displayMessage(f"Object {obj_path} not found.")
        return
        geo = obj.parent().createNode("geo", "motion_trail")
    geo.moveToGoodPosition()

    # Add trail SOP to geometry node
    file_sop = geo.createNode("object_merge", "import_obj")
    file_sop.parm("objpath1").set(obj_path)

    trail = geo.createNode("trail", "motion")
    trail.setInput(0, file_sop)
    trail.parm("resulttype").set(1)  # Compute velocity against the file_sop over 0++
    trail.parm("trailsteps").set(1)

    add_trail = geo.createNode("add", "connect_trail")
    add_trail.setInput(0, trail)
    add_trail.parm("addpts").set(True)

    add_trail.setDisplayFlag(True)
    add_trail.setRenderFlag(True)

    geo.layoutChildren()
    hou.ui.displayMessage("Motion trail created!")


