from os.path import basename, dirname, join
from docx import Document, ImagePart


def extract_image(document):
    for p in document.paragraphs:
        for image in p._element.xpath('.//pic:pic'):
            for img_id in image.xpath('.//a:blip/@r:embed'):
                part = document.part.related_parts[img_id]
                if not isinstance(part, ImagePart):
                    continue
                save_dir = dirname(__file__)
                save_path = join(save_dir, basename(part.partname))
                with open(save_path, 'wb') as f:
                    f.write(part.blob)


if __name__ == '__main__':
    doc = Document("./output/test.docx")
    extract_image(doc)

