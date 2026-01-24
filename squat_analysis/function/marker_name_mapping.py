"""
Marker name mapping dictionary for converting from expected format (with '_study' suffix)
to actual format (without '_study' suffix, lowercase).

This mapping is used to rename markers in TRC files to match the expected format
used by the gait_analysis class.

Expected format: markers end with '_study' (e.g., 'r_calc_study', 'r.ASIS_study')
Actual format: markers without '_study' suffix, lowercase (e.g., 'r_calc', 'r_ASIS')
"""

MARKER_NAME_MAPPING = {
    # Pelvis markers
    'r.ASIS_study': 'r_ASIS',
    'L.ASIS_study': 'l_ASIS',
    'r.PSIS_study': 'r_PSIS',
    'L.PSIS_study': 'l_PSIS',
    
    # Right leg markers
    'r_knee_study': 'r_knee',
    'r_mknee_study': 'r_mknee',
    'r_ankle_study': 'r_ankle',
    'r_mankle_study': 'r_mankle',
    'r_toe_study': 'r_toe',
    'r_5meta_study': 'r_5meta',
    'r_calc_study': 'r_calc',
    
    # Left leg markers
    'L_knee_study': 'l_knee',
    'L_mknee_study': 'l_mknee',
    'L_ankle_study': 'l_ankle',
    'L_mankle_study': 'l_mankle',
    'L_toe_study': 'l_toe',
    'L_calc_study': 'l_calc',
    'L_5meta_study': 'l_5meta',
    
    # Shoulder markers
    'r_shoulder_study': 'r_shoulder',
    'L_shoulder_study': 'l_shoulder',
    
    # Spine markers
    'C7_study': 'C7',
    
    # Hip joint centers
    'RHJC_study': 'RHJC',  # Check if exists in actual file
    'LHJC_study': 'LHJC',  # Check if exists in actual file
    
    # Elbow markers
    'r_melbow_study': 'r_melbow',
    'L_melbow_study': 'l_melbow',
    
}

# Reverse mapping (actual -> expected) for renaming markers in TRC files
REVERSE_MARKER_NAME_MAPPING = {v: k for k, v in MARKER_NAME_MAPPING.items()}

