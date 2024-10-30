```powershell
[yasei@localhost TP-dev]$ cat /tmp/urls_list
https://www.ynov.com
https://example.org
https://www.thinkerview.com
https://www.torproject.org
https://google.com
https://loldle.com
https://youtube.com
https://open.spotify.com
https://github.com
https://trello.com
[yasei@localhost TP-dev]$ time python tp-6/web_sync_mutiple.py /tmp/urls_list
Content saved to web_www.ynov.com
Content saved to web_example.org
Content saved to web_www.thinkerview.com
Content saved to web_www.torproject.org
Content saved to web_google.com
Content saved to web_loldle.com
Content saved to web_youtube.com
Content saved to web_open.spotify.com
Content saved to web_github.com
Content saved to web_trello.com

real    0m5.971s
user    0m0.038s
sys     0m0.180s
[yasei@localhost TP-dev]$ time python tp-6/web_async_multiple.py /tmp/urls_list
Content saved to web_async_www.ynov.com
Content saved to web_async_example.org
Content saved to web_async_www.thinkerview.com
Content saved to web_async_www.torproject.org
Content saved to web_async_google.com
Content saved to web_async_loldle.com
Content saved to web_async_youtube.com
Content saved to web_async_open.spotify.com
Content saved to web_async_github.com
Content saved to web_async_trello.com

real    0m6.938s
user    0m0.049s
sys     0m0.263s
[yasei@localhost TP-dev]$
```