{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "#import chromedriver\n",
    "from splinter import Browser\n",
    "\n",
    "url = \"https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest\"\n",
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html, 'html.parser')\n",
    "\n",
    "#find titles and article teasers in html\n",
    "titles = soup.find('div', class_='content_title').text\n",
    "article_teasers = soup.find('div', class_='article_teaser_body').text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NASA's Mars 2020 Rover Completes Its First Drive\n",
      "In a 10-plus-hour marathon, the rover steered, turned and drove in 3-foot (1-meter) increments over small ramps.\n"
     ]
    }
   ],
   "source": [
    "#save them as variables for later\n",
    "news_title = titles\n",
    "news_p     = article_teasers\n",
    "print(news_title)\n",
    "print(news_p)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "#set browser for jpl site\n",
    "url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA14712_ip.jpg'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#click on image link and get url for image\n",
    "browser.find_by_id('full_image').click()\n",
    "featured_image_url = browser.find_by_css('.fancybox-image').first['src']\n",
    "\n",
    "featured_image_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "#get martian weather report\n",
    "#url\n",
    "twitter_url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "#visit url\n",
    "browser.visit(twitter_url)\n",
    "twitter_html = browser.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "#set up web driver to read javascript?\n",
    "from selenium import webdriver\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(twitter_url)\n",
    "twitter_html = driver.page_source\n",
    "driver.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A 4K sweep across the foothills of Mt. Sharp, #Mars, using @MarsCuriosity MastCam imagery.\n",
      "\n",
      "On YouTube @ 4k60fps: https://youtu.be/LHLORu8vBmo \n",
      "\n",
      "Full Image: https://flic.kr/p/2i3w9PP pic.twitter.com/lnYE8BO7Nl\n"
     ]
    }
   ],
   "source": [
    "#make soup\n",
    "twitter_soup = BeautifulSoup(twitter_html, 'html.parser')\n",
    "#grab first tweet out of soup\n",
    "mars_weather = twitter_soup.find_all('p', class_=\"tweet-text\")[0].text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table class=\"tablepress tablepress-id-p-mars\" id=\"tablepress-p-mars\">\n",
      " <tbody>\n",
      "  <tr class=\"row-1 odd\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Equatorial Diameter:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    6,792 km\n",
      "    <br/>\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-2 even\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Polar Diameter:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    6,752 km\n",
      "    <br/>\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-3 odd\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Mass:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    6.39 × 10^23 kg\n",
      "    <br/>\n",
      "    (0.11 Earths)\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-4 even\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Moons:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    2 (\n",
      "    <a href=\"https://space-facts.com/moons/phobos/\">\n",
      "     Phobos\n",
      "    </a>\n",
      "    &amp;\n",
      "    <a href=\"https://space-facts.com/moons/deimos/\">\n",
      "     Deimos\n",
      "    </a>\n",
      "    )\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-5 odd\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Orbit Distance:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    227,943,824 km\n",
      "    <br/>\n",
      "    (1.38 AU)\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-6 even\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Orbit Period:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    687 days (1.9 years)\n",
      "    <br/>\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-7 odd\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Surface Temperature:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    -87 to -5 °C\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-8 even\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     First Record:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    2nd millennium BC\n",
      "   </td>\n",
      "  </tr>\n",
      "  <tr class=\"row-9 odd\">\n",
      "   <td class=\"column-1\">\n",
      "    <strong>\n",
      "     Recorded By:\n",
      "    </strong>\n",
      "   </td>\n",
      "   <td class=\"column-2\">\n",
      "    Egyptian astronomers\n",
      "   </td>\n",
      "  </tr>\n",
      " </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "#mars facts table\n",
    "#url\n",
    "mars_facts_url = 'https://space-facts.com/mars/'\n",
    "#visit url\n",
    "browser.visit(mars_facts_url)\n",
    "mars_facts_html = browser.html\n",
    "#make soup\n",
    "mars_facts_soup = BeautifulSoup(mars_facts_html, 'html.parser')\n",
    "#find table\n",
    "mars_facts = mars_facts_soup.find_all('table', class_=\"tablepress-id-p-mars\")[0].prettify()\n",
    "print(mars_facts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>0</th>\n",
      "      <th>1</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg  (0.11 Earths)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (  Phobos  &amp;  Deimos  )</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km  (1.38 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "#convert to pandas DF\n",
    "import pandas as pd\n",
    "mars_table = pd.read_html(mars_facts)\n",
    "mars_df = mars_table[0]\n",
    "mars_df_html = pd.DataFrame.to_html(mars_df)\n",
    "print(mars_df_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#mars hemispheres\n",
    "#url\n",
    "mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "#visit url\n",
    "browser.visit(mars_hemispheres_url)\n",
    "mars_hemispheres_html = browser.html\n",
    "#make soup\n",
    "mars_hemispheres_soup = BeautifulSoup(mars_hemispheres_html, 'html.parser')\n",
    "#find table\n",
    "mars_hemispheres = mars_hemispheres_soup.find_all('h3')\n",
    "\n",
    "#create empty list to store hemispher names\n",
    "hemisphere_list = []\n",
    "#show html\n",
    "\n",
    "for hemisphere in mars_hemispheres:\n",
    "    hemisphere_list.append(hemisphere.text)\n",
    "\n",
    "\n",
    "#create list of hemisphere urls\n",
    "hemisphere_image_urls = []\n",
    "\n",
    "#for loop using splinter to find links, click on them\n",
    "for hemisphere in hemisphere_list:\n",
    "    #click on link with hemisphere name\n",
    "    browser.click_link_by_partial_text(hemisphere)\n",
    "    #open page to full res\n",
    "    browser.find_link_by_text('Open').first.click()\n",
    "    #grab url\n",
    "    hemisphere_url = browser.find_by_css('.wide-image').first['src']\n",
    "    #add to dictionary\n",
    "    hemisphere_image_dict = {'title': hemisphere, \"img_url\":hemisphere_url}\n",
    "    #add dictionary to list\n",
    "    hemisphere_image_urls.append(hemisphere_image_dict)\n",
    "    #go back to 'home'page\n",
    "    browser.visit(mars_hemispheres_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg'}]"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#did it work?\n",
    "hemisphere_image_urls"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
