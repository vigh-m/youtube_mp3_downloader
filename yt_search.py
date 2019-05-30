from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import yt_download as dlHandler

opts = Options()
opts.set_headless()
#assert opts.headless

browser = Firefox(options=opts)
#browser.get('https://www.youtube.com')

#print('Fetched the website')

#search_box = browser.find_element_by_name("search_query")
#search_box.send_keys('Porcupine Tree')
#search_box.submit()

search_term = raw_input("Enter the video to search for:\n")

print(search_term)

search_term.replace(' ', '+')

print(search_term)

print('Searched for the requested name')
browser.get('https://www.youtube.com/results?search_query='+search_term)

print("Showing the first 10 results:\n")

results = browser.find_elements_by_xpath("//*[@id='video-title']")

i = 1

#print(results[1].get_attribute('class'))
#print(results[1])

for r in results:
	print('{} - {}'.format(i, r.text.encode('utf-8')))
	i+=1
	if i > 10:
		break

vid_number = input("Enter the number of the video to dl:\n")

if isinstance(vid_number, int) != True:
	print("Incorrect Input")
	print(type(vid_number))
	browser.close()
	quit()

if vid_number > len(results) or vid_number < 1:
	print("Number out of range")
	browser.close()
	quit()

dl_element = browser.find_element_by_link_text(results[vid_number - 1].text)

print(dl_element.text)
#print(dl_element.get_attribute('href'))

vid_link = dl_element.get_attribute('href').split('&')[0]

print('Video Link = {}'.format(vid_link))

dlHandler.download(vid_link)

browser.close()
quit()
