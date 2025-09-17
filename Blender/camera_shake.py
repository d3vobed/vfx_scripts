import bpy
import math
import random

def add_camera_shake(cam_name="Camera", strength=0.05, speed=0.5, frames=250):
    cam = bpy.data.objects.get(cam_name)
    if not cam:
        print(f"Camera '{cam_name}' not found!")
        return

    fcurve_x = cam.animation_data_create().action.fcurves.new(data_path="location", index=0)
    fcurve_y = cam.animation_data.action.fcurves.new(data_path="location", index=1)
    fcurve_z = cam.animation_data.action.fcurves.new(data_path="location", index=2)

    for f in range(frames):
        t = f * speed
        dx = math.sin(t * 0.9) * strength + random.uniform(-strength, strength) * 0.2
        dy = math.cos(t * 1.1) * strength + random.uniform(-strength, strength) * 0.2
        dz = math.sin(t * 0.7) * (strength / 2) + random.uniform(-strength, strength) * 0.1
        fcurve_x.keyframe_points.insert(f, dx)
        fcurve_y.keyframe_points.insert(f, dy)
        fcurve_z.keyframe_points.insert(f, dz)

    print("Camera shake animation added!")
# add_camera_shake("Camera", strength=0.1, speed=0.8, frames=300)
