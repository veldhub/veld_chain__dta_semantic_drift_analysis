import os

from lxml import etree


PATH_INPUT = "/veld/input/"
PATH_OUTPUT = "/veld/output/"
XMLNS = {
    "xmlns": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace",
}


def delete_output():
    for file in os.listdir(PATH_OUTPUT):
        if file != ".gitkeep":
            os.remove(PATH_OUTPUT + file)


def load_xml(path_xml):
    xml = None
    with open(path_xml, "r") as f:
        try:
            xml = etree.parse(f)
        except etree.XMLSyntaxError as ex:
            print("etree.XMLSyntaxError:", ex)
    return xml


def extract_decade(xml):
    decade = None
    xpath_base_search = "/xmlns:TEI/xmlns:teiHeader/xmlns:fileDesc/xmlns:sourceDesc/xmlns:biblFull/xmlns:publicationStmt/xmlns:date"
    xpath_publication = xpath_base_search + "[@type='publication']"
    xpath_creation = xpath_base_search + "[@type='creation']"
    xpath_search = xpath_publication + "|" + xpath_creation
    date = xml.xpath(xpath_search, namespaces=XMLNS)
    if date:
        if len(date) == 1:
            decade = date[0].text.split("-")[0][:-1]
        else:
            print("found multiple dates. Skipping")
    else:
        print("no date found")
    return decade


def extract_text(xml):
    text = ""
    sentence = ""
    for s in xml.xpath("//xmlns:s", namespaces=XMLNS):
        s_id = s.attrib.get(f"{{{XMLNS['xml']}}}id")
        if "_" not in s_id:
            text += sentence + "\n"
            sentence = ""
        for w in s.xpath(".//xmlns:w", namespaces=XMLNS):
            token = w.attrib.get("lemma")
            pos = w.attrib.get("pos")
            if token and pos:
                if not pos.startswith("$"):
                    sentence += token
                if not w.attrib.get("join") == "right":
                    sentence += " "
    if not text:
        print("no text found")
    return text


def persist_text(path_txt, text):
    print("appending to:", path_txt)
    with open(path_txt, "a") as f:
        f.write(text)


def main():

    # produce output
    delete_output()
    for file in os.listdir(PATH_INPUT):
        path_xml = PATH_INPUT + file
        print("processing:", file)
        xml = load_xml(path_xml)
        if xml:
            decade = extract_decade(xml)
            if decade:
                text = extract_text(xml)
                path_txt = PATH_OUTPUT + decade + ".txt"
                persist_text(path_txt, text)

    # remove all but samples
    sample_set = os.getenv("sample_set")
    if sample_set is not None:
        sample_set = [s + ".txt" for s in sample_set.split(",")]
        for file in os.listdir(PATH_OUTPUT):
            if file not in sample_set:
                file_path = PATH_OUTPUT + file
                print("removing:", file_path)
                os.remove(file_path)


if __name__ == "__main__":
    main()

