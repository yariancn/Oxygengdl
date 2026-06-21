#!/usr/bin/env python3
"""Generate treatment landing pages for OXYGENGDL."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "camaras-hiperbaricas"

PIXEL = """    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '2512040732587770');
    fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=2512040732587770&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Meta Pixel Code -->"""

CSS = """
        :root { --navy: #1d3557; --navy-deep: #0a2540; --cyan: #00b4d8; --white: #ffffff; --muted: #5a6b7d; --border: #e2e8f0; --cream: #f8fafc; --forest: #2b2d42; }
        *, *::before, *::after { box-sizing: border-box; }
        html, body { margin: 0; padding: 0; background: var(--cream); color: var(--forest); font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.65; }
        a { color: var(--navy); }
        a:hover { color: var(--cyan); }
        .site-header { position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: var(--white); box-shadow: 0 2px 15px rgba(0,0,0,0.1); }
        .nav-container { display: flex; align-items: center; justify-content: space-between; max-width: 1200px; margin: 0 auto; padding: 10px 20px; gap: 12px; flex-wrap: wrap; }
        .logo-nav img { max-height: 52px; width: auto; display: block; }
        .nav-links { display: flex; gap: 16px; flex-wrap: wrap; font-size: 0.88rem; font-weight: 600; }
        .nav-links a { text-decoration: none; }
        .btn-wa { display: inline-flex; padding: 10px 18px; background: var(--navy); color: var(--white); border-radius: 6px; font-weight: 700; font-size: 0.88rem; text-decoration: none; white-space: nowrap; }
        .btn-wa:hover { background: var(--cyan); color: var(--white); }
        body { padding-top: 88px; }
        .page-wrap { max-width: 860px; margin: 0 auto; padding: 36px 20px 64px; }
        .breadcrumb { font-size: 0.88rem; color: var(--muted); margin-bottom: 20px; }
        .hero-img { width: 100%; max-height: 320px; object-fit: cover; border-radius: 12px; margin-bottom: 24px; display: block; }
        h1 { color: var(--navy); font-size: clamp(1.5rem, 3vw, 2rem); margin: 0 0 10px; }
        .lead { font-size: 1.05rem; color: var(--muted); margin-bottom: 24px; }
        h2 { color: var(--navy); font-size: 1.15rem; margin: 28px 0 10px; }
        p, li { font-size: 0.95rem; }
        ul { padding-left: 1.25rem; margin: 0 0 14px; }
        li { margin-bottom: 6px; }
        .notice { background: var(--white); border: 1px solid var(--border); border-left: 4px solid var(--cyan); padding: 16px 18px; border-radius: 8px; margin: 20px 0; }
        .notice strong { color: var(--navy); }
        .notice-harch { border-left-color: #1d3557; }
        .cta-box { background: var(--navy); color: var(--white); padding: 28px; border-radius: 12px; text-align: center; margin: 32px 0; }
        .cta-box a { display: inline-block; margin-top: 12px; padding: 12px 28px; background: var(--cyan); color: var(--white); border-radius: 8px; font-weight: 700; text-decoration: none; }
        .cta-box a:hover { opacity: 0.9; }
        .related { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-top: 16px; }
        .related a { display: block; padding: 12px 14px; background: var(--white); border: 1px solid var(--border); border-radius: 8px; text-decoration: none; font-size: 0.9rem; font-weight: 600; }
        .related a:hover { border-color: var(--cyan); }
        footer { background: var(--navy); color: #f1f3f5; padding: 24px 20px; font-size: 0.85rem; text-align: center; border-top: 4px solid var(--cyan); }
        footer a { color: var(--cyan); }
        .disclaimer { font-size: 0.8rem; color: #a8b8c8; margin-top: 12px; }
"""

ATA_NOTICE = """
        <div class="notice">
            <p><strong>Presión de operación:</strong> Nuestras cámaras hiperbáricas operan con presión controlada <strong>hasta 2.0 ATA</strong> (atmosferas absolutas). Los protocolos que aplicamos en OXYGENGDL <strong>no superan este límite</strong>. Cada esquema se define con valoración individual previa.</p>
        </div>"""

HARCH_NOTICE = """
        <div class="notice notice-harch">
            <p><strong>Referencia clínica — Dr. Paul Harch:</strong> En condiciones neurológicas, el diseño de nuestros protocolos toma como referencia las recomendaciones publicadas por el <strong>Dr. Paul Harch</strong> sobre dosificación de oxigenoterapia hiperbárica en lesión neurológica crónica. La literatura publicada por el Dr. Harch enfatiza presiones en el rango de <strong>baja a media presión</strong> (habitualmente <strong>1.3–1.5 ATA</strong> en esquemas descritos, sin exceder nuestro límite de 2.0 ATA), con evaluación periódica de respuesta y ajuste de dosis. En pacientes con antecedente de convulsiones, la literatura publicada sugiere iniciar a presiones más bajas y titular con observación clínica cuidadosa. La presión controlada se considera una variable terapéutica relevante en estos contextos. Todo esquema se integra al plan médico o de rehabilitación del paciente.</p>
        </div>"""

MEDICAL_DISCLAIMER = "La oxigenoterapia hiperbárica es un tratamiento de apoyo complementario. No sustituye diagnóstico, indicación ni seguimiento médico profesional. Certificación IBUM y permiso COFEPRIS."

TREATMENTS = [
    {
        "slug": "diabetes",
        "title": "Cámara Hiperbárica para Diabetes y Pie Diabético en Guadalajara",
        "h1": "Oxigenoterapia Hiperbárica para Diabetes y Pie Diabético",
        "description": "Soporte complementario con cámara hiperbárica hasta 2.0 ATA para microcirculación y cuidado de heridas en diabetes. OXYGENGDL, Guadalajara.",
        "image": "/assets/images/IMAGEN-DIABETES.jpg",
        "image_alt": "Oxigenoterapia hiperbárica para diabetes y pie diabético en Guadalajara",
        "neurological": False,
        "intro": "En OXYGENGDL ofrecemos oxigenoterapia hiperbárica como apoyo complementario para personas con diabetes, incluyendo complicaciones de microcirculación y cuidado de heridas en extremidades.",
        "sections": [
            ("¿Cómo puede apoyar la hiperbaria?", [
                "Favorecer la oxigenación tisular en zonas con microcirculación comprometida.",
                "Apoyar procesos naturales de regeneración en heridas de difícil cicatrización.",
                "Complementar el esquema de cuidado indicado por el médico tratante.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA, sin superar este límite en ningún esquema.",
                "Duración y número de sesiones definidos según valoración individual.",
                "Coordinación con el médico del paciente cuando existan complicaciones del pie diabético.",
            ]),
        ],
        "faq": [
            ("¿Sustituye el tratamiento de diabetes?", "No. Es un apoyo complementario dentro de un plan integral que incluye control glucémico y seguimiento médico."),
            ("¿Cuánto cuesta una sesión?", "Desde $750 MXN por sesión. Paquetes de 5, 10 y 20 sesiones con precio preferencial."),
        ],
    },
    {
        "slug": "autismo",
        "title": "Cámara Hiperbárica para Autismo en Guadalajara | OXYGENGDL",
        "h1": "Oxigenoterapia Hiperbárica como Apoyo en Autismo",
        "description": "Soporte complementario con protocolos de baja a media presión hasta 2.0 ATA, alineados a recomendaciones publicadas del Dr. Harch. Guadalajara.",
        "image": "/assets/images/IMAGEN-AUTISMO.jpg",
        "image_alt": "Oxigenoterapia complementaria para autismo en Guadalajara",
        "neurological": True,
        "intro": "En OXYGENGDL la oxigenoterapia hiperbárica se ofrece como apoyo complementario no invasivo dentro de protocolos de neurodesarrollo, con presión controlada hasta 2.0 ATA y enfoque alineado a la literatura publicada sobre dosificación neurológica.",
        "sections": [
            ("Enfoque de apoyo", [
                "Acompañar de forma complementaria los programas de terapia y neurodesarrollo existentes.",
                "Aplicar presión controlada en rangos terapéuticos de baja a media presión según valoración.",
                "Priorizar seguridad, titulación gradual y observación clínica en cada sesión.",
            ]),
            ("Protocolo neurológico", [
                "Presiones habituales en rango 1.3–1.5 ATA según referencia publicada del Dr. Harch, sin exceder 2.0 ATA.",
                "Esquemas modulares con evaluación periódica de respuesta.",
                "Participación de padres o tutores en consentimiento informado y seguimiento.",
            ]),
        ],
        "faq": [
            ("¿Es un tratamiento curativo para autismo?", "No. Es un apoyo complementario que puede integrarse a un plan terapéutico integral bajo indicación y seguimiento profesional."),
            ("¿Qué presión se utiliza?", "Protocolos con presión controlada hasta 2.0 ATA, habitualmente en rangos de baja a media presión según valoración individual."),
        ],
    },
    {
        "slug": "recuperacion-postoperatoria",
        "title": "Cámara Hiperbárica Postoperatoria en Guadalajara | OXYGENGDL",
        "h1": "Recuperación Postoperatoria con Oxigenoterapia Hiperbárica",
        "description": "Apoyo en cicatrización y recuperación post-cirugía con cámara hiperbárica hasta 2.0 ATA en Guadalajara. Certificación IBUM y COFEPRIS.",
        "image": "/assets/images/IMAGEN-CIRUGIA.jpg",
        "image_alt": "Oxigenoterapia hiperbárica para recuperación postoperatoria en Guadalajara",
        "neurological": False,
        "intro": "La oxigenoterapia hiperbárica puede actuar como coadyuvante en postoperatorios estéticos, reconstructivos y ortopédicos, apoyando la desinflamación tisular y la cicatrización bajo protocolos de presión controlada.",
        "sections": [
            ("Beneficios de apoyo", [
                "Apoyar la oxigenación de tejidos en fase de recuperación.",
                "Complementar indicaciones del cirujano tratante.",
                "Facilitar el retorno progresivo a actividades cotidianas.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA según tipo de cirugía y tiempo de evolución.",
                "Coordinación con fechas de control postoperatorio del médico.",
                "Valoración previa para descartar contraindicaciones.",
            ]),
        ],
        "faq": [
            ("¿Cuándo puedo iniciar después de cirugía?", "Depende del procedimiento y de la autorización de su médico tratante. Realizamos valoración previa."),
            ("¿Cuántas sesiones se recomiendan?", "Varía según el caso. Se define en valoración individual; ofrecemos paquetes de 5, 10 y 20 sesiones."),
        ],
    },
    {
        "slug": "paralisis-cerebral",
        "title": "Cámara Hiperbárica para Parálisis Cerebral Infantil | Guadalajara",
        "h1": "Soporte Hiperbárico en Parálisis Cerebral Infantil",
        "description": "Oxigenoterapia hiperbárica complementaria con protocolos de baja a media presión hasta 2.0 ATA, referencia Dr. Harch. OXYGENGDL Guadalajara.",
        "image": "/assets/images/IMAGEN-PARALISIS-CEREBRAL.jpg",
        "image_alt": "Soporte hiperbárico en parálisis cerebral infantil en Guadalajara",
        "neurological": True,
        "intro": "OXYGENGDL ofrece oxigenoterapia hiperbárica como apoyo coadyuvante en rehabilitación física y terapia neuromuscular infantil, con protocolos de presión controlada alineados a recomendaciones publicadas en lesión neurológica.",
        "sections": [
            ("Integración con rehabilitación", [
                "Complementar fisioterapia y terapias neuromusculares en curso.",
                "Buscar optimizar la respuesta funcional dentro de un plan integral.",
                "Trabajo coordinado con padres y equipo terapéutico del menor.",
            ]),
            ("Protocolo neurológico", [
                "Presiones en rango 1.3–1.5 ATA según referencia publicada del Dr. Harch, sin exceder 2.0 ATA.",
                "Titulación cuidadosa; en antecedente de convulsiones, inicio a presión más baja con observación.",
                "Evaluación periódica de respuesta y ajuste de esquema.",
            ]),
        ],
        "faq": [
            ("¿Desde qué edad se puede valorar?", "Se valora caso por caso con historial clínico y autorización de padres o tutores."),
            ("¿Reemplaza la terapia de rehabilitación?", "No. Es un complemento al plan de rehabilitación indicado por especialistas."),
        ],
    },
    {
        "slug": "evento-cerebrovascular",
        "title": "Cámara Hiperbárica tras Evento Cerebrovascular | Guadalajara",
        "h1": "Apoyo Hiperbárico tras Evento Cerebrovascular",
        "description": "Oxigenoterapia complementaria en rehabilitación neuro-motriz con protocolos hasta 2.0 ATA, referencia publicada Dr. Harch. OXYGENGDL.",
        "image": "/assets/images/IMAGEN-STROKE.jpg",
        "image_alt": "Rehabilitación con cámara hiperbárica tras evento cerebrovascular",
        "neurological": True,
        "intro": "Como apoyo dentro de esquemas integrales de rehabilitación neuro-motriz, la oxigenoterapia hiperbárica puede acompañar la recuperación funcional tras un evento cerebrovascular, con presión controlada y protocolos basados en literatura publicada sobre dosificación neurológica.",
        "sections": [
            ("Rol complementario", [
                "Apoyar áreas con metabolismo cerebral disminuido dentro de un plan de rehabilitación.",
                "Integrarse a terapia física y neurológica prescrita.",
                "No sustituir tratamiento médico de urgencia ni rehabilitación especializada.",
            ]),
            ("Protocolo neurológico", [
                "Esquemas con presión controlada hasta 2.0 ATA; rangos habituales 1.3–1.5 ATA según Dr. Harch.",
                "Cursos modulares con evaluación de respuesta entre bloques de sesiones.",
                "Ajuste de presión ante signos de sensibilidad o según evolución clínica.",
            ]),
        ],
        "faq": [
            ("¿Cuándo se puede iniciar?", "Solo tras valoración médica y estabilización según criterio del neurólogo o médico tratante."),
            ("¿Cuántas sesiones?", "La literatura publicada del Dr. Harch describe cursos modulares (p. ej. bloques de 40 sesiones con evaluación intermedia); el esquema se personaliza."),
        ],
    },
    {
        "slug": "fibromialgia",
        "title": "Cámara Hiperbárica para Fibromialgia en Guadalajara | OXYGENGDL",
        "h1": "Oxigenoterapia Hiperbárica para Fibromialgia",
        "description": "Apoyo complementario para fibromialgia con cámara hiperbárica hasta 2.0 ATA en Guadalajara. OXYGENGDL, certificación IBUM.",
        "image": "/assets/images/fibromialgia.jpg",
        "image_alt": "Terapia hiperbárica para fibromialgia en Guadalajara",
        "neurological": False,
        "intro": "La oxigenoterapia hiperbárica puede ofrecer apoyo complementario orientado a mitigar el agotamiento celular muscular crónico y la inflamación sistémica asociada a la fibromialgia, bajo protocolos de presión controlada hasta 2.0 ATA.",
        "sections": [
            ("Enfoque de apoyo", [
                "Apoyar oxigenación profunda de tejidos musculares.",
                "Complementar el manejo indicado por reumatología o medicina del dolor.",
                "Buscar mejorar calidad de descanso y actividades cotidianas.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA, definida según tolerancia individual.",
                "Sesiones programadas en paquetes de 5, 10 o 20 según valoración.",
            ]),
        ],
        "faq": [
            ("¿Alivia el dolor de fibromialgia?", "Es un apoyo complementario; los resultados varían según cada paciente y deben evaluarse con el médico tratante."),
            ("¿Necesito diagnóstico previo?", "Sí, recomendamos contar con diagnóstico y seguimiento médico de fibromialgia."),
        ],
    },
    {
        "slug": "migrana",
        "title": "Cámara Hiperbárica para Migraña Crónica | Guadalajara",
        "h1": "Oxigenoterapia Hiperbárica para Migraña Crónica",
        "description": "Apoyo complementario en migraña crónica con protocolos de presión controlada hasta 2.0 ATA. OXYGENGDL, Guadalajara.",
        "image": "/assets/images/IMAGEN-MIGRANA.jpg",
        "image_alt": "Oxigenoterapia para migraña crónica en Guadalajara",
        "neurological": True,
        "intro": "Como apoyo fisiológico complementario, la oxigenoterapia hiperbárica puede acompañar el manejo de migraña crónica con presión controlada y protocolos de baja a media presión, sin exceder 2.0 ATA.",
        "sections": [
            ("Enfoque complementario", [
                "Apoyar la regulación vascular cerebral dentro de un plan integral.",
                "Integrarse al tratamiento indicado por neurología.",
                "No sustituir medicación ni protocolos de migraña prescritos.",
            ]),
            ("Protocolo", [
                "Presión controlada hasta 2.0 ATA; rangos terapéuticos personalizados según valoración.",
                "Referencia a principios de dosificación publicados en contextos neurológicos (Dr. Harch).",
            ]),
        ],
        "faq": [
            ("¿Puedo recibir sesión durante una crisis?", "Se valora caso por caso; muchos esquemas se aplican en fase intercrisis bajo indicación."),
            ("¿Cuántas sesiones?", "Depende de la respuesta individual; ofrecemos paquetes desde 5 sesiones."),
        ],
    },
    {
        "slug": "lesiones-deportivas",
        "title": "Cámara Hiperbárica para Lesiones Deportivas | Guadalajara",
        "h1": "Recuperación Deportiva con Oxigenoterapia Hiperbárica",
        "description": "Apoyo en recuperación de lesiones deportivas con cámara hiperbárica hasta 2.0 ATA. OXYGENGDL Guadalajara.",
        "image": "/assets/images/IMAGEN-DEPORTE.jpg",
        "image_alt": "Recuperación deportiva con cámara hiperbárica en Guadalajara",
        "neurological": False,
        "intro": "Atletas y personas activas pueden beneficiarse de la oxigenoterapia hiperbárica como apoyo en la recuperación de músculos, tendones y ligamentos, con protocolos de presión controlada hasta 2.0 ATA.",
        "sections": [
            ("Apoyo en recuperación", [
                "Favorecer oxigenación de tejidos tras esfuerzo intenso o lesión.",
                "Complementar fisioterapia y reposo indicados.",
                "Apoyar retorno gradual al entrenamiento.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA según tipo de lesión y fase de recuperación.",
                "Paquetes de 5, 10 y 20 sesiones disponibles.",
            ]),
        ],
        "faq": [
            ("¿Es solo para deportistas profesionales?", "No. Cualquier persona con lesión deportiva o sobreuso puede valorarse para apoyo complementario."),
            ("¿Cuánto antes de volver a entrenar?", "Depende de la lesión y criterio médico; la hiperbaria es un complemento, no un atajo."),
        ],
    },
    {
        "slug": "procesos-oncologicos",
        "title": "Cámara Hiperbárica en Procesos Oncológicos | Guadalajara",
        "h1": "Oxigenoterapia Hiperbárica como Apoyo en Procesos Oncológicos",
        "description": "Soporte complementario en procesos oncológicos con cámara hiperbárica hasta 2.0 ATA. OXYGENGDL Guadalajara, COFEPRIS.",
        "image": "/assets/images/IMAGEN-CANCER.jpg",
        "image_alt": "Soporte complementario de oxigenoterapia en procesos oncológicos",
        "neurological": False,
        "intro": "La oxigenoterapia hiperbárica puede actuar como apoyo complementario en procesos oncológicos, buscando optimizar el entorno celular y acompañar la estabilidad general del paciente dentro de su esquema de cuidado integral.",
        "sections": [
            ("Enfoque integral", [
                "Apoyo complementario, nunca sustituto de oncología convencional.",
                "Coordinación con el equipo médico tratante obligatoria.",
                "Presión controlada hasta 2.0 ATA según valoración y fase de tratamiento.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Valoración previa detallada y autorización del oncólogo.",
                "Esquemas modulares con seguimiento de tolerancia.",
            ]),
        ],
        "faq": [
            ("¿Puede recibir quien está en quimioterapia?", "Solo con autorización expresa del oncólogo tratante y valoración previa en OXYGENGDL."),
            ("¿Cura el cáncer?", "No. Es un apoyo complementario dentro de un plan oncológico integral."),
        ],
    },
]


def render_page(t: dict) -> str:
    url = f"https://oxygengdl.com/camaras-hiperbaricas/{t['slug']}/"
    wa_text = t["h1"].replace(" ", "%20")[:60]
    sections_html = ""
    for heading, bullets in t["sections"]:
        items = "".join(f"<li>{b}</li>" for b in bullets)
        sections_html += f"<h2>{heading}</h2><ul>{items}</ul>\n"

    faq_html = ""
    for q, a in t["faq"]:
        faq_html += f'<div class="notice"><p><strong>{q}</strong><br>{a}</p></div>\n'

    neuro_block = HARCH_NOTICE if t["neurological"] else ""

    related = [x for x in TREATMENTS if x["slug"] != t["slug"]][:6]
    related_html = "".join(
        f'<a href="/camaras-hiperbaricas/{x["slug"]}/">{x["h1"].split(" con ")[0].split(" para ")[0][:40]}</a>'
        for x in related
    )

    schema = f"""    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "MedicalWebPage",
      "name": "{t['title']}",
      "description": "{t['description']}",
      "url": "{url}",
      "inLanguage": "es-MX",
      "about": {{
        "@type": "HyperbaricMedicineService",
        "name": "{t['h1']}",
        "provider": {{
          "@type": "MedicalClinic",
          "name": "Cámara Hiperbárica OXYGENGDL",
          "url": "https://oxygengdl.com/"
        }},
        "areaServed": "Guadalajara, Jalisco, México"
      }}
    }}
    </script>"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{PIXEL}
    <title>{t['title']}</title>
    <meta name="description" content="{t['description']}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">
    <link rel="icon" type="image/png" href="/assets/images/logo.png">
{schema}
    <style>{CSS}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="nav-container">
            <a href="/" class="logo-nav" aria-label="Inicio OXYGENGDL">
                <img src="/assets/images/OXY-LOGO_Mesa-de-trabajo-1.png" alt="OXYGENGDL" width="160" height="52">
            </a>
            <nav class="nav-links" aria-label="Secciones">
                <a href="/camaras-hiperbaricas/">Indicaciones</a>
                <a href="/#costos">Precios</a>
                <a href="/#ubicacion">Ubicación</a>
            </nav>
            <a class="btn-wa" href="https://wa.me/523328332686?text=Hola,%20me%20interesa%20información%20sobre%20{wa_text}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
    </header>

    <main class="page-wrap">
        <p class="breadcrumb"><a href="/">Inicio</a> · <a href="/camaras-hiperbaricas/">Cámaras hiperbáricas</a> · {t['h1']}</p>
        <img class="hero-img" src="{t['image']}" alt="{t['image_alt']}" width="860" height="320" loading="eager">
        <h1>{t['h1']}</h1>
        <p class="lead">{t['intro']} · <strong>Guadalajara, Jalisco</strong> · Certificación IBUM · Permiso COFEPRIS</p>
{ATA_NOTICE}
{neuro_block}
        {sections_html}
        <h2>Preguntas frecuentes</h2>
        {faq_html}
        <div class="cta-box">
            <p><strong>Agenda tu valoración en OXYGENGDL</strong><br>C. Gral. San Martín 420, Col. Americana, Guadalajara · Tel. 33 2833 2686</p>
            <a href="https://wa.me/523328332686?text=Hola,%20quiero%20información%20sobre%20{wa_text}" target="_blank" rel="noopener">Agendar por WhatsApp</a>
        </div>
        <h2>Otras indicaciones</h2>
        <div class="related">{related_html}</div>
    </main>

    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a> · <a href="/terminos-y-condiciones/">Términos</a></p>
        <p class="disclaimer">{MEDICAL_DISCLAIMER}</p>
    </footer>
</body>
</html>
"""


def render_hub() -> str:
    cards = ""
    for t in TREATMENTS:
        cards += f"""            <a class="card" href="/camaras-hiperbaricas/{t['slug']}/">
                <img src="{t['image']}" alt="{t['image_alt']}" width="400" height="180" loading="lazy">
                <div class="card-body"><h2>{t['h1']}</h2><p>{t['intro'][:120]}…</p></div>
            </a>
"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{PIXEL}
    <title>Cámaras Hiperbáricas en Guadalajara | Oxigenoterapia hasta 2.0 ATA | OXYGENGDL</title>
    <meta name="description" content="Cámara hiperbárica en Guadalajara con presión controlada hasta 2.0 ATA. Indicaciones de apoyo: diabetes, autismo, postoperatorio, rehabilitación neurológica y más. OXYGENGDL.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://oxygengdl.com/camaras-hiperbaricas/">
    <link rel="icon" type="image/png" href="/assets/images/logo.png">
    <style>{CSS}
        .hub-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-top: 24px; }}
        .card {{ background: var(--white); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; text-decoration: none; color: inherit; transition: transform 0.2s, box-shadow 0.2s; }}
        .card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.08); }}
        .card img {{ width: 100%; height: 160px; object-fit: cover; display: block; }}
        .card-body {{ padding: 18px; }}
        .card-body h2 {{ font-size: 1.05rem; margin: 0 0 8px; color: var(--navy); }}
        .card-body p {{ margin: 0; font-size: 0.88rem; color: var(--muted); }}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="nav-container">
            <a href="/" class="logo-nav"><img src="/assets/images/OXY-LOGO_Mesa-de-trabajo-1.png" alt="OXYGENGDL" width="160" height="52"></a>
            <nav class="nav-links"><a href="/#costos">Precios</a><a href="/#ubicacion">Ubicación</a></nav>
            <a class="btn-wa" href="https://wa.me/523328332686" target="_blank" rel="noopener">WhatsApp</a>
        </div>
    </header>
    <main class="page-wrap">
        <p class="breadcrumb"><a href="/">Inicio</a> · Cámaras hiperbáricas</p>
        <h1>Cámara Hiperbárica en Guadalajara</h1>
        <p class="lead">Oxigenoterapia hiperbárica con presión controlada <strong>hasta 2.0 ATA</strong>. Certificación IBUM · Permiso COFEPRIS · C. Gral. San Martín 420, Col. Americana.</p>
{ATA_NOTICE}
        <p>Explore nuestras indicaciones de apoyo complementario. En condiciones neurológicas, los protocolos siguen referencias publicadas del <strong>Dr. Paul Harch</strong> sobre dosificación, con presiones habituales de baja a media presión sin exceder 2.0 ATA.</p>
        <div class="hub-grid">
{cards}        </div>
        <div class="cta-box">
            <p><strong>¿No encuentra su indicación?</strong> Escríbanos por WhatsApp al 33 2833 2686.</p>
            <a href="https://wa.me/523328332686" target="_blank" rel="noopener">Contactar</a>
        </div>
    </main>
    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a></p>
        <p class="disclaimer">{MEDICAL_DISCLAIMER}</p>
    </footer>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(render_hub(), encoding="utf-8")
    for t in TREATMENTS:
        d = OUT / t["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render_page(t), encoding="utf-8")
    print(f"Generated hub + {len(TREATMENTS)} landing pages in {OUT}")


if __name__ == "__main__":
    main()
