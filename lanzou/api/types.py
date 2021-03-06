"""
API 处理后返回的数据类型
"""

from collections import namedtuple

File = namedtuple('File', ['name', 'id', 'time', 'size', 'type', 'downs', 'has_pwd', 'has_des'])
Folder = namedtuple('Folder', ['name', 'id', 'has_pwd', 'desc'])
FolderId = namedtuple('FolderId', ['name', 'id', 'desc', 'now'])
RecFile = namedtuple('RecFile', ['name', 'id', 'type', 'size', 'time'])
RecFolder = namedtuple('RecFolder', ['name', 'id', 'size', 'time', 'files'])
FileDetail = namedtuple('FileDetail', ['code', 'name', 'size', 'type', 'time', 'desc', 'pwd', 'url', 'durl'],
                        defaults=(0, *[''] * 8))
ShareInfo = namedtuple('ShareInfo', ['code', 'name', 'url', 'pwd', 'desc', 'time', 'size'], defaults=(0, *[''] * 6))
DirectUrlInfo = namedtuple('DirectUrlInfo', ['code', 'name', 'durl'])
FolderInfo = namedtuple('Folder', ['name', 'id', 'pwd', 'time', 'desc', 'url', 'size', 'size_int'],
                        defaults=(*('',) * 7, 0))
FileInFolder = namedtuple('FileInFolder', ['name', 'time', 'size', 'type', 'url', 'pwd'], defaults=('',) * 6)
FolderDetail = namedtuple('FolderDetail', ['code', 'folder', 'files'], defaults=(0, FolderInfo(), FileInFolder()))
