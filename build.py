# ============== ICON SYSTEM (line icons, brass on navy) ==============
ICONS = {
 'home': '<path d="M4 10.5 12 4l8 6.5"/><path d="M6 9.5V20h12V9.5"/><path d="M10 20v-5h4v5"/>',
 'building': '<path d="M6 22V4a1 1 0 0 1 1-1h7a1 1 0 0 1 1 1v18"/><path d="M6 12H4a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h16a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1h-2"/><path d="M9 7h2M9 11h2M9 15h2"/>',
 'landmark': '<path d="M3 21h18"/><path d="M5 21V11M9.5 21V11M14.5 21V11M19 21V11"/><path d="M3 11 12 4l9 7"/><path d="M3 11h18"/>',
 'sprout': '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
 'chart': '<path d="M3 21h18"/><rect x="6" y="12" width="3" height="6" rx=".5"/><rect x="11" y="8" width="3" height="10" rx=".5"/><rect x="16" y="5" width="3" height="13" rx=".5"/>',
 'cog': '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/>',
 'bulb': '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"/>',
 'clipboard': '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 12h6M9 16h6"/>',
 'scale': '<path d="M12 3v18"/><path d="M7 21h10"/><path d="M3 7h4c2 0 4-1 5-2 1 1 3 2 5 2h4"/><path d="m6.5 7-3 7a3 3 0 0 0 6 0z"/><path d="m17.5 7-3 7a3 3 0 0 0 6 0z"/>',
 'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
 'pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
 'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>',
 'mail': '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-10 5L2 7"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'euro': '<path d="M4 10h12M4 14h9"/><path d="M19 6a7.7 7.7 0 0 0-5.2-2A7.9 7.9 0 0 0 6 12c0 4.4 3.5 8 7.8 8 2 0 3.8-.7 5.2-2"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
 'moon': '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
 'menu': '<path d="M3 6h18M3 12h18M3 18h18"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
def icon_inline(name):
    return f'<svg class="i-sm" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

import os
import shutil
ROOT=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.join(ROOT,"dist")
URL="https://www.valorisasset.bg"
ICONS['globe']='<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18Z"/>'

SHIELD = ('<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
  '<path d="M16 2.5 4.5 6.4V15c0 7 5 12 11.5 14.5C22.5 27 27.5 22 27.5 15V6.4L16 2.5Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>'
  '<rect x="9.6" y="16" width="2.7" height="6" rx=".4" fill="currentColor"/>'
  '<rect x="14.1" y="12.4" width="2.7" height="9.6" rx=".4" fill="currentColor"/>'
  '<rect x="18.6" y="8.8" width="2.7" height="13.2" rx=".4" fill="currentColor"/>'
  '<path d="M8.5 21.5C12 25 19 24.5 23 17.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" fill="none"/>'
  '</svg>')
LOGO = '<span class="logo-mark">'+SHIELD+'</span><span class="logo-text"><span class="lt-main">Valoris</span><span class="lt-sub">ASSET</span></span>'


def brand(lang):
    return ('Валу','Про','В') if lang=='bg' else ('Valu','Pro','V')

# ---------- chrome strings ----------
T={
 'bg':{'skip':'Към съдържанието','menu':'Меню','theme':'Смяна на тема (светла/тъмна)',
   'req':'Заяви оценка','lang_to':'EN','lang_aria':'Switch to English',
   'n_val':'Оценки','n_about':'За нас','n_blog':'Блог','n_clients':'Клиенти','n_faq':'ЧЗВ','n_contact':'Контакти',
   'd_re':'Недвижими имоти','d_biz':'Бизнес оценки','d_mach':'Машини и съоръжения','d_int':'Нематериални активи','d_agri':'Земеделски земи','d_add':'Допълващи услуги','d_price':'Цени',
   'd_who':'Кои сме ние','d_meth':'Методология','d_net':'Оценителска мрежа',
   'f_tag':'Независим оценител с над 20 години опит и национална мрежа от сертифицирани оценители.',
   'f_services':'Услуги','f_info':'Информация','f_contact':'Контакт',
   'f_about':'За нас','f_price':'Ценоразпис','f_meth':'Методология','f_faq':'Въпроси','f_contacts':'Контакти',
   'f_addr':'София, ул. Примерна 1','f_hours':'Пон–Пет: 9:00–18:00',
   'f_copy':'© 2025 Valoris Asset. Всички права запазени.','f_legal':'Политика за поверителност · Бисквитки · Общи условия',
   'ck':'Използваме бисквитки за основни функции и анализ на трафика. Вижте нашата','ck_link':'Политика за бисквитки','ck_acc':'Приемам','ck_dec':'Само необходимите','ck_aria':'Съгласие за бисквитки','top':'Нагоре',
   'jsonld_desc':'Независими пазарни оценки на недвижими имоти, бизнес, машини и земеделска земя в България.','jsonld_name':'Valoris Asset','jsonld_city':'София','jsonld_street':'ул. Примерна 1'},
 'en':{'skip':'Skip to content','menu':'Menu','theme':'Switch theme (light/dark)',
   'req':'Request a Valuation','lang_to':'BG','lang_aria':'Превключи на български',
   'n_val':'Valuations','n_about':'About','n_blog':'Blog','n_clients':'Clients','n_faq':'FAQ','n_contact':'Contact',
   'd_re':'Real Estate','d_biz':'Business Valuation','d_mach':'Machinery & Equipment','d_int':'Intangible Assets','d_agri':'Agricultural Land','d_add':'Additional Services','d_price':'Pricing',
   'd_who':'Who We Are','d_meth':'Methodology','d_net':'Appraiser Network',
   'f_tag':'Independent appraiser with over 20 years of experience and a nationwide network of certified appraisers.',
   'f_services':'Services','f_info':'Information','f_contact':'Contact',
   'f_about':'About','f_price':'Pricing','f_meth':'Methodology','f_faq':'FAQ','f_contacts':'Contact',
   'f_addr':'Sofia, 1 Primerna St.','f_hours':'Mon–Fri: 9:00–18:00',
   'f_copy':'© 2025 Valoris Asset. All rights reserved.','f_legal':'Privacy Policy · Cookies · Terms',
   'ck':'We use cookies for essential functions and traffic analysis. See our','ck_link':'Cookie Policy','ck_acc':'Accept','ck_dec':'Essential only','ck_aria':'Cookie consent','top':'Back to top',
   'jsonld_desc':'Independent market valuations of real estate, businesses, machinery and agricultural land in Bulgaria.','jsonld_name':'Valoris Asset','jsonld_city':'Sofia','jsonld_street':'1 Primerna St.'},
}

def loc(lang, file):
    base = URL + ('' if lang=='bg' else '/en')
    return base + ('/' if file=='index.html' else '/'+file)

def head(lang, file, title, desc):
    pre = '' if lang=='bg' else '../'
    t=T[lang]
    bg=loc('bg',file); en=loc('en',file)
    canon = bg if lang=='bg' else en
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0f1d33">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="bg" href="{bg}">
<link rel="alternate" hreflang="en" href="{en}">
<link rel="alternate" hreflang="x-default" href="{bg}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'bg_BG' if lang=='bg' else 'en_US'}">
<meta property="og:site_name" content="{T[lang]['jsonld_name']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary_large_image">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self' data: https:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; script-src 'self' 'unsafe-inline'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Inter:wght@400;500;600;700&display=swap">
<link rel="icon" type="image/png" href="{pre}assets/favicon.png">
<link rel="apple-touch-icon" href="{pre}assets/favicon.png">
<meta property="og:image" content="{URL}/assets/logo.jpg">
<link rel="stylesheet" href="{pre}assets/styles.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ProfessionalService","name":"{t['jsonld_name']}","description":"{t['jsonld_desc']}","url":"{URL}","telephone":"{PHONE_L}","email":"{EMAIL}","areaServed":"BG","address":{{"@type":"PostalAddress","addressCountry":"BG","addressLocality":"{t['jsonld_city']}","streetAddress":"{t['jsonld_street']}"}},"priceRange":"€€"}}
</script>
</head>
<body>
<a class="skip-link" href="#main">{t['skip']}</a>'''

def nav(lang, active, file):
    t=T[lang]; b=brand(lang)
    other = ('en/'+file) if lang=='bg' else ('../'+file)
    def a(n): return ' active' if active==n else ''
    return f'''<header class="nav">
  <div class="nav-inner">
    <a href="index.html" class="logo" aria-label="Valoris Asset">
      {LOGO}
    </a>
    <nav aria-label="{t['menu']}">
    <ul class="nav-links" id="navLinks">
      <li class="has-drop">
        <a href="ocenki-nedvizhimi-imoti.html" class="{a('val').strip()}">{t['n_val']}</a>
        <ul class="dropdown">
          <li><a href="ocenki-nedvizhimi-imoti.html">{t['d_re']}</a></li>
          <li><a href="ocenki-biznes.html">{t['d_biz']}</a></li>
          <li><a href="ocenki-mashini.html">{t['d_mach']}</a></li>
          <li><a href="ocenki-nematerialni.html">{t['d_int']}</a></li>
          <li><a href="ocenki-zemedelski-zemi.html">{t['d_agri']}</a></li>
          <li><a href="ocenki-dopalvashti.html">{t['d_add']}</a></li>
          <li><a href="ceni.html">{t['d_price']}</a></li>
        </ul>
      </li>
      <li class="has-drop">
        <a href="za-nas.html" class="{a('about').strip()}">{t['n_about']}</a>
        <ul class="dropdown">
          <li><a href="za-nas.html">{t['d_who']}</a></li>
          <li><a href="metodologia.html">{t['d_meth']}</a></li>
          <li><a href="ocenitelska-mreja.html">{t['d_net']}</a></li>
        </ul>
      </li>
      <li><a href="blog.html" class="{a('blog').strip()}">{t['n_blog']}</a></li>
      <li><a href="klienti.html" class="{a('clients').strip()}">{t['n_clients']}</a></li>
      <li><a href="vyprosi.html" class="{a('faq').strip()}">{t['n_faq']}</a></li>
      <li><a href="kontakti.html" class="{a('contact').strip()}">{t['n_contact']}</a></li>
    </ul>
    </nav>
    <div class="nav-actions">
      <a class="lang-switch" href="{other}" hreflang="{'en' if lang=='bg' else 'bg'}" aria-label="{t['lang_aria']}" data-lang="{'en' if lang=='bg' else 'bg'}">{icon('globe')}{t['lang_to']}</a>
      <button class="icon-btn theme-toggle" id="themeToggle" aria-label="{t['theme']}">
        <span class="sun">{icon('sun')}</span><span class="moon">{icon('moon')}</span>
      </button>
      <a href="kontakti.html" class="btn btn-accent">{t['req']}</a>
      <button class="icon-btn nav-toggle" id="navToggle" aria-label="{t['menu']}" aria-expanded="false" aria-controls="navLinks">{icon('menu')}</button>
    </div>
  </div>
