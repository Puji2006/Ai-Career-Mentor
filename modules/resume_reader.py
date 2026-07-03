from pypdf import PdfReader


def read_resume(uploaded_file):
    """
    Read PDF resume and return extracted text.
    """

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    return resume_text