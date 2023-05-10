''' 
crawl the webpage to extract all the links 
and then download pdf.
'''
import logging
from PdfDownloadLib import request_get, extract_pdf_links, handle_pdf_links, download_pdfs

#global setting
max_pdf_download = 2
delay = 1
url='https://apptimdev.bsite.net/Home/Pdf'

domain = None
timeout = 30

if __name__ == "__main__":
    try:
        res = request_get(url, headers=None, timeout=timeout)
        if res.status_code == 200:            
            pdf_links = extract_pdf_links(res)
            pdf_links = handle_pdf_links(pdf_links, url, domain=domain)
            download_pdfs(pdf_links, delay=0, max_num_limit=max_pdf_download)
        else:
            print('Status Code: ', res.status_code)

    except Exception as e:
        logging.exception("main exception")