</header>'''

def footer(lang):
    t=T[lang]; b=brand(lang)
    return f'''<footer>
  <div class="f-inner">
    <div class="f-brand">
      <span class="logo">{LOGO}</span>
      <p>{t['f_tag']}</p>
      <div class="f-social">
        <a href="#" aria-label="Facebook" rel="noopener noreferrer" target="_blank">f</a>
        <a href="#" aria-label="LinkedIn" rel="noopener noreferrer" target="_blank">in</a>
      </div>
    </div>
    <div><h4>{t['f_services']}</h4><ul>
      <li><a href="ocenki-nedvizhimi-imoti.html">{t['d_re']}</a></li>
      <li><a href="ocenki-biznes.html">{t['d_biz']}</a></li>
      <li><a href="ocenki-mashini.html">{t['d_mach']}</a></li>
      <li><a href="ocenki-zemedelski-zemi.html">{t['d_agri']}</a></li>
      <li><a href="ocenki-nematerialni.html">{t['d_int']}</a></li>
    </ul></div>
    <div><h4>{t['f_info']}</h4><ul>
      <li><a href="za-nas.html">{t['f_about']}</a></li>
      <li><a href="ceni.html">{t['f_price']}</a></li>
      <li><a href="metodologia.html">{t['f_meth']}</a></li>
      <li><a href="vyprosi.html">{t['f_faq']}</a></li>
      <li><a href="kontakti.html">{t['f_contacts']}</a></li>
    </ul></div>
    <div><h4>{t['f_contact']}</h4><ul>
      <li><a href="tel:{PHONE_L}">{PHONE_D}</a></li>
      <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{t['f_addr']}</li>
      <li>{t['f_hours']}</li>
    </ul></div>
  </div>
  <div class="f-bottom"><span>{t['f_copy']}</span><span>{t['f_legal']}</span></div>
</footer>'''

def tail(lang):
    t=T[lang]
    return f'''<button class="totop" id="toTop" aria-label="{t['top']}">{icon('menu') and ""}↑</button>
<div class="cookie" id="cookieBanner" role="dialog" aria-label="{t['ck_aria']}">
  <p>{t['ck']} <a href="#">{t['ck_link']}</a>.</p>
  <div class="ck-actions">
    <button class="btn btn-accent" data-cookie="accepted">{t['ck_acc']}</button>
    <button class="btn btn-outline" data-cookie="declined">{t['ck_dec']}</button>
  </div>
</div>
<script src="{'' if lang=='bg' else '../'}assets/script.js"></script>
</body>
</html>'''

def doc(lang, file, active, title, desc, body):
    return head(lang,file,title,desc)+"\n"+nav(lang,active,file)+"\n"+body+"\n"+footer(lang)+"\n"+tail(lang)

def write(lang, file, html):
    d = OUT if lang=='bg' else os.path.join(OUT,'en')
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d,file),'w',encoding='utf-8').write(html)

print("i18n core ready")

# =====================================================================
#  PAGE CONTENT  (C[lang] dicts)
# =====================================================================
C={'bg':{},'en':{}}

# ---------- HOMEPAGE ----------
def home_body(lang):
    g=lambda k:C[lang][k]
    s=HOME[lang]
    cards="".join(f'<div class="card reveal"><div class="ic">{icon(ic)}</div><h3>{ti}</h3><p>{d}</p><a class="more" href="{u}">{s["more"]}</a></div>' for ic,ti,d,u in [(c["icon"],c["title"],c["desc"],c["url"]) for c in s["cards"]])
    quotes="".join(f'<div class="quote reveal"><p>{q}</p><div class="by">{n} <span>– {r}</span></div></div>' for q,n,r in [(x["text"],x["name"],x["role"]) for x in s["quotes"]])
    steps="".join(f'<div class="step reveal"><div class="sn">{i+1}</div><div><h3>{ti}</h3><p>{d}</p></div></div>' for i,(ti,d) in enumerate([(x["title"],x["desc"]) for x in s["steps"]]))
    statcells="".join(f'<div class="stat"><div class="n" data-target="{tg}"{(" data-suffix=\""+sf+"\"") if sf else ""}>0</div><div class="l">{l}</div></div>' for tg,sf,l in [(x["value"],x["suffix"],x["label"]) for x in s["stats"]])
    return f'''<main id="main">
<section class="hero"><div class="hero-inner">
  <div class="reveal">
    <span class="eyebrow">{s["eyebrow"]}</span>
    <h1>{s["h1"]}</h1>
    <p>{s["lead"]}</p>
    <div class="hero-actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{s["cta1"]}</a><a href="ceni.html" class="btn btn-ghost-light btn-lg">{s["cta2"]}</a></div>
    <div class="creds">
      <span class="cred">{icon('shield')} {s["cr1"]}</span>
      <span class="cred">{icon('scale')} {s["cr2"]}</span>
      <span class="cred">{icon('landmark')} {s["cr3"]}</span>
      <span class="cred">{icon('pin')} {s["cr4"]}</span>
    </div>
  </div>
  <div class="reveal"><div class="valcard" role="img" aria-label="{s["vc_aria"]}">
    <span class="vc-badge">{s["vc_badge"]}</span>
    <div class="vc-head"><div class="vc-ico">{icon('home')}</div><div><div class="vc-title">{s["vc_title"]}</div><div class="vc-sub">{s["vc_sub"]}</div></div></div>
    <div class="vc-rows">
      <div class="vc-row"><span>{s["vc_r1"]}</span><b>{s["vc_v1"]}</b></div>
      <div class="vc-row"><span>{s["vc_r2"]}</span><b>{s["vc_v2"]}</b></div>
      <div class="vc-row"><span>{s["vc_r3"]}</span><b>{s["vc_v3"]}</b></div>
    </div>
    <div class="vc-value"><span class="lbl">{s["vc_val"]}</span><span class="amt">€ 248 500</span></div>
    <div class="vc-bars" aria-hidden="true"><i style="height:40%"></i><i style="height:65%"></i><i style="height:50%"></i><i style="height:85%"></i><i style="height:70%"></i><i style="height:100%"></i><i style="height:80%"></i></div>
  </div></div>
</div></section>
<section class="section"><div class="wrap stats reveal">{statcells}</div></section>
<section class="section alt"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">{s["sv_eye"]}</span><h2>{s["sv_h"]}</h2><p>{s["sv_p"]}</p></div>
  <div class="grid grid-3">{cards}</div>
</div></section>
<section class="section"><div class="wrap-narrow">
  <div class="section-head reveal"><span class="eyebrow">{s["pr_eye"]}</span><h2>{s["pr_h"]}</h2></div>
  <div class="steps">{steps}</div>
</div></section>
<section class="section alt"><div class="wrap"><div class="cta reveal">
  <div><h3>{s["cta_h"]}</h3><p>{s["cta_p"]}</p></div>
  <div class="actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{s["cta1"]}</a><a href="tel:{PHONE_L}" class="btn btn-ghost-light btn-lg">{PHONE_D}</a></div>
