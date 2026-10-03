with open('index.html', 'r') as f:
    content = f.read()

script = """
    // Fluid dynamics scroll interpolation
    const revealElements = document.querySelectorAll('.doc-section, .feature-card, .metric-card, .callout');
    
    // Set initial state
    revealElements.forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(16px)';
      el.style.filter = 'blur(4px)';
      el.style.transition = 'opacity 0.8s cubic-bezier(0.32, 0.72, 0, 1), transform 0.8s cubic-bezier(0.32, 0.72, 0, 1), filter 0.8s cubic-bezier(0.32, 0.72, 0, 1)';
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          entry.target.style.filter = 'blur(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -50px 0px' });

    revealElements.forEach(el => observer.observe(el));
"""

content = content.replace('</body>', script + '\n</body>')

with open('index.html', 'w') as f:
    f.write(content)
print("Observer added.")
