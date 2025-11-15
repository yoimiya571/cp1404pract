from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy app demonstrating box layout with greeting functionality."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet button press, display greeting with name if provided."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}" if name else "Hello"

    def handle_clear(self):
        """Handle clear button press, reset input and output fields."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'


BoxLayoutDemo().run()
