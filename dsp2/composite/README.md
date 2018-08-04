$ python -i dsp2/composite/file_folder.py

```python
>>> folder1 = Folder("folder1")

>>> folder2 = Folder("folder2")

>>> root.add_child(folder1)

>>> root.add_child(folder2)

>>> root

<__main__.Folder object at 0x7efc19e41eb8>

>>> folder11 = Folder("folder11")

>>> folder1.add_child(folder11)

>>> file111 = File("file111", "contents")

>>> folder11.add_child(file111)

>>> file21 = File("file21", "other contents")

>>> folder2.add_child(file21)

>>> folder2.children

{'file21': <__main__.File object at 0x7efc187c9780>}

>>> folder2.move('/folder1/folder11')

>>> folder11.children

{'folder2': <__main__.Folder object at 0x7efc187c9588>, 'file111': <__main__.File object at 0x7efc187c9710>}

>>> folder2.children

{'file21': <__main__.File object at 0x7efc187c9780>}
{'folder11': <__main__.Folder object at 0x7efc187c9668>}
>>> file21.move('/folder1')

>>> folder1.children

{'folder11': <__main__.Folder object at 0x7efc187c9668>, 'file21': <__main__.File object at 0x7efc187c9780>}
```