</div></div></section>
<section class="section"><div class="wrap">
  <div class="section-head reveal"><span class="eyebrow">{s["ts_eye"]}</span><h2>{s["ts_h"]}</h2></div>
  <div class="grid grid-3">{quotes}</div>
</div></section>
</main>'''

HOME={
 'bg':{'eyebrow':'20 години на пазара','h1':'Независими <em>експертни оценки</em> на активи в България',
   'lead':'Пазарни оценки на недвижими имоти, бизнес, машини и земеделска земя — изготвени бързо, прецизно и в съответствие с международните стандарти.',
   'cta1':'Заяви оценка','cta2':'Виж цените',
   'cr1':'<b>КНОБ</b>&nbsp;регистриран','cr2':'Вещо лице','cr3':'Одобрен от банки','cr4':'София и региона',
   'vc_aria':'Примерна сертифицирана оценка на апартамент','vc_badge':'СЕРТИФИЦИРАНА ОЦЕНКА',
   'vc_title':'Оценка на апартамент','vc_sub':'гр. София · 98 м² · 2025',
   'vc_r1':'Метод','vc_v1':'Пазарен подход','vc_r2':'Състояние','vc_v2':'Завършено','vc_r3':'Срок','vc_v3':'3–5 дни','vc_val':'Пазарна стойност',
   'stats':[('20','+','години опит'),('15000','+','изготвени оценки'),('100','+','оценители в мрежата'),('28','','области покритие')],
   'sv_eye':'Услуги','sv_h':'Какво оценяваме','sv_p':'Пълен набор от оценителски услуги за частни лица, бизнес и институции.',
   'more':'Научи повече →',
   'cards':[('home','Недвижими имоти','Апартаменти, къщи, офиси, търговски и индустриални имоти.','ocenki-nedvizhimi-imoti.html'),
            ('chart','Бизнес оценки','Оценка на предприятия, дялове и капиталови инструменти.','ocenki-biznes.html'),
            ('cog','Машини и съоръжения','Производствено оборудване, превозни средства, инвентар.','ocenki-mashini.html'),
            ('bulb','Нематериални активи','Търговски марки, патенти, ноу-хау и репутация.','ocenki-nematerialni.html'),
            ('sprout','Земеделски земи','Ниви, трайни насаждения, поземлени имоти и терени.','ocenki-zemedelski-zemi.html'),
            ('clipboard','Допълващи услуги','Консултации, анализи и експертни становища.','ocenki-dopalvashti.html')],
   'pr_eye':'Процес','pr_h':'Как протича една оценка',
   'steps':[('Запитване','Изпращате ни описание на обекта за оценяване по телефон или имейл.'),('Оферта и договор','Получавате конкретна цена и срок в рамките на 24 часа.'),('Оглед','Наш оценител извършва оглед на място и събира необходимите данни.'),('Доклад','Получавате готовия експертен доклад в договорения срок.')],
   'cta_h':'Готови сте да заявите оценка?','cta_p':'Свържете се с нас за безплатна консултация и индивидуална оферта.',
   'ts_eye':'Клиенти','ts_h':'Какво казват за нас',
   'quotes':[('Изключително задоволни от бързото и прецизно изготвяне на оценката. Екипът надхвърли нашите очаквания за професионализъм.','Име Фамилия','Длъжност, Компания ООД'),('Благодарни сме за ползотворното сътрудничество. Ще продължим да работим заедно с компанията.','Име Фамилия','Длъжност, Компания АД'),('Качество и кратък срок благодарение на широката оценителска мрежа в цялата страна.','Име Фамилия','Компания ЕАД')]},
 'en':{'eyebrow':'20 years in the market','h1':'Independent <em>expert valuations</em> of assets in Bulgaria',
   'lead':'Market valuations of real estate, businesses, machinery and agricultural land — delivered quickly, precisely and in line with international standards.',
   'cta1':'Request a Valuation','cta2':'View Pricing',
   'cr1':'<b>CIAB</b>&nbsp;registered','cr2':'Court expert','cr3':'Bank approved','cr4':'Sofia & region',
   'vc_aria':'Sample certified apartment valuation','vc_badge':'CERTIFIED VALUATION',
   'vc_title':'Apartment valuation','vc_sub':'Sofia · 98 m² · 2025',
   'vc_r1':'Method','vc_v1':'Market approach','vc_r2':'Condition','vc_v2':'Completed','vc_r3':'Turnaround','vc_v3':'3–5 days','vc_val':'Market value',
   'stats':[('20','+','years of experience'),('15000','+','valuations completed'),('100','+','appraisers in the network'),('28','','regions covered')],
   'sv_eye':'Services','sv_h':'What We Value','sv_p':'A full range of valuation services for individuals, businesses and institutions.',
   'more':'Learn more →',
   'cards':[('home','Real Estate','Apartments, houses, offices, commercial and industrial properties.','ocenki-nedvizhimi-imoti.html'),
            ('chart','Business Valuation','Valuation of enterprises, shares and equity instruments.','ocenki-biznes.html'),
            ('cog','Machinery & Equipment','Production equipment, vehicles and inventory.','ocenki-mashini.html'),
            ('bulb','Intangible Assets','Trademarks, patents, know-how and goodwill.','ocenki-nematerialni.html'),
            ('sprout','Agricultural Land','Arable land, permanent crops, plots and parcels.','ocenki-zemedelski-zemi.html'),
            ('clipboard','Additional Services','Consulting, analyses and expert opinions.','ocenki-dopalvashti.html')],
   'pr_eye':'Process','pr_h':'How a valuation works',
   'steps':[('Enquiry','You send us a description of the asset by phone or email.'),('Quote & contract','You receive a firm price and timeline within 24 hours.'),('Inspection','Our appraiser inspects the site and collects the required data.'),('Report','You receive the completed expert report within the agreed deadline.')],
   'cta_h':'Ready to request a valuation?','cta_p':'Contact us for a free consultation and an individual quote.',
   'ts_eye':'Clients','ts_h':'What they say about us',
   'quotes':[('Extremely satisfied with the fast and precise valuation. The team exceeded our expectations for professionalism.','Name Surname','Position, Company Ltd'),('We are grateful for the productive cooperation and will continue to work together.','Name Surname','Position, Company JSC'),('Quality and short turnaround thanks to the broad appraiser network across the country.','Name Surname','Company Plc')]},
}
HOMETITLE={'bg':('Valoris Asset – Експертни пазарни оценки в България','Независими пазарни оценки на недвижими имоти, бизнес, машини и земеделска земя. Над 20 години опит и национална оценителска мрежа.'),
           'en':('Valoris Asset – Expert market valuations in Bulgaria','Independent market valuations of real estate, businesses, machinery and agricultural land. Over 20 years of experience and a nationwide network.')}

# ---------- SERVICE PAGES ----------
SVC_CHROME={'bg':{'eye':'Услуги','desc_p':'Тук опишете подробно услугата: за кого е предназначена, в какви случаи се изисква оценка, какви документи са необходими и какъв е резултатът. Заменете този текст с вашето реално съдържание.',
   'when_h':'Кога е необходима тази оценка','when':['Покупко-продажба или замяна на активи','Банково кредитиране и обезпечения','Счетоводни и данъчни цели','Съдебни и нотариални производства','Апортни вноски и преобразуване на дружества'],
   'incl_h':'Какво включва услугата','meth_h':'Методология','meth_p':'Прилагаме международно признатите подходи — пазарен, разходен и приходен — съобразно вида на актива и целта на оценката. Всеки доклад е изготвен от сертифициран оценител.',
   'as_h':'Заяви оценка','as_p':'Индивидуална оферта в рамките на 24 часа.','as_btn':'Запитване','as_price':'Виж ценоразписа',
   'cta_h':'Имате нужда от тази услуга?','cta_p':'Изпратете ни описание на обекта и ще получите оферта бързо.','cta1':'Заяви оценка','cta2':'Цени'},
 'en':{'eye':'Services','desc_p':'Describe the service in detail here: who it is for, when a valuation is required, what documents are needed and what the deliverable is. Replace this text with your real content.',
   'when_h':'When this valuation is needed','when':['Purchase, sale or exchange of assets','Bank lending and collateral','Accounting and tax purposes','Court and notary proceedings','In-kind contributions and company restructuring'],
   'incl_h':'What the service includes','meth_h':'Methodology','meth_p':'We apply the internationally recognised approaches — market, cost and income — according to the type of asset and the purpose of the valuation. Every report is prepared by a certified appraiser.',
   'as_h':'Request a valuation','as_p':'An individual quote within 24 hours.','as_btn':'Enquiry','as_price':'View pricing',
   'cta_h':'Need this service?','cta_p':"Send us a description of the asset and you'll get a quote quickly.",'cta1':'Request a Valuation','cta2':'Pricing'}}

SERVICES={  # file: (icon, {lang:(title,desc,h1,lead,[ (ft,fd)x4 ])})
 'ocenki-nedvizhimi-imoti.html':('home',{
   'bg':('Оценка на недвижими имоти – Valoris Asset','Пазарни оценки на жилищни, офис, търговски и индустриални имоти в цялата страна.','Оценка на недвижими имоти','Пазарни оценки на жилищни, офис, търговски и индустриални имоти в цялата страна.',[('Жилищни имоти','Апартаменти, къщи, мезонети и ваканционни имоти.'),('Търговски имоти','Магазини, ресторанти, складове и офис площи.'),('Индустриални имоти','Производствени бази, цехове и логистични центрове.'),('Терени','УПИ, поземлени имоти и парцели.')]),
   'en':('Real Estate Valuation – Valoris Asset','Market valuations of residential, office, retail and industrial properties across the country.','Real Estate Valuation','Market valuations of residential, office, retail and industrial properties across the country.',[('Residential','Apartments, houses, maisonettes and holiday homes.'),('Commercial','Shops, restaurants, warehouses and office space.'),('Industrial','Production sites, workshops and logistics centres.'),('Land','Regulated plots, land parcels and lots.')])}),
 'ocenki-biznes.html':('chart',{
   'bg':('Бизнес оценки – Valoris Asset','Оценка на цели предприятия, дялове, акции и капиталови инструменти.','Бизнес оценки','Оценка на цели предприятия, дялове, акции и капиталови инструменти.',[('Оценка на предприятия','Справедлива стойност на действащ бизнес.'),('Дялове и акции','Миноритарни и мажоритарни пакети, опции.'),('Сделки M&A','Придобивания, сливания и продажби.'),('Финансово отчитане','Оценки за целите на МСФО.')]),
   'en':('Business Valuation – Valoris Asset','Valuation of whole enterprises, shares, stock and equity instruments.','Business Valuation','Valuation of whole enterprises, shares, stock and equity instruments.',[('Enterprise valuation','Fair value of a going concern.'),('Shares & stock','Minority and majority stakes, options.'),('M&A deals','Acquisitions, mergers and disposals.'),('Financial reporting','Valuations for IFRS purposes.')])}),
 'ocenki-mashini.html':('cog',{
   'bg':('Оценка на машини и съоръжения – Valoris Asset','Оценка на производствено оборудване, транспортни средства и инвентар.','Оценка на машини и съоръжения','Оценка на производствено оборудване, транспортни средства и инвентар.',[('Производствени машини','Самостоятелни машини и поточни линии.'),('Транспортни средства','Леки, товарни автомобили и техника.'),('Селскостопанска техника','Трактори, комбайни и инвентар.'),('Оборудване','Компютърна техника, обзавеждане, запаси.')]),
   'en':('Machinery & Equipment Valuation – Valoris Asset','Valuation of production equipment, vehicles and inventory.','Machinery & Equipment Valuation','Valuation of production equipment, vehicles and inventory.',[('Production machines','Standalone machines and production lines.'),('Vehicles','Cars, trucks and specialised equipment.'),('Agricultural machinery','Tractors, combines and implements.'),('Equipment','Computers, furnishings and stock.')])}),
 'ocenki-nematerialni.html':('bulb',{
   'bg':('Оценка на нематериални активи – Valoris Asset','Оценка на търговски марки, патенти, ноу-хау, лицензи и репутация.','Оценка на нематериални активи','Оценка на търговски марки, патенти, ноу-хау, лицензи и репутация.',[('Търговски марки','Стойност на бранд и регистрирани марки.'),('Патенти','Интелектуална собственост и технологии.'),('Ноу-хау и лицензи','Договори, права на ползване, франчайз.'),('Репутация (Goodwill)','Превишение над нетните активи.')]),
   'en':('Intangible Asset Valuation – Valoris Asset','Valuation of trademarks, patents, know-how, licences and goodwill.','Intangible Asset Valuation','Valuation of trademarks, patents, know-how, licences and goodwill.',[('Trademarks','Brand value and registered marks.'),('Patents','Intellectual property and technologies.'),('Know-how & licences','Contracts, usage rights, franchising.'),('Goodwill','Excess over net tangible assets.')])}),
 'ocenki-zemedelski-zemi.html':('sprout',{
   'bg':('Оценка на земеделски земи – Valoris Asset','Оценка на ниви, трайни насаждения, пасища и поземлени имоти.','Оценка на земеделски земи','Оценка на ниви, трайни насаждения, пасища и поземлени имоти.',[('Обработваеми земи','Ниви и земеделски парцели.'),('Трайни насаждения','Лозя, овощни градини и гори.'),('Пасища и ливади','Постоянно затревени площи.'),('Поземлени имоти','ПИ и УПИ в различни територии.')]),
   'en':('Agricultural Land Valuation – Valoris Asset','Valuation of arable land, permanent crops, pastures and plots.','Agricultural Land Valuation','Valuation of arable land, permanent crops, pastures and plots.',[('Arable land','Fields and agricultural parcels.'),('Permanent crops','Vineyards, orchards and forests.'),('Pastures & meadows','Permanently grassed areas.'),('Land plots','Parcels and regulated plots in various zones.')])}),
 'ocenki-dopalvashti.html':('clipboard',{
   'bg':('Допълващи услуги – Valoris Asset','Консултации, анализи, експертни становища и съдебни експертизи.','Допълващи професионални услуги','Консултации, анализи, експертни становища и съдебни експертизи.',[('Инвестиционни анализи','Доходност и осъществимост на проекти.'),('Експертни становища','Писмени становища по казуси.'),('Съдебни експертизи','Оценки за съдебни производства.'),('Консултации','Професионални консултации.')]),
   'en':('Additional Services – Valoris Asset','Consulting, analyses, expert opinions and court expertise.','Additional Professional Services','Consulting, analyses, expert opinions and court expertise.',[('Investment analyses','Yield and feasibility of projects.'),('Expert opinions','Written opinions on specific cases.'),('Court expertise','Valuations for court proceedings.'),('Consulting','Professional consulting.')])}),
}
def service_body(lang, ic_name, h1, lead, feats):
    c=SVC_CHROME[lang]
    cards="".join(f'<div class="card reveal"><h3>{t}</h3><p>{d}</p></div>' for t,d in [(x["title"],x["desc"]) for x in feats])
    whens="".join(f'<li>{w}</li>' for w in c['when'])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal">
  <span class="eyebrow">{c["eye"]}</span><div class="hero-ic">{icon(ic_name)}</div><h1>{h1}</h1><p>{lead}</p>
</div></div></section>
<section class="section"><div class="wrap split">
  <div class="prose reveal">
    <p class="lead">{lead}</p>
    <p>{c["desc_p"]}</p>
    <h2>{c["when_h"]}</h2><ul>{whens}</ul>
    <h2>{c["incl_h"]}</h2>
    <div class="grid grid-2" style="margin-top:1rem;">{cards}</div>
    <h2>{c["meth_h"]}</h2><p>{c["meth_p"]}</p>
  </div>
  <aside class="aside reveal">
    <h4>{c["as_h"]}</h4><p style="color:var(--muted);font-size:.9rem;">{c["as_p"]}</p>
    <a href="kontakti.html" class="btn btn-accent" style="width:100%;margin-top:1rem;">{c["as_btn"]}</a>
    <ul>
      <li>{icon_inline('phone')} <a href="tel:{PHONE_L}">{PHONE_D}</a></li>
      <li>{icon_inline('mail')} <a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{icon_inline('euro')} <a href="ceni.html">{c["as_price"]}</a></li>
    </ul>
  </aside>
</div>
<div class="wrap" style="margin-top:3rem;"><div class="cta reveal">
  <div><h3>{c["cta_h"]}</h3><p>{c["cta_p"]}</p></div>
  <div class="actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{c["cta1"]}</a><a href="ceni.html" class="btn btn-ghost-light btn-lg">{c["cta2"]}</a></div>
</div></div>
</section></main>'''

