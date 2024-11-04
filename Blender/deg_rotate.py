import bpy
from math import radians
import mathutils

class LaptopAnimator:
    def __init__(self):
        self.laptop = bpy.data.objects.get('Laptop')
        if not self.laptop:
            raise Exception("Laptop object not found!")
        
        self.total_frames = 240
        self.rotation_duration = 60
        
    def setup_scene(self):
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = self.total_frames
        self.laptop.animation_data_clear()
        
    def create_rotation_sequence(self):
        self.add_rotation_keyframes(0, 60, "180")
        self.add_rotation_keyframes(60, 80, "pause")
        self.add_rotation_keyframes(80, 140, "360_inverse")
        self.add_rotation_keyframes(140, 160, "pause")
        # Return back to original position
        self.add_rotation_keyframes(160, 220, "360")
        
    def add_rotation_keyframes(self, start_frame, end_frame, rotation_type):
        if rotation_type == "pause":
            return
            
        # Set initial position using euler gcd
        self.laptop.rotation_euler = (0, 0, 0)
        self.laptop.keyframe_insert(data_path="rotation_euler", frame=start_frame)
        
        # Calculate rotation
        if rotation_type == "180":
            final_rotation = (0, radians(180), 0)
        elif rotation_type == "360":
            final_rotation = (0, radians(360), 0)
        elif rotation_type == "180_inverse":
            final_rotation = (0, radians(-180), 0)
        elif rotation_type == "360_inverse":
            final_rotation = (0, radians(-360), 0)
            
        self.laptop.rotation_euler = final_rotation
        self.laptop.keyframe_insert(data_path="rotation_euler", frame=end_frame)
        
        # Add easing curve by interpolating the fucking fcurves from the rotation keyframes
        for fcurve in self.laptop.animation_data.action.fcurves:
            for kf in fcurve.keyframe_points:
                kf.interpolation = 'BEZIER'
                kf.easing = 'EASE_IN_OUT'

def main():
    animator = LaptopAnimator()
    animator.setup_scene()
    animator.create_rotation_sequence()
#please work
if __name__ == "__main__":
    main()


# Add this to the LaptopAnimator class for more control
#def add_smooth_interpolation(self): 
    # if not self.laptop.animation_data or not self.laptop.animation_data.action: 
    #     return 
    # for fcurve in self.laptop.animation_data.action.fcurves: 
    #     for kf in fcurve.keyframe_points: 
    #         kf.interpolation = 'BEZIER' 
    #         kf.handle_left_type = 'AUTO_CLAMPED' 
    #         kf.handle_right_type = 'AUTO_CLAMPED' 

#def add_bounce_effect(self, frame): 
    # bounce_angle = radians(5) 
    # bounce_frames = 10 
    # self.laptop.rotation_euler.y += bounce_angle 
    # self.laptop.keyframe_insert(data_path="rotation_euler", frame=frame) 
    # self.laptop.rotation_euler.y -= bounce_angle 
    # self.laptop.keyframe_insert(data_path="rotation_euler", frame=frame + bounce_frames) 
