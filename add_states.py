import re

with open('index.html', 'r') as f:
    content = f.read()

# Add focus and active states
states_css = """
    /* Interactive States (from Design System) */
    a:focus-visible, button:focus-visible, input:focus-visible, .nav-item-link:focus-visible {
      outline: 2px solid var(--accent-cyan);
      outline-offset: 2px;
    }
    
    a:active, button:active, .nav-item-link:active, .toc-action-btn:active {
      transform: scale(0.98);
    }
    
    .feature-card:active {
      transform: scale(0.98);
    }
"""
content = content.replace('</style>', states_css + '\n  </style>')

with open('index.html', 'w') as f:
    f.write(content)
print("States added.")