print("page content part 1 loaded")

# ---------- PRICING (ceni) ----------
CENI={
 'bg':{'eye':'Ценоразпис','h1':'Цени за <em>експертни оценки</em>','lead':'Прозрачни и конкурентни цени за всички видове пазарни оценки. Без скрити такси.',
   'th':['Вид имот / актив','Такса (EUR с ДДС)','Такса (BGN с ДДС)','Срок (дни)'],'th_asset':'Вид оценяван актив',
   's1':'Оценка на недвижим имот','s2':'Сгради с прилежаща земя','s3':'Машини и съоръжения','s4':'Земеделска земя',
   'neg':'по договаряне','minw':'минимум','min':'мин.','lv':'лв.','express':'ЕКСПРЕСНА','expressd':'Оценка (до 2 дни)','exprate':'+50% от основното възнаграждение','upto2':'до 2',
   'foot':'* Цените са преизчислени по курс 1 EUR = 1,95583 BGN и закръглени до два знака. За нестандартни обекти цената е по индивидуално договаряне.',
   'cta_h':'Нужна ви е индивидуална оферта?','cta_p':'Изпратете ни списък с обектите и техните характеристики — отговаряме до 24 часа.','cta1':'Изпратете запитване',
   'r':{'a1':'Апартамент до 150 м² – завършено','a2':'Апартамент до 150 м² – незавършено','gar+':'Доплащане за гараж или паркомясто','gar':'Самостоятелен гараж / паркомясто','a3':'Апартамент над 150 м²; мезонет – завършено','a4':'Апартамент над 150 м²; мезонет – незавършено','off':'Офис самостоятелен – до 200 м²','add200':'Доплащане за всеки допълнителни 200 м²','shop':'Търговски обект до 200 м²','house1':'Едноетажна къща със ЗП до 150 м²','floor+':'Доплащане за всеки допълнителен етаж/постройка','house2':'Къща над 150 м² или „луксозен имот"','car':'Лек автомобил','truck':'Товарен автомобил','agm':'Селскостопанска машина','impl':'Прикачен инвентар','prod':'Производствена машина – самостоятелна','line':'Поточна линия','comp':'Компютърна техника, материални запаси','zem':'Земеделска земя – поземлен имот (1 бр.)','parc+':'Доплащане за всеки допълнителен парцел','trk':'Земеделска земя с трайни насаждения','vac':'Празен терен (УПИ, ПИ) без разрешение','upi':'УПИ с разрешение за строеж'}},
 'en':{'eye':'Pricing','h1':'Prices for <em>expert valuations</em>','lead':'Transparent and competitive prices for all types of market valuations. No hidden fees.',
   'th':['Property / asset type','Fee (EUR incl. VAT)','Fee (BGN incl. VAT)','Time (days)'],'th_asset':'Asset type',
   's1':'Real estate valuation','s2':'Buildings with adjoining land','s3':'Machinery & equipment','s4':'Agricultural land',
   'neg':'by agreement','minw':'minimum','min':'min.','lv':'BGN','express':'EXPRESS','expressd':'valuation (up to 2 days)','exprate':'+50% of the base fee','upto2':'up to 2',
   'foot':'* Prices are converted at the rate 1 EUR = 1.95583 BGN and rounded to two decimals. Non-standard assets are priced by individual agreement.',
   'cta_h':'Need an individual quote?','cta_p':'Send us a list of the assets and their characteristics — we reply within 24 hours.','cta1':'Send an enquiry',
   'r':{'a1':'Apartment up to 150 m² – completed','a2':'Apartment up to 150 m² – unfinished','gar+':'Surcharge for garage or parking space','gar':'Standalone garage / parking space','a3':'Apartment over 150 m²; maisonette – completed','a4':'Apartment over 150 m²; maisonette – unfinished','off':'Standalone office – up to 200 m²','add200':'Surcharge per additional 200 m²','shop':'Retail unit up to 200 m²','house1':'Single-storey house, built-up area up to 150 m²','floor+':'Surcharge per additional floor/building','house2':'House over 150 m² or "luxury property"','car':'Passenger car','truck':'Truck','agm':'Agricultural machine','impl':'Towed implement','prod':'Production machine – standalone','line':'Production line','comp':'Computer equipment, inventory','zem':'Agricultural land – plot (1 pc.)','parc+':'Surcharge per additional parcel','trk':'Agricultural land with permanent crops','vac':'Vacant plot (regulated/land) without permit','upi':'Regulated plot with building permit'}},
}
def bgn(lang, v):  # v like "293,37" bg -> "BGN 293.37" en
    return (v+' лв.') if lang=='bg' else ('BGN '+v.replace(',','.'))
