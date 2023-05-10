import requests 
import random
from bs4 import BeautifulSoup 
import time, re, logging


def get_user_agent():
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
    return random.choice(USER_AGENTS)


def save_file(file_name, res):
    # res: reponse object type
    with open(file_name, 'wb') as f: 
        for chunk in res.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk)


def request_get(url, headers=None, cookies=None, timeout=30, stream=False):
    if headers is None:
        user_agent = get_user_agent()
        #print(f'user agent:{user_agent}')
        headers = {
            'User-Agent': user_agent
        }
    res = requests.get(url, headers=headers, cookies=cookies, timeout=timeout, stream=stream)
    # print('Url: ',res.url)
    # print('Object Type: ',type(res)) 
    # print('Header Information: ',res.headers)        
    # print('Encoding: ',res.encoding)
    # print('Status Code: ',res.status_code)
    # content_type = res.headers['content-type']
    # print('Content Type:',content_type)
    return res


def download_pdf(link):
    try:
        # obtain filename by splitting url and getting last string
        file_name = link.split('/')[-1]            
        print ("Downloading file: %s"%file_name)
        res = request_get(link, stream = True)
        if res.status_code == 200:
            content_type = res.headers['content-type']
            # application/pdf
            if 'pdf' in content_type:
                save_file(file_name, res)
            else:
                print('Invalid content type for pdf')
        else:
            print('Status Code: ', res.status_code)
            print(f'Pdf donwload link: {link}') 
    except Exception as e:
        print(f'Pdf donwload is fail for link: {link}') 
        logging.exception("download_pdf exception")



def download_pdfs(pdf_links, delay=0, max_num_limit=0):
    count_download = 0
    for link in pdf_links:
        '''
        iterate all links in pdf_links 
        and download pdf one by one
        '''
        download_pdf(link)

        count_download+=1        
        if max_num_limit>0 and count_download>=max_num_limit:
            break
        if delay>0:
            time.sleep(delay)        
    print("Download task is completed!")
        

def extract_pdf_links(res):    
    # create beautiful-soup object 
    bs = BeautifulSoup(res.content, 'html5lib')          
    links = bs.findAll('a') # find all a tag on web-page 
    # for link in links:
    #     if link.has_attr('href') and link['href'].endswith('pdf'):
    #         print(link['href'])
    pdf_links = [link['href'] for link in links if 'href' in link.attrs and link['href'].endswith('pdf')] 
    return pdf_links


def handle_url(link, url, domain=None):
    matchObj  = re.search("^(https://|http://).*$", link)
    if not matchObj:
        matchObj  = re.search("^/{1}.+$", link)
        if matchObj:
            if domain is None:
                #get domain from url
                #url start with http:// or https://
                matchObj  = re.search("^(https://|http://).*$", url)
                if matchObj:
                    matchObj  = re.search("^(https://|http://)", url)
                    url_head = matchObj.group()
                    url_main = re.sub("^(https://|http://)", "", url)
                    url_firstpart = url_main.split("/")[0]
                    url_domain = url_head + url_firstpart
                    # print(url_head)
                    # print(url_main)
                    # print(url_firstpart)
                    # print(f"url_domain: {url_domain}")
                    return url_domain + link
            else:
                return domain + link
    return link


def handle_pdf_links(links, url, domain=None):
    result_links = []
    for link in links:
        result_links.append(handle_url(link, url, domain=domain))
    return result_links