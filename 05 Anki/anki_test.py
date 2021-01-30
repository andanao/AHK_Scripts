from ankipandas import Collection
import pandas as pd

anki_path = "C:\\Users\\Adrian\\AppData\\Roaming\\Anki2\\User 1\\collection.anki2"
col = Collection(path = anki_path)

# Add a note type HSK
col.notes.add_note('HSK',['test_python','test_python','','','','','',],ntags=['DHS'],inplace=True)
col.summarize_changes()

# Below should write changes to Anki but its not working ¯\_(ツ)_/¯ 
# col.write(modify=True,add=True)pip 