def neg_eur(lang, mn):
    c=CENI[lang]; return f'<span class="neg">{c["neg"]}</span><span class="min">{c["minw"]} €{mn}</span>'
def min_bgn(lang, v):
    c=CENI[lang]; return f'<span class="min">{c["min"]} {bgn(lang,v)}</span>'
def ceni_body(lang):
    c=CENI[lang]; th=c['th']; tb=c['tables']
    def negspan(): return f'<span class="neg">{c["neg"]}</span>'
    def cell(text,neg,mn):
        out = (negspan() if neg else text)
        if mn: out += f'<span class="min">{mn}</span>'
        return out
    def row(rw):
        cls=rw.get('type','b')
        nm=rw['name']
        nm = f'<strong>{nm}</strong>' if cls=='b' else nm
        eur=cell(rw.get('eur',''),rw.get('eur_neg'),rw.get('eur_min',''))
        bg=cell(rw.get('bgn',''),rw.get('bgn_neg'),rw.get('bgn_min',''))
        return f'<tr class="{cls}"><td>{nm}</td><td class="price-eur">{eur}</td><td class="price-bgn">{bg}</td><td class="days">{rw.get("days","")}</td></tr>'
    head4=f'<thead><tr><th>{th[0]}</th><th class="c">{th[1]}</th><th class="c">{th[2]}</th><th class="c">{th[3]}</th></tr></thead>'
    head4a=f'<thead><tr><th>{c["th_asset"]}</th><th class="c">{th[1]}</th><th class="c">{th[2]}</th><th class="c">{th[3]}</th></tr></thead>'
    express=f'<tr><td><span class="express">{c["express"]}</span> {c["expressd"]}</td><td class="price-eur" colspan="2" style="text-align:center;color:var(--accent);font-size:.85rem;">{c["exprate"]}</td><td class="days">{c["upto2"]}</td></tr>'
    t1='<div class="table-wrap reveal"><table>'+head4+'<tbody>'+''.join(row(r) for r in tb['realestate'])+express+'</tbody></table></div>'
    t2='<div class="table-wrap reveal"><table>'+head4+'<tbody>'+''.join(row(r) for r in tb['buildings'])+'</tbody></table></div>'
    t3='<div class="table-wrap reveal"><table>'+head4a+'<tbody>'+''.join(row(r) for r in tb['machinery'])+'</tbody></table></div>'
    t4='<div class="table-wrap reveal"><table>'+head4a+'<tbody>'+''.join(row(r) for r in tb['agri'])+'</tbody></table></div>'
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal">
  <span class="eyebrow">{c['eye']}</span><h1>{c['h1']}</h1><p>{c['lead']}</p>
</div></div></section>
<section class="section"><div class="wrap">
  <div class="row-head reveal"><span class="row-badge">01</span><h2>{c['s1']}</h2><div class="row-line"></div></div>{t1}
  <div class="row-head reveal" style="margin-top:2.4rem;"><span class="row-badge">02</span><h2>{c['s2']}</h2><div class="row-line"></div></div>{t2}
  <p class="footnote reveal">{c['foot']}</p>
  <div class="row-head reveal"><span class="row-badge">03</span><h2>{c['s3']}</h2><div class="row-line"></div></div>{t3}
  <div class="row-head reveal"><span class="row-badge">04</span><h2>{c['s4']}</h2><div class="row-line"></div></div>{t4}
  <div class="cta reveal" style="margin-top:3rem;"><div><h3>{c['cta_h']}</h3><p>{c['cta_p']}</p></div>
  <div class="actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{c['cta1']}</a><a href="tel:{PHONE_L}" class="btn btn-ghost-light btn-lg">{PHONE_D}</a></div></div>
</div></section></main>'''
CENITITLE={'bg':('Цени за оценки – Valoris Asset','Прозрачен ценоразпис за оценки на недвижими имоти, машини, съоръжения и земеделска земя.'),
           'en':('Pricing – Valoris Asset','Transparent price list for valuations of real estate, machinery, equipment and agricultural land.')}
print("ceni loaded")

def stat_cells(stats):
    return "".join(f'<div class="stat"><div class="n" data-target="{x["value"]}"{(" data-suffix=\""+x["suffix"]+"\"") if x["suffix"] else ""}>0</div><div class="l">{x["label"]}</div></div>' for x in stats)

# ---------- ABOUT ----------
ABOUT={
 'bg':{'title':('За нас – Valoris Asset','Запознайте се с Valoris Asset — независим оценител с над 20 години опит на българския пазар.'),'eye':'За нас','h1':'Кои сме ние','hp':'Над 20 години изграждаме доверие като независим оценител на българския пазар.',
   'lead':'Valoris Asset е сред водещите оценителски компании в България с над 20 години опит и национална мрежа от сертифицирани оценители.','p':'Заменете този текст с историята на вашата компания — кога е основана, основните етапи в развитието, ценностите и какво ви отличава.',
   'mh':'Нашата мисия','mp':'Да предоставяме независими, обективни и навременни оценки, на които клиентите ни могат да разчитат при важни финансови решения.','wh':'Защо да изберете нас',
   'why':[('Опит','над две десетилетия и хиляди изготвени доклада.'),('Покритие','оценители във всички региони на страната.'),('Бързина','стандартен срок 3–5 дни, експресни до 2 дни.'),('Качество','доклади по международните стандарти.')],
   'stats':[('20','+','години опит'),('15000','+','изготвени оценки'),('100','+','оценители'),('28','','области')]},
 'en':{'title':('About – Valoris Asset','Meet Valoris Asset — an independent appraiser with over 20 years of experience on the Bulgarian market.'),'eye':'About','h1':'Who We Are','hp':'For over 20 years we have built trust as an independent appraiser on the Bulgarian market.',
   'lead':'Valoris Asset is among the leading appraisal companies in Bulgaria, with over 20 years of experience and a nationwide network of certified appraisers.','p':"Replace this text with your company's story — when it was founded, key milestones, your values and what sets you apart.",
   'mh':'Our mission','mp':'To deliver independent, objective and timely valuations our clients can rely on for important financial decisions.','wh':'Why choose us',
   'why':[('Experience','over two decades and thousands of reports delivered.'),('Coverage','appraisers in every region of the country.'),('Speed','standard turnaround 3–5 days, express up to 2 days.'),('Quality','reports compliant with international standards.')],
   'stats':[('20','+','years of experience'),('15000','+','valuations completed'),('100','+','appraisers'),('28','','regions')]},
}
def about_body(lang):
    a=ABOUT[lang]
    why="".join(f'<li><strong>{h}</strong> — {d}</li>' for h,d in [(x["head"],x["desc"]) for x in a['why']])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{a['eye']}</span><h1>{a['h1']}</h1><p>{a['hp']}</p></div></div></section>
<section class="section"><div class="wrap-narrow prose reveal">
  <p class="lead">{a['lead']}</p><p>{a['p']}</p>
  <h2>{a['mh']}</h2><p>{a['mp']}</p>
  <h2>{a['wh']}</h2><ul>{why}</ul>
</div></div></section>
<section class="section alt"><div class="wrap stats reveal">{stat_cells(a['stats'])}</div></section>
</main>'''

