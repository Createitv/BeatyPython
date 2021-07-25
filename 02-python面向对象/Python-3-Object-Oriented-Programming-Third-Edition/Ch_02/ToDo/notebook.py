import datetime

last_id = 0


class Note(object):
    "笔记记录"

    def __init__(self, memo, tags=''):
        "笔记时间，笔记内容，笔记种类"
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        "根据内容和笔记Tag匹配笔记"
        return filter in self.memo or filter in self.tags


class NoteBook():

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]


if __name__ == '__main__':
    n = NoteBook()
    n.new_note('hello world')
    n.new_note('hello again')
    print(n.notes)
    print(n.notes[0].memo, n.notes[0].id)
    print(n.notes[1].memo)
    n.modify_memo(2, "show me")
    print(n.search('hello'))
    print(n.notes[0].memo)
