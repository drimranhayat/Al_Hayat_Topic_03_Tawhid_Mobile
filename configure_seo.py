"""Set real canonical URLs and generate a sitemap after choosing the deployment URL."""
import argparse,re,html
from pathlib import Path
from urllib.parse import urlsplit,quote
p=argparse.ArgumentParser();p.add_argument('--base-url',required=True);p.add_argument('--directory',default='dist');a=p.parse_args()
base=a.base_url.rstrip('/')+'/';url=urlsplit(base)
if url.scheme!='https' or not url.netloc or url.query or url.fragment:raise SystemExit('Use the real HTTPS deployment base URL without a query or fragment.')
root=Path(a.directory);urls=[]
for f in sorted(root.rglob('*.html')):
 if f.name=='404.html':continue
 rel=f.relative_to(root).as_posix();canonical=base if rel=='index.html' else base+quote(rel)
 s=f.read_text();s=re.sub(r'<link rel="canonical"[^>]*>|<meta property="og:url"[^>]*>','',s)
 s=s.replace('</head>',f'<link rel="canonical" href="{html.escape(canonical,quote=True)}"><meta property="og:url" content="{html.escape(canonical,quote=True)}"></head>');f.write_text(s);urls.append(canonical)
(root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+html.escape(u)+'</loc></url>' for u in urls)+'</urlset>')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'sitemap.xml\n')
print('Configured',len(urls),'canonical pages and sitemap for',base)