# ---------- METHODOLOGY ----------
METH={
 'bg':{'title':('Методология – Valoris Asset','Методология на оценяване по международните стандарти (IVS): пазарен, разходен и приходен подход.'),'eye':'За нас','h1':'Методология на оценяване','hp':'Прилагаме международно признатите подходи и стандарти за оценяване.',
   'lead':'Всяка оценка се изготвя в съответствие с Международните стандарти за оценяване (IVS) и българското законодателство.','ah':'Трите основни подхода',
   'app':[('Пазарен подход','Стойността се определя чрез сравнение с реализирани сделки за сходни активи.'),('Разходен подход','Стойността се базира на разходите за възстановяване, намалени с амортизацията.'),('Приходен подход','Стойността се извежда от способността на актива да генерира бъдещи парични потоци.')],
   'sh':'Етапи на работа','steps':[('Дефиниране на задачата','Уточняване на обекта, целта и базата на оценката.'),('Събиране на данни','Оглед, документи и пазарна информация.'),('Анализ','Прилагане на подходящите подходи и методи.'),('Заключение и доклад','Изготвяне на писмен експертен доклад.')]},
 'en':{'title':('Methodology – Valoris Asset','Valuation methodology under the International Valuation Standards (IVS): market, cost and income approaches.'),'eye':'About','h1':'Valuation Methodology','hp':'We apply internationally recognised valuation approaches and standards.',
   'lead':'Every valuation is prepared in accordance with the International Valuation Standards (IVS) and Bulgarian legislation.','ah':'The three core approaches',
   'app':[('Market approach','Value is determined by comparison with completed transactions for similar assets.'),('Cost approach','Value is based on replacement cost less accumulated depreciation.'),('Income approach',"Value is derived from the asset's ability to generate future cash flows.")],
   'sh':'Workflow stages','steps':[('Defining the engagement','Clarifying the asset, purpose and basis of value.'),('Data collection','Inspection, documents and market information.'),('Analysis','Applying the appropriate approaches and methods.'),('Conclusion & report','Preparing a written expert report.')]},
}
def meth_body(lang):
    m=METH[lang]
    apps="".join(f'<h3>{h}</h3><p>{d}</p>' for h,d in [(x["title"],x["desc"]) for x in m['app']])
    steps="".join(f'<div class="step reveal"><div class="sn">{i+1}</div><div><h3>{h}</h3><p>{d}</p></div></div>' for i,(h,d) in enumerate([(x["title"],x["desc"]) for x in m['steps']]))
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{m['eye']}</span><h1>{m['h1']}</h1><p>{m['hp']}</p></div></div></section>
<section class="section"><div class="wrap-narrow prose reveal"><p class="lead">{m['lead']}</p><h2>{m['ah']}</h2>{apps}</div></section>
<section class="section alt"><div class="wrap-narrow"><div class="section-head reveal"><h2>{m['sh']}</h2></div><div class="steps">{steps}</div></div></section>
</main>'''

# ---------- NETWORK ----------
NET={
 'bg':{'title':('Оценителска мрежа – Valoris Asset','Национална мрежа от сертифицирани оценители с покритие във всички области на България.'),'eye':'За нас','h1':'Оценителска мрежа','hp':'Сертифицирани оценители във всички региони на страната.',
   'lead':'Нашата национална мрежа от независими оценители ни позволява да извършваме огледи и оценки в кратки срокове във всяка точка на България.','p':'Заменете този текст с описание на вашата мрежа — брой оценители, специализации, регионално покритие и контрол на качеството.',
   'rh':'Регионално покритие','regions':['София','Пловдив','Варна','Бургас','Русе','Стара Загора','Плевен','Велико Търново','Благоевград','Хасково','Шумен','Добрич'],
   'cta_h':'Искате да станете част от мрежата?','cta_p':'Търсим сертифицирани оценители за разширяване на екипа.','cta1':'Кандидатствай'},
 'en':{'title':('Appraiser Network – Valoris Asset','A nationwide network of certified appraisers covering every region of Bulgaria.'),'eye':'About','h1':'Appraiser Network','hp':'Certified appraisers in every region of the country.',
   'lead':'Our nationwide network of independent appraisers lets us carry out inspections and valuations quickly anywhere in Bulgaria.','p':'Replace this text with a description of your network — number of appraisers, specialisations, regional coverage and quality control.',
   'rh':'Regional coverage','regions':['Sofia','Plovdiv','Varna','Burgas','Ruse','Stara Zagora','Pleven','Veliko Tarnovo','Blagoevgrad','Haskovo','Shumen','Dobrich'],
   'cta_h':'Want to join the network?','cta_p':"We're looking for certified appraisers to expand the team.",'cta1':'Apply'},
}
def net_body(lang):
    n=NET[lang]; tiles="".join(f'<div class="tile">{r}</div>' for r in n['regions'])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{n['eye']}</span><h1>{n['h1']}</h1><p>{n['hp']}</p></div></div></section>
<section class="section"><div class="wrap-narrow prose reveal"><p class="lead">{n['lead']}</p><p>{n['p']}</p></div></section>
<section class="section alt"><div class="wrap"><div class="section-head reveal"><h2>{n['rh']}</h2></div><div class="wall reveal">{tiles}</div>
<div class="cta reveal" style="margin-top:2.5rem;"><div><h3>{n['cta_h']}</h3><p>{n['cta_p']}</p></div><div class="actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{n['cta1']}</a></div></div>
</div></section></main>'''

# ---------- CLIENTS ----------
CLI={
 'bg':{'title':('Клиенти – Valoris Asset','Банки, корпоративни клиенти и институции се доверяват на нашите експертни оценки.'),'eye':'Клиенти','h1':'Нашите клиенти','hp':'Доверието на банки, корпорации и институции е нашето най-голямо постижение.',
   'b1':'Банки','b1h':'Банкови институции','b2':'Бизнес','b2h':'Корпоративни клиенти','b3':'Държава','b3h':'Институции',
   'banks':['Банка 1','Банка 2','Банка 3','Банка 4'],'corp':['Компания A','Компания B','Компания C','Компания D','Компания E','Компания F'],'inst':['Институция 1','Институция 2','Институция 3'],
   'reh':'Референции','reh2':'Какво казват клиентите ни',
   'quotes':[('Изключително задоволни от професионалната работа, извършена с високо качество и в кратък срок.','Име Фамилия','Длъжност, Компания ООД'),('Благодарни сме за ползотворното сътрудничество и ще продължим да работим заедно.','Име Фамилия','Длъжност, Компания АД'),('Екипът извършва всяка експертна оценка с висок професионализъм и в договорения срок.','Име Фамилия','Компания ЕАД'),('Компанията работи на най-високо ниво от гледна точка на професионализъм и коректност.','Име Фамилия','Длъжност, Компания ООД')]},
 'en':{'title':('Clients – Valoris Asset','Banks, corporate clients and institutions trust our expert valuations.'),'eye':'Clients','h1':'Our Clients','hp':'The trust of banks, corporations and institutions is our greatest achievement.',
   'b1':'Banks','b1h':'Banking institutions','b2':'Business','b2h':'Corporate clients','b3':'Public','b3h':'Institutions',
   'banks':['Bank 1','Bank 2','Bank 3','Bank 4'],'corp':['Company A','Company B','Company C','Company D','Company E','Company F'],'inst':['Institution 1','Institution 2','Institution 3'],
   'reh':'References','reh2':'What our clients say',
   'quotes':[('Extremely satisfied with the professional work, delivered to a high standard and on a short timeline.','Name Surname','Position, Company Ltd'),('We are grateful for the productive cooperation and will continue to work together.','Name Surname','Position, Company JSC'),('The team carries out every expert valuation with high professionalism and within the agreed deadline.','Name Surname','Company Plc'),('The company operates at the highest level in terms of professionalism and integrity.','Name Surname','Position, Company Ltd')]},
}
def cli_body(lang):
    c=CLI[lang]
    def wall(items): return "".join(f'<div class="tile">{i}</div>' for i in items)
    quotes="".join(f'<div class="quote reveal"><p>{q}</p><div class="by">{n} <span>– {r}</span></div></div>' for q,n,r in [(x["text"],x["name"],x["role"]) for x in c['quotes']])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{c['eye']}</span><h1>{c['h1']}</h1><p>{c['hp']}</p></div></div></section>
