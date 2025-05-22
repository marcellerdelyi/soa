import bpy
import os
import sys
import csv
# -------------------------------------------------------
# 1) Clear Blender terminal
# -------------------------------------------------------

# Linux
if sys.platform.startswith('linux'):
    os.system('clear')
# Windows
elif sys.platform.startswith('win32'):
    os.system('cls')
    
# -------------------------------------------------------
# 2) Delete all object keyframes
# -------------------------------------------------------
scene = bpy.context.scene
for ob in scene.objects:
    if ob.animation_data:
        ob.animation_data_clear()
    print(f"{ob.name} has been cleared of keyframes (if any).")

# -------------------------------------------------------
# Configuration - Animation Settings
# -------------------------------------------------------

# --- File Paths ---
csvfilepath = r"C:\Users\marce\Desktop\Lego Offshore Windmill\LegoAssemblyData - Copy.csv"

list_order = False 

# Constant property
hide_z = -1000  # Hide location on Z axis

# User defined properties
spawn_z = 5      # z location where the object will drop/spawn from
hold_keyframe = 12 # pause the animation for this many frames
next_keyframe = 24 # always comes after hold keyframe

current_frame = 0    # keyframe where we start the animation on the timeline 
  
    
# -------------------------------------------------------
# 4) Read and store CSV data
# -------------------------------------------------------
rows = []
with open(csvfilepath, mode='r', newline='') as file:
    datareader = csv.reader(file)
    next(datareader)  # Skip the header
    for row in datareader:
        assembly_order = int(row[0])  # AssemblyOrder
        object_name    = row[1]       # ObjectName
        rows.append((assembly_order, object_name))
        
# -------------------------------------------------------
# 5) Animate objects in a sorted order
# -------------------------------------------------------

def animator(current_frame, list_order):
    
    if list_order:  
        # If True, reverse the existing sorted 'rows'
        iteration_sequence = reversed(rows)
    else:
        # If False, just use them as-is
        iteration_sequence = rows

    for assembly_order, object_name in iteration_sequence:

        ob = bpy.data.objects.get(object_name)

        bpy.context.view_layer.objects.active = ob
        ob.select_set(True)
        
        # Grab the current z location of the object
        obj_loc_z = bpy.context.active_object.location[2]
        
        # 1. Keyframe: hide location on the current frame
        ob.location.z += hide_z
        ob.keyframe_insert(data_path="location", frame=current_frame)
        
        # 2. Keyframe: move one keyframe and set location z on the object at spawn_z location
        current_frame += 1
        ob.location.z = obj_loc_z + spawn_z
        ob.keyframe_insert(data_path="location", frame=current_frame)
        
        # 3. Keyframe: move another amount of frames on the timeline
        current_frame += hold_keyframe
        ob.keyframe_insert(data_path="location", frame=current_frame)
        
        # 4. Keyframe: move an extra amount of keyframes and keyframe at the initial location of the object
        current_frame += next_keyframe
        ob.location.z = obj_loc_z
        ob.keyframe_insert(data_path="location", frame=current_frame)

        ob.select_set(False)
        
    return None

bpy.data.scenes["Scene"].frame_start = 0
bpy.data.scenes["Scene"].frame_end = 888

if __name__ == "__main__":
    animator(current_frame, list_order)


