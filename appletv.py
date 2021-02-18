#appletv.py
import sys
from datetime import date
import logging
from pysitemap import crawler

if __name__ == '__main__':
    if '--iocp' in sys.argv:
        from asyncio import events, windows_events
        sys.argv.remove('--iocp')
        logging.info('using iocp')
        el = windows_events.ProactorEventLoop()
        events.set_event_loop(el)

    # root_url = sys.argv[1]
    root_url = 'https://tv.apple.com/'
    today = date.today()
    d = today.strftime("%m.%d.%y")
    crawler(root_url, out_file=f'../outputs/apple{d}.txt', out_format='txt')
             
