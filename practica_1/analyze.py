from grobid_client.grobid_client import GrobidClient

def process_pdf():
    client = GrobidClient(config_path="../config.json")
    client.process("processFulltextDocument", "../pdfs/input", output="../pdfs/output", consolidate_citations=True, tei_coordinates=True, force=True)
