import os
from win32com import client


def doc_to_docx(path):
    print("Path: {}".format(path))
    if not os.path.isabs(path):
        print(f'Not absolute path')
        return
    if not os.path.exists(path):
        print('file not exists')
        return
    if os.path.splitext(path)[1] != '.doc':
        print('file type error')
        return

    app = client.Dispatch('Word.Application')
    # app = client.Dispatch('kwps.Application')
    app.DisplayAlerts = False
    document = app.Documents.Open(path)
    document.SaveAs(os.path.splitext(path)[0] + '.docx', 12)
    document.Close()
    app.Quit()



if __name__ == '__main__':
    path = r""
    doc_to_docx(path)