<section class="section"><div class="wrap">
  <div class="row-head reveal" id="bank"><span class="row-badge">{c['b1']}</span><h2>{c['b1h']}</h2><div class="row-line"></div></div><div class="wall reveal">{wall(c['banks'])}</div>
  <div class="row-head reveal" id="corporate" style="margin-top:2.4rem;"><span class="row-badge">{c['b2']}</span><h2>{c['b2h']}</h2><div class="row-line"></div></div><div class="wall reveal">{wall(c['corp'])}</div>
  <div class="row-head reveal" id="institution" style="margin-top:2.4rem;"><span class="row-badge">{c['b3']}</span><h2>{c['b3h']}</h2><div class="row-line"></div></div><div class="wall reveal">{wall(c['inst'])}</div>
</div></section>
<section class="section alt"><div class="wrap" id="references"><div class="section-head reveal"><span class="eyebrow">{c['reh']}</span><h2>{c['reh2']}</h2></div><div class="grid grid-2">{quotes}</div></div></section>
</main>'''

# ---------- BLOG ----------
BLOG={
 'bg':{'title':('Блог – Valoris Asset','Новини, анализи и полезни статии за пазарните оценки в България.'),'eye':'Блог','h1':'Актуално','hp':'Новини, анализи и полезни статии от света на оценяването.',
   'posts':[('clipboard','15 ЯНУАРИ 2025','Как се определя пазарната стойност на жилище','Основните фактори, които влияят върху оценката на апартамент или къща.'),('chart','02 ФЕВРУАРИ 2025','Кога е необходима бизнес оценка','Типичните ситуации, в които компаниите се нуждаят от професионална оценка.'),('landmark','20 МАРТ 2025','Оценка за банков кредит — какво да очаквате','Процесът при изготвяне на оценка за ипотечно кредитиране.'),('sprout','05 АПРИЛ 2025','Особености при оценка на земеделска земя','Кои фактори определят стойността на нивите и насажденията.'),('cog','18 МАЙ 2025','Амортизация при оценка на машини','Как се отчита износването на производственото оборудване.'),('euro','01 ЮНИ 2025','Преминаване към еврото и оценките','Какво се променя в ценоразписа след въвеждането на еврото.')]},
 'en':{'title':('Blog – Valoris Asset','News, analyses and useful articles on market valuations in Bulgaria.'),'eye':'Blog','h1':'News','hp':'News, analyses and useful articles from the world of valuation.',
   'posts':[('clipboard','15 JANUARY 2025',"How a home's market value is determined",'The main factors that influence the valuation of an apartment or house.'),('chart','02 FEBRUARY 2025','When you need a business valuation','Typical situations where companies need a professional valuation.'),('landmark','20 MARCH 2025','Valuation for a bank loan — what to expect','The process of preparing a valuation for mortgage lending.'),('sprout','05 APRIL 2025','Specifics of valuing agricultural land','Which factors determine the value of fields and crops.'),('cog','18 MAY 2025','Depreciation in machinery valuation','How wear of production equipment is accounted for.'),('euro','01 JUNE 2025','The euro changeover and valuations','What changes in the price list after the euro is introduced.')]},
}
def blog_body(lang):
    b=BLOG[lang]
    posts="".join(f'<a href="#" class="post reveal"><div class="thumb">{icon(ic)}</div><div class="pb"><div class="date">{d}</div><h3>{ti}</h3><p>{e}</p></div></a>' for ic,d,ti,e in [(x["icon"],x["date"],x["title"],x["excerpt"]) for x in b['posts']])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{b['eye']}</span><h1>{b['h1']}</h1><p>{b['hp']}</p></div></div></section>
<section class="section"><div class="wrap"><div class="grid grid-3">{posts}</div></div></section></main>'''

# ---------- FAQ ----------
FAQ={
 'bg':{'title':('Често задавани въпроси – Valoris Asset','Отговори на често задавани въпроси за процеса, цените и валидността на оценките.'),'eye':'Помощ','h1':'Често задавани въпроси','hp':'Отговори на най-честите въпроси за нашите услуги.',
   'q':[('Какъв е процесът на изготвяне на оценка?','След запитване изготвяме оферта, извършваме оглед, анализираме данните и предоставяме готовия доклад в договорения срок.'),('Как протича огледът на обекта?','Наш оценител посещава обекта в уговорено време, прави снимки и заснема необходимите характеристики и размери.'),('Каква е цената на оценката?','Зависи от вида и характеристиките на актива. Вижте ценоразписа или се свържете с нас за оферта.'),('Каква е валидността на оценката?','Обикновено 6 месеца, но срокът може да варира според целта и изискванията на институцията.'),('Може ли една оценка да послужи на няколко места?','В повечето случаи да, ако целта и базата ѝ съответстват на изискванията на съответната институция.'),('Каква методология използвате?','Пазарен, разходен и приходен подход съобразно актива и целта, по международните стандарти.')],
   'cta_h':'Не намерихте отговор?','cta_p':'Свържете се с нас и ще ви помогнем.','cta1':'Контакти'},
 'en':{'title':('FAQ – Valoris Asset','Answers to frequently asked questions about the process, pricing and validity of valuations.'),'eye':'Help','h1':'Frequently Asked Questions','hp':'Answers to the most common questions about our services.',
   'q':[('What is the valuation process?','After your enquiry we prepare a quote, carry out an inspection, analyse the data and deliver the completed report within the agreed deadline.'),('How does the on-site inspection work?','Our appraiser visits the site at an agreed time, takes photos and records the necessary features and dimensions.'),('How much does a valuation cost?','It depends on the type and characteristics of the asset. See our pricing or contact us for a quote.'),('How long is a valuation valid?','Usually 6 months, but this can vary depending on the purpose and the requirements of the institution.'),('Can one valuation be used in several places?','In most cases yes, if its purpose and basis match the requirements of the relevant institution.'),('What methodology do you use?','Market, cost and income approaches according to the asset and purpose, in line with international standards.')],
   'cta_h':"Didn't find an answer?",'cta_p':"Contact us and we'll help.",'cta1':'Contact'},
}
def faq_body(lang):
    f=FAQ[lang]
    items="".join(f'<div class="faq-item"><button class="faq-q">{q}</button><div class="faq-a"><div>{a}</div></div></div>' for q,a in [(x["q"],x["a"]) for x in f['q']])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{f['eye']}</span><h1>{f['h1']}</h1><p>{f['hp']}</p></div></div></section>
<section class="section"><div class="wrap-narrow reveal">{items}
<div class="cta reveal" style="margin-top:2rem;"><div><h3>{f['cta_h']}</h3><p>{f['cta_p']}</p></div><div class="actions"><a href="kontakti.html" class="btn btn-accent btn-lg">{f['cta1']}</a></div></div>
</div></section></main>'''

# ---------- CONTACT ----------
KON={
 'bg':{'title':('Контакти – Valoris Asset','Свържете се с Valoris Asset за безплатна консултация и индивидуална оферта за оценка.'),'eye':'Контакти','h1':'Свържете се с нас','hp':'Готови сме да отговорим на вашите въпроси и да изготвим оферта.',
   'ih':'Информация за контакт','addr':'Адрес','addrv':'гр. София, ул. „Примерна" № 1<br>(заменете с вашия адрес)','ph':'Телефон','em':'Имейл','wh':'Работно време','whv':'Понеделник – Петък: 9:00 – 18:00',
   'fh':'Изпратете запитване','f_name':'Име *','f_namep':'Вашето име','f_email':'Имейл *','f_phone':'Телефон','f_type':'Вид оценка','opts':['Недвижим имот','Бизнес оценка','Машини и съоръжения','Земеделска земя','Друго'],'f_msg':'Съобщение *','f_msgp':'Опишете обекта за оценяване...','f_btn':'Изпрати запитване',
   'e_name':'Моля, въведете вашето име.','e_email':'Моля, въведете валиден имейл.','e_msg':'Моля, въведете съобщение.',
   'note':'* Полетата са задължителни. Формата се валидира в браузъра; за реално изпращане я свържете с вашия сървър или имейл услуга със server-side валидация.'},
 'en':{'title':('Contact – Valoris Asset','Contact Valoris Asset for a free consultation and an individual valuation quote.'),'eye':'Contact','h1':'Get in touch','hp':"We're ready to answer your questions and prepare a quote.",
   'ih':'Contact information','addr':'Address','addrv':'1 Primerna St., Sofia<br>(replace with your address)','ph':'Phone','em':'Email','wh':'Working hours','whv':'Monday – Friday: 9:00 – 18:00',
   'fh':'Send an enquiry','f_name':'Name *','f_namep':'Your name','f_email':'Email *','f_phone':'Phone','f_type':'Valuation type','opts':['Real estate','Business valuation','Machinery & equipment','Agricultural land','Other'],'f_msg':'Message *','f_msgp':'Describe the asset to be valued...','f_btn':'Send enquiry',
   'e_name':'Please enter your name.','e_email':'Please enter a valid email.','e_msg':'Please enter a message.',
   'note':'* Required fields. The form is validated in the browser; to actually send it, connect it to your server or email service with server-side validation.'},
}
def kon_body(lang):
    k=KON[lang]
    opts="".join(f'<option>{o}</option>' for o in k['opts'])
    return f'''<main id="main">
