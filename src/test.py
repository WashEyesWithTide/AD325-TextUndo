import unittest
from text_edit import TextEditor, TextOperation


class TestTextEditor(unittest.TestCase):

    def test_add_characters(self):
        editor = TextEditor()
        editor.add("H")
        editor.add("i")
        self.assertEqual("".join(editor.text), "Hi")
        self.assertEqual(len(editor.history), 2)

    def test_delete_character(self):
        editor = TextEditor()
        editor.add("H")
        editor.add("i")
        editor.delete()
        self.assertEqual("".join(editor.text), "H")
        self.assertEqual(editor.history[-1].op_type, TextOperation.DELETE)
        self.assertEqual(editor.history[-1].character, "i")

    def test_undo_reverses_add(self):
        editor = TextEditor()
        editor.add("H")
        editor.add("i")
        editor.undo()
        self.assertEqual("".join(editor.text), "H")
        self.assertEqual(len(editor.history), 1)

    def test_undo_reverses_delete(self):
        editor = TextEditor()
        editor.add("H")
        editor.add("i")
        editor.delete()
        editor.undo()
        self.assertEqual("".join(editor.text), "Hi")

    def test_undo_on_empty_history(self):
        editor = TextEditor()
        editor.undo()
        self.assertEqual("".join(editor.text), "")
        self.assertEqual(editor.history, [])

    def test_delete_on_empty_text(self):
        editor = TextEditor()
        editor.delete()
        self.assertEqual("".join(editor.text), "")
        self.assertEqual(editor.history, [])

    def test_multiple_consecutive_undos(self):
        editor = TextEditor()
        for ch in "Hi!":
            editor.add(ch)
        editor.undo()
        editor.undo()
        editor.undo()
        editor.undo()
        self.assertEqual("".join(editor.text), "")
        self.assertEqual(editor.history, [])


if __name__ == "__main__":
    unittest.main()