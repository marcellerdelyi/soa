SOA - Sequential Object Animator

# --------------------------------------------------------------------
# Script Name: Sequential Object Animator
# Description:
#   This script animates objects in Blender sequentially based on data
#   from a CSV file. The CSV file should contain the assembly order
#   and object names.
#
# Usage:
#   1. Ensure CSV file path is correctly set.
#   2. Modify animation preferences (spawn_z, hold_keyframe, next_keyframe) 
#       in SECTION 3 if needed.
#   3. Run this script in Blender's Scripting tab.
#
# CSV File Structure:
#   - Header row is skipped.
#   - Column 1: AssemblyOrder
#   - Column 2: ObjectName 
# -------------------------------------------------------------------- 