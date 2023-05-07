import os
import PyPDF2

def merge_pdfs(docs_directory):
    pdf_files = [f for f in os.listdir(docs_directory) if f.endswith('.pdf')]
    pdf_files.sort()

    merger = PyPDF2.PdfMerger()

    for pdf in pdf_files:
        pdf_path = os.path.join(docs_directory, pdf)
        merger.append(pdf_path)

    #merged_pdf_path = os.path.join(docs_directory, 'all_merged.pdf')

    #get current project name
    project_name = os.path.basename(os.path.normpath(docs_directory))

    merged_pdf_path = os.path.join(docs_directory, project_name + '_merged.pdf')
    merger.write(merged_pdf_path)
    merger.close()

    # move merged pdf file one level down
    os.rename(merged_pdf_path, os.path.join(docs_directory, '..', 'all_merged.pdf'))
    




def merge_all_pdfs(root_directory):
    for subdir, dirs, files in os.walk(root_directory):
        for d in dirs:
            docs_directory = os.path.join(subdir, d, 'Docs')
            if os.path.isdir(docs_directory):
                merge_pdfs(docs_directory)

root_directory = input('Enter root directory path: ')
merge_all_pdfs(root_directory)
