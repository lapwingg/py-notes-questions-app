"""top_bar_producer.py"""
from src.presentation.qpresentation_widget import QPresentationWidget


class TopBarProducer:
    """Helper which provides app style top bar"""
    @classmethod
    def produce_top_bar(cls, buttons=None):
        """Produces top bar with buttons"""
        top_bar_layout = QPresentationWidget.produce_horizontal_layout()
        max_elem = 4
        buttons_count = len(buttons)
        widgets_count = max_elem - buttons_count
        for i in range(0, widgets_count + 1):
            widget = QPresentationWidget.produce_widget()
            top_bar_layout.addWidget(widget)

        for i in range(0, buttons_count):
            top_bar_layout.addWidget(buttons[i])

        return top_bar_layout
