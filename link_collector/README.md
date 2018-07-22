1. Start fake web server
cd web/
python3 -m http.server

Browse to http://localhost:8000

2. Connect to a page and parse all the links from that page

RUN:
python link_collector/link_parser.py http://localhost:8000/contact.html

