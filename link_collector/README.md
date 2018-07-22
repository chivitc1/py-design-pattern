1. Start fake web server
cd web/
python3 -m http.server

Browse to http://localhost:8000

2. Connect to a page and parse all the links from that page => use set

RUN:
python link_collector/link_parser.py http://localhost:8000/contact.html

3. Need to build a site map: which links were linked to from which pages => use dict

4. Use queue to process multiple requests parallel as replacement for currently recursive collect_links