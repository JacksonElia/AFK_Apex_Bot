from tkinter import ttk


# MODIFIES THE TEXTFIELD CLASS TO ADD PLACEHOLDERS
class PlaceholderEntry(ttk.Entry):
    def __init__(self, container, placeholder, **kwargs):
        # PASSES IN A CUSTOM STYLE TO THE TEXTFIELD CLASS AND KWARGS SO YOU CAN USE NORMAL PARAMETERS
        super().__init__(container, style="Placeholder.TEntry", **kwargs)
        self.placeholder = placeholder
        # SETS THE TEXTFIELD'S PLACEHOLDER
        self.insert("0", self.placeholder)
        # BINDS A FUNCTION TO THE TEXTFIELD FOR WHEN THEY ARE SELECTED OR DESELECTED
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    # FUNCTION USED FOR WHEN TEXTFIELD IS CLICKED TO REMOVE THE PLACEHOLDER
    def _clear_placeholder(self, e):
        if self["style"] == "Placeholder.TEntry":
            self.delete("0", "end")
            self["style"] = "TEntry"

    # FUNCTION USED FOR WHEN TEXTFIELD IS UNCLICKED TO ADD THE PLACEHOLDER
    def _add_placeholder(self, e):
        if not self.get():
            self.insert("0", self.placeholder)
            self["style"] = "Placeholder.TEntry"


# FUNCTION FOR CREATING AND RETURNING THE CUSTOM TEXTFIELD
def create_custom_entry(root, placeholder_text):
    style = ttk.Style(root)
    style.configure(style="Placeholder.TEntry", foreground="#d5d5d5")
    # USES THE KWARGS
    entry = PlaceholderEntry(container=root, placeholder=placeholder_text, background="white", font=("Helvetica", 10, "bold"), width=33)
    return entry
