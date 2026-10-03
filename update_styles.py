import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fonts
content = re.sub(
    r'<link href="https://fonts.googleapis.com/css2\?family=Inter[^"]+" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">',
    content
)
content = content.replace(
    "--font-sans: 'Inter', -apple-system",
    "--font-sans: 'Manrope', -apple-system"
)

# 2. Dark Mode Backgrounds
content = content.replace('--bg-canvas: #090d16;', '--bg-canvas: #131209;')
content = content.replace('--bg-surface: #0f172a;', '--bg-surface: #181818;')
content = content.replace('--bg-surface-elevated: #162036;', '--bg-surface-elevated: #1F1F1F;')
content = content.replace('--bg-surface-hover: #1e293b;', '--bg-surface-hover: #272727;')
content = content.replace('--bg-glass: rgba(15, 23, 42, 0.85);', '--bg-glass: rgba(19, 18, 9, 0.85);')
content = content.replace('--code-bg: #0b0f19;', '--code-bg: #000000;')

# 3. Text wrap for headings and body
content = content.replace('p {\n      color: var(--text-muted);', 'p {\n      color: var(--text-muted);\n      text-wrap: pretty;')
content = content.replace('.doc-h1 {\n      font-size: 2.25rem;', '.doc-h1 {\n      font-size: 2.25rem;\n      text-wrap: balance;')
content = content.replace('.doc-h2 {\n      font-size: 1.625rem;', '.doc-h2 {\n      font-size: 1.625rem;\n      text-wrap: balance;')

# 4. Transitions
content = re.sub(
    r'transition:\s*[^;]+;',
    'transition: all 0.7s cubic-bezier(0.32, 0.72, 0, 1);',
    content
)

# 5. Gradient on H1 (Hero Heading)
# I will find the doc-h1 rule and add the background clip
h1_css = """
    .doc-h1 {
      font-size: 2.25rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.2;
      margin-bottom: 1rem;
      background: linear-gradient(to right, #FFFFFF, #9B9B9B);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      color: transparent;
      text-wrap: balance;
    }
    :root[data-theme="light"] .doc-h1 {
      background: linear-gradient(to right, #000000, #666666);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      color: transparent;
    }
"""
content = re.sub(r'\.doc-h1\s*\{[^}]+\}', h1_css.strip(), content)

# 6. Type scale
# Replace custom rem font sizes with Tailwind scale snaps
# text-base: 1rem (16px), text-lg: 1.125rem (18px), text-xl: 1.25rem (20px), text-2xl: 1.5rem (24px)
content = content.replace('font-size: 15px;', 'font-size: 16px;') # base font size
content = content.replace('font-size: 0.8125rem;', 'font-size: 0.875rem;') # text-sm
content = content.replace('font-size: 0.875rem;', 'font-size: 0.875rem;') # text-sm
content = content.replace('font-size: 0.9375rem;', 'font-size: 1rem;') # text-base
content = content.replace('font-size: 1.0625rem;', 'font-size: 1.125rem;') # text-lg
content = content.replace('font-size: 1.1875rem;', 'font-size: 1.25rem;') # text-xl
content = content.replace('font-size: 1.625rem;', 'font-size: 1.5rem;') # text-2xl
content = content.replace('font-size: 2.25rem;', 'font-size: 2.25rem;') # text-4xl

# 7. No gradients in backgrounds (except hero text, and brand-icon-box gradient must be kept because user said "leave the icon")
# Checked: brand-icon-box has linear-gradient, which is the icon.

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
