class TextOperation:
    ADD = "add"
    DELETE = "delete"

    def __init__(self, op_type, character=None):
        self.op_type = op_type
        self.character = character

    def __repr__(self):
        if self.character:
            return f"TextOperation({self.op_type!r}, {self.character!r})"
        return f"TextOperation({self.op_type!r})"


class TextEditor:
    def __init__(self):
        self.text = []
        self.history = []

    def display(self):
        current = "".join(self.text)
        print(f"  Text: '{current}'")

    def add(self, character):
        self.text.append(character)
        self.history.append(TextOperation(TextOperation.ADD, character))
        print(f"[ADD '{character}']")
        self.display()

    def delete(self):
        if not self.text:
            print("[DELETE] Nothing to delete.")
            self.display()
            return
        character = self.text.pop()
        self.history.append(TextOperation(TextOperation.DELETE, character))
        print(f"[DELETE '{character}']")
        self.display()

    def undo(self):
        if not self.history:
            print("[UNDO] Nothing to undo.")
            self.display()
            return
        last_op = self.history.pop()
        if last_op.op_type == TextOperation.ADD:
            self.text.pop()
            print(f"[UNDO add '{last_op.character}']")
        elif last_op.op_type == TextOperation.DELETE:
            self.text.append(last_op.character)
            print(f"[UNDO delete '{last_op.character}']")
        self.display()

if __name__ == "__main__":
    editor = TextEditor()

    print("=== Adding characters: H, i, ! ===")
    editor.add("H")
    editor.add("i")
    editor.add("!")

    print("\n=== Deleting last character ===")
    editor.delete()

    print("\n=== Undo the deletion ===")
    editor.undo()

    print("\n=== Undo the 'i' addition ===")
    editor.undo()

    print("\n=== Undo the 'H' addition ===")
    editor.undo()

    print("\n=== Undo on empty history ===")
    editor.undo()

    print("\n=== Delete on empty text ===")
    editor.delete()

    print("\n=== Build 'Hello' then undo twice ===")
    for ch in "Hello":
        editor.add(ch)
    editor.undo()
    editor.undo()