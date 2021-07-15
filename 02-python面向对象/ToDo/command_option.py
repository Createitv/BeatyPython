import sys
from notebook import NoteBook, Note


class Menu():
    def __init__(self):
        self.notebook = NoteBook()
        self.choices = {
            '1': self.show_notes,
            '2': self.search_notes,
            '3': self.add_note,
            '4': self.modify_note,
            '5': self.quit
        }

    def display_menu(self):
        print("""
            1. Show All notes.
            2. Search notes.
            3. Add Note.
            4. Modify Note.
            5. Quit
              """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not available choice".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("id\ttag\tmemo\tcreation_time\t")
            print("{0}: {1:12} {2:12} {3:8}".format(
                note.id, note.tags, note.memo, note.creation_date))

    def search_notes(self):
        filter = input("Search for:")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo:")
        self.notebook.new_note(memo)
        print("Your note has been added")

    def modify_note(self):
        id = input("Enter a note id:")
        memo = input("Enter a memo:")
        tags = input("Enter tags:")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thanks for you using your notebook today")
        sys.exit(0)


if __name__ == '__main__':
    Menu().run()
