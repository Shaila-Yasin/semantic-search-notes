import os


def load_documents(notes_folder):
    """
    Reads all Markdown (.md) files from the given folder.

    Args:
        notes_folder (str): Path to the notes directory.

    Returns:
        list: A list of dictionaries containing
              filename and file content.
    """

    documents = []

    # Loop through every file in the notes folder
    for filename in os.listdir(notes_folder):

        # Process only Markdown files
        if filename.endswith(".md"):

            file_path = os.path.join(notes_folder, filename)

            # Open and read the file
            with open(file_path, "r", encoding="utf-8") as file:

                content = file.read()

                documents.append({
                    "filename": filename,
                    "content": content
                })

    return documents