<section class="hero hero-sm"><div class="hero-inner"><div class="reveal"><span class="eyebrow">{k['eye']}</span><h1>{k['h1']}</h1><p>{k['hp']}</p></div></div></section>
<section class="section"><div class="wrap cgrid">
  <div class="reveal">
    <h2 style="font-size:1.4rem;margin-bottom:1.5rem;">{k['ih']}</h2>
    <div class="cinfo"><div class="ci">{icon('pin')}</div><div><h4>{k['addr']}</h4><p>{k['addrv']}</p></div></div>
    <div class="cinfo"><div class="ci">{icon('phone')}</div><div><h4>{k['ph']}</h4><a href="tel:{PHONE_L}">{PHONE_D}</a></div></div>
    <div class="cinfo"><div class="ci">{icon('mail')}</div><div><h4>{k['em']}</h4><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="cinfo"><div class="ci">{icon('clock')}</div><div><h4>{k['wh']}</h4><p>{k['whv']}</p></div></div>
  </div>
  <div class="reveal">
    <h2 style="font-size:1.4rem;margin-bottom:1.5rem;">{k['fh']}</h2>
    <form id="contactForm" novalidate>
      <input type="text" name="company_website" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <div class="field"><label for="f-name">{k['f_name']}</label><input id="f-name" name="name" type="text" data-required placeholder="{k['f_namep']}"><span class="err">{k['e_name']}</span></div>
      <div class="field"><label for="f-email">{k['f_email']}</label><input id="f-email" name="email" type="email" data-required placeholder="example@email.com"><span class="err">{k['e_email']}</span></div>
      <div class="field"><label for="f-phone">{k['f_phone']}</label><input id="f-phone" name="phone" type="tel" placeholder="0888 000 000"></div>
      <div class="field"><label for="f-type">{k['f_type']}</label><select id="f-type" name="type">{opts}</select></div>
      <div class="field"><label for="f-msg">{k['f_msg']}</label><textarea id="f-msg" name="message" rows="4" data-required placeholder="{k['f_msgp']}"></textarea><span class="err">{k['e_msg']}</span></div>
      <button type="submit" class="btn btn-accent btn-lg">{k['f_btn']}</button>
      <div class="form-msg" id="formMsg"></div>
      <p class="form-note">{k['note']}</p>
    </form>
  </div>
</div></section></main>'''

# ---------- 404 ----------
NF={'bg':('Страницата не е намерена – Valoris Asset','404 – страницата не е намерена','Грешка 404','Страницата не е намерена','Възможно е връзката да е остаряла или преместена.','Към началото'),
    'en':('Page not found – Valoris Asset','404 – page not found','Error 404','Page not found','The link may be outdated or moved.','Back to home')}
def nf_body(lang):
    t=NF[lang]
    return f'''<main id="main">
<section class="hero" style="min-height:58vh;display:flex;align-items:center;"><div class="hero-inner" style="grid-template-columns:1fr;text-align:center;"><div class="reveal">
  <span class="eyebrow" style="justify-content:center;">{t['eyebrow']}</span>
  <h1 style="margin:1rem 0;">{t['h1']}</h1>
  <p style="margin:0 auto 1.5rem;">{t['p']}</p>
  <a href="index.html" class="btn btn-accent btn-lg">{t['button']}</a>
</div></div></section>
</main>'''


# ---------------- LOAD EDITABLE CONTENT ----------------
import json as _json, glob as _glob
_data={}
for _fp in sorted(_glob.glob(os.path.join(ROOT,'content','*.json'))):
    _data.update(_json.load(open(_fp,encoding='utf-8')))
SITE=_data['site']; URL=SITE['url']; PHONE_D=SITE['phone_display']; PHONE_L=SITE['phone_link']; EMAIL=SITE['email']; BRAND=SITE['brand']
T=_data['chrome']; HOME=_data['home']; HOMETITLE=_data['home_title']; SVC_CHROME=_data['svc_chrome']
SERVICES=_data['services']; CENI=_data['ceni']; CENITITLE=_data['ceni_title']
ABOUT=_data['about']; METH=_data['methodology']; NET=_data['network']; CLI=_data['clients']
BLOG=_data['blog']; FAQ=_data['faq']; KON=_data['contact']; NF=_data['notfound']
if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT, exist_ok=True)
# =====================================================================
#  BUILD BOTH LANGUAGES
# =====================================================================
for lang in ('bg','en'):
    write(lang,'index.html', doc(lang,'index.html','', HOMETITLE[lang]['title'], HOMETITLE[lang]['desc'], home_body(lang)))
    for sv in SERVICES:
        f=sv['file']; dd=sv[lang]
        write(lang,f, doc(lang,f,'val',dd['title'],dd['desc'], service_body(lang,sv['icon'],dd['h1'],dd['lead'],dd['features'])))
    write(lang,'ceni.html', doc(lang,'ceni.html','val',CENITITLE[lang]['title'], CENITITLE[lang]['desc'], ceni_body(lang)))
    write(lang,'za-nas.html', doc(lang,'za-nas.html','about',ABOUT[lang]['title']['title'], ABOUT[lang]['title']['desc'], about_body(lang)))
    write(lang,'metodologia.html', doc(lang,'metodologia.html','about',METH[lang]['title']['title'], METH[lang]['title']['desc'], meth_body(lang)))
    write(lang,'ocenitelska-mreja.html', doc(lang,'ocenitelska-mreja.html','about',NET[lang]['title']['title'], NET[lang]['title']['desc'], net_body(lang)))
    write(lang,'klienti.html', doc(lang,'klienti.html','clients',CLI[lang]['title']['title'], CLI[lang]['title']['desc'], cli_body(lang)))
    write(lang,'blog.html', doc(lang,'blog.html','blog',BLOG[lang]['title']['title'], BLOG[lang]['title']['desc'], blog_body(lang)))
    write(lang,'vyprosi.html', doc(lang,'vyprosi.html','faq',FAQ[lang]['title']['title'], FAQ[lang]['title']['desc'], faq_body(lang)))
    write(lang,'kontakti.html', doc(lang,'kontakti.html','contact',KON[lang]['title']['title'], KON[lang]['title']['desc'], kon_body(lang)))
    write(lang,'404.html', doc(lang,'index.html','', NF[lang]['title'], NF[lang]['p'], nf_body(lang)))
    print(f"built all pages for: {lang}")
print("DONE")

# ---------------- STATIC ASSETS + ADMIN + SEO FILES ----------------
shutil.copytree(os.path.join(ROOT,'assets'), os.path.join(OUT,'assets'))
if os.path.isdir(os.path.join(ROOT,'admin')):
    shutil.copytree(os.path.join(ROOT,'admin'), os.path.join(OUT,'admin'))
for fn in ('site.webmanifest','.htaccess'):
    p=os.path.join(ROOT,fn)
    if os.path.isfile(p): shutil.copy(p, os.path.join(OUT,fn))
open(os.path.join(OUT,'.nojekyll'),'w').close()
open(os.path.join(OUT,'robots.txt'),'w',encoding='utf-8').write("User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n"%URL)
pages=['index.html','ocenki-nedvizhimi-imoti.html','ocenki-biznes.html','ocenki-mashini.html','ocenki-nematerialni.html','ocenki-zemedelski-zemi.html','ocenki-dopalvashti.html','ceni.html','za-nas.html','metodologia.html','ocenitelska-mreja.html','klienti.html','blog.html','vyprosi.html','kontakti.html']
sm=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for p in pages:
    bg=URL+('/' if p=='index.html' else '/'+p); en=URL+('/en/' if p=='index.html' else '/en/'+p)
    for u in (bg,en):
        sm.append('  <url><loc>%s</loc><xhtml:link rel="alternate" hreflang="bg" href="%s"/><xhtml:link rel="alternate" hreflang="en" href="%s"/><xhtml:link rel="alternate" hreflang="x-default" href="%s"/><changefreq>monthly</changefreq><priority>0.8</priority></url>'%(u,bg,en,bg))
sm.append('</urlset>')
open(os.path.join(OUT,'sitemap.xml'),'w',encoding='utf-8').write("\n".join(sm))
print("BUILD OK ->", OUT)
