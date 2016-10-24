from selenium import webdriver 
import time 

def browse_web(proxy):
    proxy = proxy.replace('\n', '')
    service_args = [
    '--proxy=' + proxy,
    '--proxy-type=http',
    ]
    print service_args
    browser = webdriver.PhantomJS(service_args=service_args)
    with open('weburls.txt', 'rb') as f:
        for each_url in f:
            try:
                each_url = each_url.replace('\n', '')
                print each_url
                browser.get(each_url)
    #browser.get("http://paris.quel-serrurier.com/serrurier-en-urgence")    
    #browser.get("http://neuilly-sur-seine.quel-serrurier.com/quentin-serrurerie")
                print "loaded"
                time.sleep(5)
                to_click = browser.find_element_by_class_name('vote')
                to_click.click()
                time.sleep(1)
            except:
                print "failed for url", each_url
        browser.quit()

def main():
    with open('proxiesone.txt', 'rb') as f:
        for each_ip in f:
            browse_web(each_ip)



if __name__ == '__main__':
    main()

