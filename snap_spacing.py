import re

with open('index.html', 'r') as f:
    content = f.read()

# Define allowed spacing in rems (based on 16px base)
# 0, 0.125 (2), 0.25 (4), 0.5 (8), 0.75 (12), 1 (16), 1.5 (24), 2 (32), 2.5 (40), 3 (48), 4 (64), 5 (80), 6 (96)
allowed_rem = [0, 0.125, 0.25, 0.5, 0.75, 1, 1.5, 2, 2.5, 3, 4, 5, 6]

def snap_rem_val(match):
    val_str = match.group(1)
    try:
        val = float(val_str)
        # Find closest allowed value below or equal
        valid_vals = [v for v in allowed_rem if v <= val]
        snapped = valid_vals[-1] if valid_vals else 0
        
        # Formatting to remove .0 if it's an integer
        if snapped == int(snapped):
            snapped = int(snapped)
            
        if snapped == 0:
            return "0"
        return f"{snapped}rem"
    except:
        return match.group(0)

def snap_property(match):
    prop = match.group(1)
    values_str = match.group(2)
    # Match any rem value like 1.5rem, .5rem, 0.5rem
    snapped_values = re.sub(r'(\d*\.?\d+)rem', snap_rem_val, values_str)
    return f"{prop}:{snapped_values}"

# Replace properties in the CSS block only, or everywhere if we are careful
# Only target specific properties
props = r"(margin|padding|margin-top|margin-bottom|margin-left|margin-right|padding-top|padding-bottom|padding-left|padding-right|gap|top|bottom|left|right)"
content = re.sub(props + r'\s*:\s*([^;]+)', snap_property, content)

with open('index.html', 'w') as f:
    f.write(content)
print("Spacing snapped.")
