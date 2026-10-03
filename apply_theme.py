import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the logo HTML
logo_old = """<div class="brand-icon-box">S</div>"""
logo_new = """<img src="assets/logo.png" alt="SANFAANI Logo" class="brand-logo-img" style="width: 32px; height: 32px; border-radius: 8px;" />"""
content = content.replace(logo_old, logo_new)

# Dark Theme Replacements
content = re.sub(r'--bg-canvas:\s*#[0-9a-fA-F]+;', '--bg-canvas: hsl(220, 18%, 9%);', content, count=1)
content = re.sub(r'--bg-surface:\s*#[0-9a-fA-F]+;', '--bg-surface: hsl(220, 17%, 13%);', content, count=1)
content = re.sub(r'--bg-surface-elevated:\s*#[0-9a-fA-F]+;', '--bg-surface-elevated: hsl(218, 15%, 16%);', content, count=1)
content = re.sub(r'--bg-surface-hover:\s*#[0-9a-fA-F]+;', '--bg-surface-hover: hsl(217, 15%, 22%);', content, count=1)
content = re.sub(r'--bg-glass:\s*rgba\([^)]+\);', '--bg-glass: hsla(220, 18%, 9%, 0.85);', content, count=1)

content = re.sub(r'--text-main:\s*#[0-9a-fA-F]+;', '--text-main: hsl(42, 35%, 93%);', content, count=1)
content = re.sub(r'--text-muted:\s*#[0-9a-fA-F]+;', '--text-muted: hsl(218, 12%, 63%);', content, count=1)
content = re.sub(r'--text-dim:\s*#[0-9a-fA-F]+;', '--text-dim: hsl(218, 12%, 50%);', content, count=1)

content = re.sub(r'--border-subtle:\s*rgba\([^)]+\);', '--border-subtle: hsl(217, 15%, 22%);', content, count=1)
content = re.sub(r'--border-medium:\s*rgba\([^)]+\);', '--border-medium: hsl(217, 15%, 32%);', content, count=1)
content = re.sub(r'--border-focus:\s*#[0-9a-fA-F]+;', '--border-focus: hsl(43, 95%, 58%);', content, count=1)

content = re.sub(r'--accent-cyan:\s*#[0-9a-fA-F]+;', '--accent-cyan: hsl(177, 52%, 32%);', content, count=1)
content = re.sub(r'--accent-cyan-subtle:\s*rgba\([^)]+\);', '--accent-cyan-subtle: hsla(177, 52%, 32%, 0.15);', content, count=1)

content = re.sub(r'--accent-emerald:\s*#[0-9a-fA-F]+;', '--accent-emerald: hsl(177, 52%, 32%);', content, count=1)
content = re.sub(r'--accent-emerald-subtle:\s*rgba\([^)]+\);', '--accent-emerald-subtle: hsla(177, 52%, 32%, 0.15);', content, count=1)

content = re.sub(r'--accent-indigo:\s*#[0-9a-fA-F]+;', '--accent-indigo: hsl(43, 95%, 58%);', content, count=1)
content = re.sub(r'--accent-indigo-subtle:\s*rgba\([^)]+\);', '--accent-indigo-subtle: hsla(43, 95%, 58%, 0.15);', content, count=1)

content = re.sub(r'--code-bg:\s*#[0-9a-fA-F]+;', '--code-bg: hsl(221, 20%, 7%);', content, count=1)

# Light Theme Replacements
content = re.sub(r'--bg-canvas:\s*#[0-9a-fA-F]+;', '--bg-canvas: hsl(42, 35%, 97%);', content, count=1) # count 1 replaces the 2nd occurrence in code? Wait no, count=1 starts from top. We need to be careful with light mode.

# Better to split by Light Theme comment
parts = content.split('/* Light Theme */')
if len(parts) == 2:
    dark_part = parts[0]
    light_part = parts[1]
    
    # Light theme specifically
    light_part = re.sub(r'--bg-canvas:\s*#[0-9a-fA-F]+;', '--bg-canvas: hsl(42, 35%, 97%);', light_part)
    light_part = re.sub(r'--bg-surface:\s*#[0-9a-fA-F]+;', '--bg-surface: hsl(0, 0%, 100%);', light_part)
    light_part = re.sub(r'--bg-surface-elevated:\s*#[0-9a-fA-F]+;', '--bg-surface-elevated: hsl(40, 20%, 93%);', light_part)
    light_part = re.sub(r'--bg-surface-hover:\s*#[0-9a-fA-F]+;', '--bg-surface-hover: hsl(220, 12%, 84%);', light_part)
    light_part = re.sub(r'--bg-glass:\s*rgba\([^)]+\);', '--bg-glass: hsla(42, 35%, 97%, 0.88);', light_part)
    
    light_part = re.sub(r'--text-main:\s*#[0-9a-fA-F]+;', '--text-main: hsl(220, 18%, 12%);', light_part)
    light_part = re.sub(r'--text-muted:\s*#[0-9a-fA-F]+;', '--text-muted: hsl(220, 10%, 42%);', light_part)
    light_part = re.sub(r'--text-dim:\s*#[0-9a-fA-F]+;', '--text-dim: hsl(220, 10%, 55%);', light_part)
    
    light_part = re.sub(r'--border-subtle:\s*#[0-9a-fA-F]+;', '--border-subtle: hsl(220, 12%, 84%);', light_part)
    light_part = re.sub(r'--border-medium:\s*#[0-9a-fA-F]+;', '--border-medium: hsl(220, 12%, 74%);', light_part)
    light_part = re.sub(r'--border-focus:\s*#[0-9a-fA-F]+;', '--border-focus: hsl(43, 95%, 48%);', light_part)
    
    light_part = re.sub(r'--accent-cyan:\s*#[0-9a-fA-F]+;', '--accent-cyan: hsl(177, 48%, 34%);', light_part)
    light_part = re.sub(r'--accent-cyan-subtle:\s*rgba\([^)]+\);', '--accent-cyan-subtle: hsla(177, 48%, 34%, 0.15);', light_part)
    
    light_part = re.sub(r'--accent-emerald:\s*#[0-9a-fA-F]+;', '--accent-emerald: hsl(177, 48%, 34%);', light_part)
    light_part = re.sub(r'--accent-emerald-subtle:\s*rgba\([^)]+\);', '--accent-emerald-subtle: hsla(177, 48%, 34%, 0.15);', light_part)
    
    light_part = re.sub(r'--accent-indigo:\s*#[0-9a-fA-F]+;', '--accent-indigo: hsl(43, 95%, 52%);', light_part)
    light_part = re.sub(r'--accent-indigo-subtle:\s*rgba\([^)]+\);', '--accent-indigo-subtle: hsla(43, 95%, 52%, 0.15);', light_part)

    light_part = re.sub(r'--code-bg:\s*#[0-9a-fA-F]+;', '--code-bg: hsl(40, 20%, 93%);', light_part)

    content = dark_part + '/* Light Theme */' + light_part

# Adjust h1 gradient based on the new theme colors
content = content.replace('background: linear-gradient(to right, #FFFFFF, #9B9B9B);', 'background: linear-gradient(to right, hsl(42, 35%, 93%), hsl(218, 12%, 63%));')
content = content.replace('background: linear-gradient(to right, #000000, #666666);', 'background: linear-gradient(to right, hsl(220, 18%, 12%), hsl(220, 10%, 42%));')

with open('index.html', 'w') as f:
    f.write(content)

print("Theme colors updated.")
