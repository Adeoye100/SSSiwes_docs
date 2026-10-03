with open('index.html', 'r') as f:
    content = f.read()

# Fix missing script tags
content = content.replace('    // Fluid dynamics scroll interpolation', '  <script>\n    // Fluid dynamics scroll interpolation')
content = content.replace('    revealElements.forEach(el => observer.observe(el));', '    revealElements.forEach(el => observer.observe(el));\n  </script>')

# Add service worker registration
sw_script = """
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then(registration => {
          console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, err => {
          console.log('ServiceWorker registration failed: ', err);
        });
      });
    }
  </script>
"""

# Insert SW registration right before </body>
content = content.replace('</body>', sw_script + '\n</body>')

with open('index.html', 'w') as f:
    f.write(content)
print("Script fixed and SW registered.")
