from pathlib import Path

# Homepage cleaning card
p = Path('scripts/generate-homepages.py')
s = p.read_text(encoding='utf-8')
s = s.replace('Caterina Cantemir', 'Caterina')
if '"whatsapp_href": "https://wa.me/351963212185"' not in s:
    s = s.replace(
        '    "tel_href": "tel:+351963212185",\n    "labels": {',
        '    "tel_href": "tel:+351963212185",\n    "whatsapp_href": "https://wa.me/351963212185",\n    "labels": {'
    )
s = s.replace('"call": "Ligar diretamente"', '"call": "Ligar"')
s = s.replace('"call": "Call directly"', '"call": "Call"')
s = s.replace('"call": "Llamar diretamente"', '"call": "Llamar"')
s = s.replace('"call": "Appeler directement"', '"call": "Appeler"')
if 'cleaning-partner-whatsapp' not in s:
    old = '''                '</a>'
                '</div>'
            )
            link_text = labels["details"]'''
    new = '''                '</a>'
                f'<a class="cleaning-partner-call cleaning-partner-whatsapp" href="{CLEANING_PARTNER["whatsapp_href"]}" '
                'target="_blank" rel="noopener noreferrer" aria-label="Contactar Caterina por WhatsApp">'
                '<i class="fa-brands fa-whatsapp" aria-hidden="true"></i>'
                '<span>WhatsApp</span>'
                '</a>'
                '</div>'
            )
            link_text = labels["details"]'''
    s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

# Cleaning service page: call and WhatsApp both direct to Caterina
p = Path('scripts/generate-servico-pages.py')
s = p.read_text(encoding='utf-8').replace('Caterina Cantemir', 'Caterina')
if '"whatsapp": "WhatsApp da Caterina · 963 212 185"' not in s:
    s = s.replace(
        '        "call": "Ligar diretamente à Caterina · 963 212 185",',
        '        "call": "Ligar à Caterina · 963 212 185",\n        "whatsapp": "WhatsApp da Caterina · 963 212 185",'
    )
    s = s.replace(
        '        "call": "Call Caterina directly · 963 212 185",',
        '        "call": "Call Caterina · 963 212 185",\n        "whatsapp": "WhatsApp Caterina · 963 212 185",'
    )
    s = s.replace(
        '        "call": "Llamar directamente a Caterina · 963 212 185",',
        '        "call": "Llamar a Caterina · 963 212 185",\n        "whatsapp": "WhatsApp Caterina · 963 212 185",'
    )
    s = s.replace(
        '        "call": "Appeler Caterina directement · 963 212 185",',
        '        "call": "Appeler Caterina · 963 212 185",\n        "whatsapp": "WhatsApp Caterina · 963 212 185",'
    )

if 'cta_wa = ui["cta_wa"]' not in s:
    s = s.replace(
'''    cta_p = ui["cta_p"].format(service=meta["service_name"])
    cta_call = ui["cta_call"]
    call_href = tel_href()
    if is_cleaning_partner:
        partner_cta = CLEANING_PARTNER_CTA[lang]
        cta_p = partner_cta["text"]
        cta_call = partner_cta["call"]
        call_href = f"tel:{CLEANING_PARTNER_PHONE}"
''',
'''    cta_p = ui["cta_p"].format(service=meta["service_name"])
    cta_call = ui["cta_call"]
    cta_wa = ui["cta_wa"]
    call_href = tel_href()
    wa_link = wa_href_for_message(meta["wa_message"])
    if is_cleaning_partner:
        partner_cta = CLEANING_PARTNER_CTA[lang]
        cta_p = partner_cta["text"]
        cta_call = partner_cta["call"]
        cta_wa = partner_cta["whatsapp"]
        call_href = f"tel:{CLEANING_PARTNER_PHONE}"
        wa_link = "https://wa.me/351963212185"
''')

s = s.replace(
'''            "CTA_WA": ui["cta_wa"],
            "CTA_CALL": cta_call,
            "WA_HREF": wa_href_for_message(meta["wa_message"]),
''',
'''            "CTA_WA": cta_wa,
            "CTA_CALL": cta_call,
            "WA_HREF": wa_link,
''')
p.write_text(s, encoding='utf-8')

# Styling
p = Path('style.css')
s = p.read_text(encoding='utf-8')
if '.cleaning-partner-whatsapp {' not in s:
    s += '\n\n.cleaning-partner-whatsapp {\n    background: #25D366;\n}\n\n.cleaning-partner-whatsapp:hover {\n    background: #1DA851;\n}\n'
p.write_text(s, encoding='utf-8')

# Public project note
doc = Path('docs/CLEANING_PARTNER.md')
if doc.exists():
    d = doc.read_text(encoding='utf-8').replace('Caterina Cantemir', 'Caterina')
    if 'wa.me/351963212185' not in d:
        d += '\n- WhatsApp direto: `https://wa.me/351963212185`\n'
    doc.write_text(d, encoding='utf-8')

print('Cleaning contact source update complete')
