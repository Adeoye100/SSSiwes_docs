import re

with open('index.html', 'r') as f:
    content = f.read()

parts = content.split('/* Light Theme */')
if len(parts) == 2:
    dark_part, light_part = parts

    # Dark Theme
    dark_part = re.sub(r'--accent-amber:\s*#[0-9a-fA-F]+;', '--accent-amber: hsl(27, 86%, 62%);', dark_part)
    dark_part = re.sub(r'--accent-amber-subtle:\s*rgba\([^)]+\);', '--accent-amber-subtle: hsla(27, 86%, 62%, 0.15);', dark_part)
    dark_part = re.sub(r'--accent-rose:\s*#[0-9a-fA-F]+;', '--accent-rose: hsl(3, 71%, 55%);', dark_part)
    dark_part = re.sub(r'--accent-rose-subtle:\s*rgba\([^)]+\);', '--accent-rose-subtle: hsla(3, 71%, 55%, 0.15);', dark_part)

    # Light Theme
    light_part = re.sub(r'--accent-amber:\s*#[0-9a-fA-F]+;', '--accent-amber: hsl(27, 86%, 55%);', light_part)
    light_part = re.sub(r'--accent-amber-subtle:\s*rgba\([^)]+\);', '--accent-amber-subtle: hsla(27, 86%, 55%, 0.15);', light_part)
    light_part = re.sub(r'--accent-rose:\s*#[0-9a-fA-F]+;', '--accent-rose: hsl(3, 71%, 48%);', light_part)
    light_part = re.sub(r'--accent-rose-subtle:\s*rgba\([^)]+\);', '--accent-rose-subtle: hsla(3, 71%, 48%, 0.15);', light_part)

    content = dark_part + '/* Light Theme */' + light_part

with open('index.html', 'w') as f:
    f.write(content)

print("Amber and Rose colors fixed.")
