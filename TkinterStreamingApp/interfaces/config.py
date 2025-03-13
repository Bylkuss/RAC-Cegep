# interfaces/config.py
from PIL import Image, ImageTk, ImageDraw
import tkinter as tk

# Global style configuration
STYLE_CONFIG = {
    'primary_color': '#6a0dad',  # Purple
    'secondary_color': '#00FFFF',  # Neon Cyan
    'background_color': '#1E1E1E',  # Dark Gray
    'button_color': '#8A2BE2',  # Electric Purple
    'font': ('Poppins', 12),
    'font_bold': ('Poppins', 14, 'bold'),
    'button_radius': 12,
    'hover_effect': {
        'bg_color': '#00FFFF',  # Neon Cyan on hover
        'fg_color': '#1E1E1E',  # Dark Gray text on hover
    },
    'glassmorphism': {
        'bg_color': '#1E1E1E',  # Hex with alpha (B3 = 70% opacity)
        'blur_radius': 10,
    },
    'input_field': {
        'bg': '#2E2E2E',
        'fg': 'white',
        'highlightcolor': '#00FFFF',
        'insertbackground': 'white',
        'relief': 'flat',
        'borderwidth': 1
    },
}

def apply_button_style(button, text, width=12, height=1):
    """Apply a consistent button style to all buttons."""
    button.config(
        text=text,
        width=width,
        height=height,
        bg=STYLE_CONFIG['button_color'],
        fg='white',
        font=STYLE_CONFIG['font_bold'],
        relief='flat',
        bd=0,
        highlightthickness=0,
        activebackground=STYLE_CONFIG['hover_effect']['bg_color'],
        activeforeground=STYLE_CONFIG['hover_effect']['fg_color'],
        padx=5,
        pady=5,
        borderwidth=0,
    )
    # Add rounded corners (requires a custom canvas-based button for full effect)
    button.config(highlightbackground=STYLE_CONFIG['button_color'], highlightcolor=STYLE_CONFIG['button_color'])

def apply_frame_style(frame, bg_color=STYLE_CONFIG['background_color']):
    """Apply consistent frame style."""
    frame.config(bg=bg_color)

def apply_label_style(label, text, font=STYLE_CONFIG['font'], fg='black'):
    """Apply consistent label style."""
    label.config(text=text, font=font, fg=fg, bg=STYLE_CONFIG['background_color'])

def create_gradient(width, height, color1_hex, color2_hex):
    """Create a gradient background image."""

    color1 = tuple(int(color1_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    color2 = tuple(int(color2_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    
    image = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(image)
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * y / height)
        g = int(color1[1] + (color2[1] - color1[1]) * y / height)
        b = int(color1[2] + (color2[2] - color1[2]) * y / height)
        draw.line((0, y, width, y), fill=(r, g, b))
    return ImageTk.PhotoImage(image)