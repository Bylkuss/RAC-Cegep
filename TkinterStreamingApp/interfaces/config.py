# config.py

# Global style configuration
STYLE_CONFIG = {
    'primary_color': '#6a0dad',  # Purple
    'secondary_color': '#ff7f32',  # Orange
    'background_color': '#2c3e50',  # Dark Blue
    'button_color': '#f39c12',  # Yellow-orange button
    'font': ('Arial', 12),
    'font_bold': ('Arial', 14, 'bold'),
    'button_radius': 12,
    'hover_effect': {
        'bg_color': '#8e44ad',  # Lighter purple on hover
        'fg_color': 'white',
    }
}

def apply_button_style(button, text, width=20, height=2):
    """Apply a consistent button style to all buttons."""
    button.config(
        text=text,
        width=width,
        height=height,
        bg=STYLE_CONFIG['button_color'],
        fg='white',
        font=STYLE_CONFIG['font_bold'],
        relief='flat',  # Flat design style
        bd=0,  # No border
        highlightthickness=0,  # No highlight on focus
        activebackground=STYLE_CONFIG['hover_effect']['bg_color'],
        activeforeground=STYLE_CONFIG['hover_effect']['fg_color'],
        relief='raised',
        padx=10,
        pady=5,
        borderwidth=0,
    )

def apply_frame_style(frame, bg_color=STYLE_CONFIG['background_color']):
    """Apply consistent frame style."""
    frame.config(bg=bg_color)

def apply_label_style(label, text, font=STYLE_CONFIG['font'], fg='white'):
    """Apply consistent label style."""
    label.config(text=text, font=font, fg=fg)
