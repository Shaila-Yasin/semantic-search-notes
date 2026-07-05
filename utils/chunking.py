import re
def chunk_documents(documents): 
    """
    Splits Markdown documents into chunks based on '##' headings.

    Args:
        documents (list): Output from load_documents().

    Returns:
        list: A list of chunk dictionaries.
    """

    chunks = []

    for document in documents:

        lines = document["content"].splitlines()

        current_title = None
        current_content = []

        for line in lines:

            line = line.strip()

            # If we find a new section heading
            if line.startswith("## "):

                # Save the previous chunk before starting a new one
                if current_title is not None:

                    chunks.append({
                        "filename": document["filename"],
                        "title": current_title,
                        "text": "\n".join(current_content).strip()
                    })

                # Start a new chunk
                title = line.replace("## ", "").strip()
                title = re.sub(r'^\d+(\.\d+)*\.\s*', '', title)
                current_title = title

                current_content = []

            else:
                # Add the line to the current section
                current_content.append(line)

        # Save the last chunk in the document
        if current_title is not None:
            chunks.append({
                "filename": document["filename"],
                "title": current_title,
                "text": "\n".join(current_content).strip()
            })

    return chunks