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
        h3 { color: var(--navy); font-size: 1rem; margin: 18px 0 8px; }
        p, li { font-size: 0.95rem; }
        ul { padding-left: 1.25rem; margin: 0 0 14px; }
        li { margin-bottom: 6px; }
        .notice { background: var(--white); border: 1px solid var(--border); border-left: 4px solid var(--cyan); padding: 16px 18px; border-radius: 8px; margin: 20px 0; }
        .notice strong { color: var(--navy); }
        .notice-harch { border-left-color: #1d3557; }
        .prep-box { background: var(--white); border: 1px solid var(--border); border-radius: 12px; padding: 20px 22px; margin: 16px 0; }
        .cta-box { background: var(--navy); color: var(--white); padding: 28px; border-radius: 12px; text-align: center; margin: 32px 0; }
        .cta-box a { display: inline-block; margin-top: 12px; padding: 12px 28px; background: var(--cyan); color: var(--white); border-radius: 8px; font-weight: 700; text-decoration: none; }
        .cta-box a:hover { opacity: 0.9; }
        .btn-home-main { display: inline-flex; align-items: center; padding: 12px 24px; background: var(--white); color: var(--navy); border: 2px solid var(--navy); border-radius: 8px; font-weight: 700; text-decoration: none; margin-top: 8px; }
        .btn-home-main:hover { background: var(--navy); color: var(--white); }
        footer { background: var(--navy); color: #f1f3f5; padding: 24px 20px; font-size: 0.85rem; text-align: center; border-top: 4px solid var(--cyan); }
        footer a { color: var(--cyan); }
        .disclaimer { font-size: 0.8rem; color: #a8b8c8; margin-top: 12px; }
        .social-links { margin: 10px 0 0; }
"""

SOCIAL_LINKS = """        <p class="social-links"><a href="https://www.facebook.com/oxygengdl" target="_blank" rel="noopener noreferrer">Facebook</a> · <a href="https://www.instagram.com/oxygengdl" target="_blank" rel="noopener noreferrer">Instagram</a> · <a href="https://www.tiktok.com/@oxygengdl" target="_blank" rel="noopener noreferrer">TikTok</a></p>"""

ATA_NOTICE = """
        <div class="notice">
            <p><strong>Presión de operación:</strong> Nuestras cámaras hiperbáricas operan con presión controlada <strong>hasta 2.0 ATA</strong> (atmosferas absolutas). La valoración se realiza en tu <strong>primera cita</strong>.</p>
        </div>"""

HARCH_NOTICE = """
        <div class="notice notice-harch">
            <p><strong>Referencia clínica:</strong> En condiciones neurológicas, nuestros protocolos toman como referencia las recomendaciones publicadas del <a href="/camaras-hiperbaricas/dr-paul-harch/">Dr. Paul Harch</a> sobre dosificación en lesión neurológica crónica, con presiones habituales de baja a media presión (1.3–1.5 ATA) y evaluación periódica de respuesta.</p>
        </div>"""

PREP_PAGE_BODY = """
        <p>¡Hola! Gracias por reservar con OXYGENGDL. 🫧</p>
        <p>Para garantizar tu seguridad y la efectividad de tu tratamiento, por favor lee las siguientes indicaciones antes de tu sesión de Cámara Hiperbárica:</p>
        <h2>🚫 Restricciones importantes</h2>
        <ul>
            <li><strong>Sustancias:</strong> No consumir alcohol ni drogas 8 horas antes.</li>
            <li><strong>Tabaco:</strong> No fumar 24 h antes ni después de la sesión.</li>
            <li><strong>Vuelos:</strong> No volar 24 h antes ni después de la sesión.</li>
            <li><strong>Salud:</strong> No ingresar con fiebre o infección respiratoria. (Pacientes con historial de neumotórax, barotrauma o implantes electrónicos no compatibles no podrán ingresar).</li>
        </ul>
        <h2>👕 Vestimenta e higiene</h2>
        <ul>
            <li>Venir bien aseado, sin cremas, perfumes ni lociones.</li>
            <li>Usar ropa cómoda (de preferencia pants).</li>
            <li>Uñas limpias, cortas y sin esmalte fresco.</li>
            <li><strong>Prohibido:</strong> Joyas, relojes, llaves, clips y dispositivos electrónicos.</li>
            <li><strong>Ojos:</strong> Usar anteojos si los necesitas; retirar lentes de contacto.</li>
        </ul>
        <h2>⏰ Sobre tu cita</h2>
        <ul>
            <li><strong>Primera vez:</strong> Llegar 30 minutos antes para valoración e inducción.</li>
            <li><strong>Identificación:</strong> Presentar identificación vigente en tu primera sesión.</li>
            <li><strong>Puntualidad:</strong> Si llegas tarde, se descontará el tiempo de tu sesión.</li>
            <li><strong>Cancelaciones:</strong> Cambios o cancelaciones con 24 h de anticipación, o la sesión se dará por tomada.</li>
        </ul>
        <h2>📍 Ubicación</h2>
        <p>General San Martín #420 (Esq. José Guadalupe Montenegro), Guadalajara.<br>
        <a href="https://maps.app.goo.gl/zaU4FmQpDf6b9rnD8" target="_blank" rel="noopener">Ver en Google Maps</a></p>
        <h2>📞 Contacto directo</h2>
        <p>Cualquier programación o dudas: <a href="tel:+523321664083">33 2166 4083</a></p>
        <p style="text-align:center;margin-top:32px;">
            <a href="/" class="btn-home-main">← Regresar a página principal</a>
        </p>"""

MEDICAL_DISCLAIMER = "La oxigenoterapia hiperbárica es un tratamiento de apoyo complementario. No sustituye diagnóstico ni seguimiento profesional. Certificación IBUM."

NAV_BUTTONS = """
        <p style="text-align:center;margin-top:24px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
            <a href="/" class="btn-home-main">← Regresar a página principal</a>
            <a href="/camaras-hiperbaricas/" class="btn-home-main">Tratamientos</a>
        </p>"""

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
                "Complementar el esquema de cuidado integral del paciente.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA.",
                "Duración y número de sesiones definidos en tu primera cita.",
                "Seguimiento de evolución en cada sesión.",
            ]),
        ],
        "faq": [
            ("¿Sustituye el tratamiento de diabetes?", "No. Es un apoyo complementario dentro de un plan integral que incluye control glucémico y cuidado personal."),
            ("¿Cuánto cuesta una sesión?", "Desde $750 MXN por sesión. Paquetes de 5, 10 y 20 sesiones con precio preferencial."),
        ],
    },
    {
        "slug": "autismo",
        "title": "Cámara Hiperbárica para Autismo en Guadalajara | OXYGENGDL",
        "h1": "Oxigenoterapia Hiperbárica como Apoyo en Autismo",
        "description": "Soporte complementario con protocolos de baja a media presión hasta 2.0 ATA en Guadalajara. OXYGENGDL.",
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
                "Presiones habituales en rango 1.3–1.5 ATA.",
                "Esquemas modulares con evaluación periódica de respuesta.",
                "Participación de padres o tutores en consentimiento informado y seguimiento.",
            ]),
        ],
        "faq": [
            ("¿Es un tratamiento curativo para autismo?", "No. Es un apoyo complementario que puede integrarse a un plan terapéutico integral."),
            ("¿Qué presión se utiliza?", "Protocolos con presión controlada hasta 2.0 ATA, habitualmente en rangos de baja a media presión."),
        ],
    },
    {
        "slug": "recuperacion-postoperatoria",
        "title": "Cámara Hiperbárica Postoperatoria en Guadalajara | OXYGENGDL",
        "h1": "Recuperación Postoperatoria con Oxigenoterapia Hiperbárica",
        "description": "Apoyo en cicatrización y recuperación post-cirugía con cámara hiperbárica hasta 2.0 ATA en Guadalajara. Certificación IBUM.",
        "image": "/assets/images/IMAGEN-CIRUGIA.jpg",
        "image_alt": "Oxigenoterapia hiperbárica para recuperación postoperatoria en Guadalajara",
        "neurological": False,
        "hide_ata": True,
        "intro": "La oxigenoterapia hiperbárica puede actuar como coadyuvante en postoperatorios estéticos, reconstructivos y ortopédicos, apoyando la desinflamación tisular y la cicatrización bajo protocolos de presión controlada.",
        "sections": [
            ("Beneficios de apoyo", [
                "Apoyar la oxigenación de tejidos en fase de recuperación.",
                "Complementar el periodo de recuperación postoperatoria.",
                "Facilitar el retorno progresivo a actividades cotidianas.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA según tipo de cirugía y tiempo de evolución.",
                "La valoración se realiza en tu primera cita.",
                "Esquemas personalizados según evolución del paciente.",
            ]),
        ],
        "faq": [
            ("¿Cuándo puedo iniciar después de cirugía?", "Depende del procedimiento y del tiempo de evolución. En tu primera cita realizamos la valoración."),
            ("¿Cuántas sesiones se recomiendan?", "Varía según el caso. Se define en tu primera cita; ofrecemos paquetes de 5, 10 y 20 sesiones."),
        ],
    },
    {
        "slug": "paralisis-cerebral",
        "title": "Cámara Hiperbárica para Parálisis Cerebral Infantil | Guadalajara",
        "h1": "Soporte Hiperbárico en Parálisis Cerebral Infantil",
        "description": "Oxigenoterapia hiperbárica complementaria con protocolos de baja a media presión hasta 2.0 ATA. OXYGENGDL Guadalajara.",
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
                "Presiones en rango 1.3–1.5 ATA.",
                "Titulación cuidadosa; en antecedente de convulsiones, inicio a presión más baja con observación.",
                "Evaluación periódica de respuesta y ajuste de esquema.",
            ]),
        ],
        "faq": [
            ("¿Desde qué edad se puede valorar?", "Se valora caso por caso con historial clínico y consentimiento de padres o tutores."),
            ("¿Reemplaza la terapia de rehabilitación?", "No. Es un complemento al plan de rehabilitación del menor."),
        ],
    },
    {
        "slug": "evento-cerebrovascular",
        "title": "Cámara Hiperbárica tras Evento Cerebrovascular | Guadalajara",
        "h1": "Apoyo Hiperbárico tras Evento Cerebrovascular",
        "description": "Oxigenoterapia complementaria en rehabilitación neuro-motriz con protocolos hasta 2.0 ATA. OXYGENGDL.",
        "image": "/assets/images/IMAGEN-STROKE.jpg",
        "image_alt": "Rehabilitación con cámara hiperbárica tras evento cerebrovascular",
        "neurological": True,
        "intro": "Como apoyo dentro de esquemas integrales de rehabilitación neuro-motriz, la oxigenoterapia hiperbárica puede acompañar la recuperación funcional tras un evento cerebrovascular, con presión controlada y protocolos basados en literatura publicada sobre dosificación neurológica.",
        "sections": [
            ("Rol complementario", [
                "Apoyar áreas con metabolismo cerebral disminuido dentro de un plan de rehabilitación.",
                "Integrarse a terapia física y neurológica en curso.",
                "Acompañar el proceso de recuperación funcional.",
            ]),
            ("Protocolo neurológico", [
                "Esquemas con presión controlada hasta 2.0 ATA; rangos habituales 1.3–1.5 ATA.",
                "Cursos modulares con evaluación de respuesta entre bloques de sesiones.",
                "Ajuste de presión ante signos de sensibilidad o según evolución.",
            ]),
        ],
        "faq": [
            ("¿Cuándo se puede iniciar?", "Tras estabilización clínica; la valoración se realiza en tu primera cita."),
            ("¿Cuántas sesiones?", "Cursos modulares con evaluación intermedia; el esquema se personaliza en tu primera cita."),
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
                "Complementar el manejo integral del paciente.",
                "Buscar mejorar calidad de descanso y actividades cotidianas.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA, definida según tolerancia individual.",
                "Sesiones programadas en paquetes de 5, 10 o 20 según tu primera valoración.",
            ]),
        ],
        "faq": [
            ("¿Alivia el dolor de fibromialgia?", "Es un apoyo complementario; los resultados varían según cada paciente."),
            ("¿Cuánto cuesta?", "Desde $750 MXN por sesión. Consulta paquetes de 5, 10 y 20 sesiones."),
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
        "intro": "Como apoyo fisiológico complementario, la oxigenoterapia hiperbárica puede acompañar el manejo de migraña crónica con presión controlada y protocolos de baja a media presión.",
        "sections": [
            ("Enfoque complementario", [
                "Apoyar la regulación vascular cerebral dentro de un plan integral.",
                "Integrarse al manejo general del paciente.",
                "Buscar espaciar la frecuencia de episodios dolorosos.",
            ]),
            ("Protocolo", [
                "Presión controlada hasta 2.0 ATA; rangos terapéuticos personalizados.",
                "Esquemas modulares con evaluación periódica de respuesta.",
            ]),
        ],
        "faq": [
            ("¿Puedo recibir sesión durante una crisis?", "Se valora caso por caso; muchos esquemas se aplican en fase intercrisis."),
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
                "Complementar fisioterapia y reposo.",
                "Apoyar retorno gradual al entrenamiento.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "Presión controlada hasta 2.0 ATA según tipo de lesión y fase de recuperación.",
                "Paquetes de 5, 10 y 20 sesiones disponibles.",
            ]),
        ],
        "faq": [
            ("¿Es solo para deportistas profesionales?", "No. Cualquier persona con lesión deportiva o sobreuso puede valorarse para apoyo complementario."),
            ("¿Cuánto antes de volver a entrenar?", "Depende de la lesión y la evolución; la hiperbaria es un complemento, no un atajo."),
        ],
    },
    {
        "slug": "procesos-oncologicos",
        "title": "Cámara Hiperbárica en Procesos Oncológicos | Guadalajara",
        "h1": "Oxigenoterapia Hiperbárica como Apoyo en Procesos Oncológicos",
        "description": "Soporte complementario en procesos oncológicos con cámara hiperbárica hasta 2.0 ATA. OXYGENGDL Guadalajara.",
        "image": "/assets/images/IMAGEN-CANCER.jpg",
        "image_alt": "Soporte complementario de oxigenoterapia en procesos oncológicos",
        "neurological": False,
        "intro": "La oxigenoterapia hiperbárica puede actuar como apoyo complementario en procesos oncológicos, buscando optimizar el entorno celular y acompañar la estabilidad general del paciente dentro de su esquema de cuidado integral.",
        "sections": [
            ("Enfoque integral", [
                "Apoyo complementario, nunca sustituto de oncología convencional.",
                "Presión controlada hasta 2.0 ATA según fase de tratamiento.",
                "Seguimiento de tolerancia en cada sesión.",
            ]),
            ("Protocolo en OXYGENGDL", [
                "La valoración se realiza en tu primera cita.",
                "Esquemas modulares con seguimiento de tolerancia.",
            ]),
        ],
        "faq": [
            ("¿Puede recibir quien está en quimioterapia?", "Se valora caso por caso en tu primera cita en OXYGENGDL."),
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
    ata_block = "" if t.get("hide_ata") else ATA_NOTICE

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
                <a href="/camaras-hiperbaricas/">Tratamientos</a>
                <a href="/#costos">Precios</a>
                <a href="/#ubicacion">Ubicación</a>
            </nav>
            <a class="btn-wa" href="https://wa.me/523328332686?text=Hola,%20me%20interesa%20información%20sobre%20{wa_text}" target="_blank" rel="noopener">WhatsApp</a>
        </div>
    </header>

    <main class="page-wrap">
        <p class="breadcrumb"><a href="/">Inicio</a> · <a href="/camaras-hiperbaricas/">Tratamientos</a> · {t['h1']}</p>
        <img class="hero-img" src="{t['image']}" alt="{t['image_alt']}" width="860" height="320" loading="eager">
        <h1>{t['h1']}</h1>
        <p class="lead">{t['intro']} · <strong>Guadalajara, Jalisco</strong> · Certificación IBUM</p>
{ata_block}
{neuro_block}
        {sections_html}
        <h2>Preguntas frecuentes</h2>
        {faq_html}
        <div class="cta-box">
            <p><strong>Agenda tu cita en OXYGENGDL</strong><br>La valoración se realiza en tu primera sesión.<br>C. Gral. San Martín 420, Col. Americana, Guadalajara · Tel. <a href="tel:+523321664083" style="color:#fff">33 2166 4083</a></p>
            <a href="https://wa.me/523328332686?text=Hola,%20quiero%20información%20sobre%20{wa_text}" target="_blank" rel="noopener">Agendar por WhatsApp</a>
        </div>
{NAV_BUTTONS}
    </main>

    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a> · <a href="/terminos-y-condiciones/">Términos</a></p>
{SOCIAL_LINKS}
        <p class="disclaimer">{MEDICAL_DISCLAIMER}</p>
    </footer>
</body>
</html>
"""


def render_harch_page() -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{PIXEL}
    <title>Dr. Paul Harch y protocolos neurológicos | OXYGENGDL</title>
    <meta name="description" content="Quién es el Dr. Paul Harch y por qué sus publicaciones son referencia para protocolos de oxigenoterapia hiperbárica en condiciones neurológicas en OXYGENGDL.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://oxygengdl.com/camaras-hiperbaricas/dr-paul-harch/">
    <link rel="icon" type="image/png" href="/assets/images/logo.png">
    <style>{CSS}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="nav-container">
            <a href="/" class="logo-nav"><img src="/assets/images/OXY-LOGO_Mesa-de-trabajo-1.png" alt="OXYGENGDL" width="160" height="52"></a>
            <nav class="nav-links"><a href="/camaras-hiperbaricas/">Tratamientos</a><a href="/">Inicio</a></nav>
            <a class="btn-wa" href="https://wa.me/523328332686" target="_blank" rel="noopener">WhatsApp</a>
        </div>
    </header>
    <main class="page-wrap">
        <p class="breadcrumb"><a href="/">Inicio</a> · <a href="/camaras-hiperbaricas/">Tratamientos</a> · Dr. Paul Harch</p>
        <h1>Dr. Paul Harch y nuestros protocolos neurológicos</h1>
        <p class="lead">Referencia clínica para condiciones neurológicas en OXYGENGDL · Guadalajara, Jalisco</p>

        <h2>¿Quién es el Dr. Paul Harch?</h2>
        <p>El <strong>Dr. Paul G. Harch, M.D.</strong> es médico especialista en medicina hiperbárica con décadas de experiencia clínica e investigación en oxigenoterapia hiperbárica (HBOT), particularmente en lesión neurológica crónica, traumatismo craneoencefálico y condiciones del neurodesarrollo. Ha publicado extensamente sobre <strong>dosificación</strong> de la terapia hiperbárica — es decir, qué presión, duración y número de sesiones utilizar según el tipo de condición y la respuesta del paciente.</p>

        <h2>¿Por qué es referencia para OXYGENGDL?</h2>
        <p>En OXYGENGDL, cuando atendemos condiciones neurológicas (como autismo, parálisis cerebral, evento cerebrovascular o migraña crónica), tomamos como referencia las <strong>recomendaciones publicadas por el Dr. Harch</strong> sobre:</p>
        <ul>
            <li>Uso de presiones de <strong>baja a media presión</strong> (habitualmente 1.3–1.5 ATA en los esquemas descritos en su literatura).</li>
            <li>Importancia de la <strong>presión controlada</strong> como variable terapéutica relevante.</li>
            <li>Esquemas <strong>modulares</strong> con evaluación periódica de respuesta.</li>
            <li>Titulación cuidadosa en pacientes con antecedente de convulsiones.</li>
        </ul>
        <p>Nuestras cámaras operan con presión controlada <strong>hasta 2.0 ATA</strong>, lo que permite aplicar estos rangos terapéuticos con margen de seguridad operativa.</p>

        <div class="notice">
            <p><strong>Nota importante:</strong> OXYGENGDL no representa al Dr. Harch ni a su clínica. Utilizamos su literatura publicada como referencia científica para el diseño de protocolos neurológicos. Cada paciente recibe valoración individual antes de iniciar sesiones.</p>
        </div>

        <h2>Indicaciones neurológicas en OXYGENGDL</h2>
        <ul>
            <li><a href="/camaras-hiperbaricas/autismo/">Autismo</a></li>
            <li><a href="/camaras-hiperbaricas/paralisis-cerebral/">Parálisis cerebral infantil</a></li>
            <li><a href="/camaras-hiperbaricas/evento-cerebrovascular/">Evento cerebrovascular</a></li>
            <li><a href="/camaras-hiperbaricas/migrana/">Migraña crónica</a></li>
        </ul>

        <p style="text-align:center;margin-top:32px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
            <a href="/camaras-hiperbaricas/" class="btn-home-main">Tratamientos</a>
            <a href="/" class="btn-home-main">← Regresar a página principal</a>
        </p>
    </main>
    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a></p>
{SOCIAL_LINKS}
        <p class="disclaimer">{MEDICAL_DISCLAIMER}</p>
    </footer>
</body>
</html>
"""


def render_prep_page() -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
{PIXEL}
    <title>Indicaciones para tu sesión | OXYGENGDL — Guadalajara</title>
    <meta name="description" content="Indicaciones para asistir a tu sesión de cámara hiperbárica en OXYGENGDL: restricciones, vestimenta, puntualidad, ubicación y contacto.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://oxygengdl.com/indicaciones-para-sesiones/">
    <link rel="icon" type="image/png" href="/assets/images/logo.png">
    <style>{CSS}
    </style>
</head>
<body>
    <header class="site-header">
        <div class="nav-container">
            <a href="/" class="logo-nav"><img src="/assets/images/OXY-LOGO_Mesa-de-trabajo-1.png" alt="OXYGENGDL" width="160" height="52"></a>
            <a href="/" class="btn-wa">Inicio</a>
        </div>
    </header>
    <main class="page-wrap">
        <h1>Indicaciones para tu sesión</h1>
        <p class="lead">OXYGENGDL · Cámara Hiperbárica · Guadalajara, Jalisco</p>
{PREP_PAGE_BODY}
    </main>
    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a></p>
{SOCIAL_LINKS}
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
        <p class="breadcrumb"><a href="/">Inicio</a> · Tratamientos</p>
        <h1>Cámara Hiperbárica en Guadalajara</h1>
        <p class="lead">Oxigenoterapia hiperbárica con presión controlada <strong>hasta 2.0 ATA</strong>. Certificación IBUM · C. Gral. San Martín 420, Col. Americana.</p>
{ATA_NOTICE}
        <p>Explore nuestros tratamientos de apoyo complementario. En condiciones neurológicas, los protocolos siguen referencias publicadas del <a href="/camaras-hiperbaricas/dr-paul-harch/">Dr. Paul Harch</a> sobre dosificación, con presiones habituales de baja a media presión.</p>
        <div class="hub-grid">
{cards}        </div>
        <div class="cta-box">
            <p><strong>¿No encuentra su tratamiento?</strong> Escríbanos por WhatsApp al <a href="tel:+523321664083" style="color:#fff">33 2166 4083</a></p>
            <a href="https://wa.me/523328332686" target="_blank" rel="noopener">Contactar</a>
        </div>
{NAV_BUTTONS}
    </main>
    <footer>
        <p><a href="/">oxygengdl.com</a> · <a href="/politica-de-privacidad/">Aviso de Privacidad</a></p>
{SOCIAL_LINKS}
        <p class="disclaimer">{MEDICAL_DISCLAIMER}</p>
    </footer>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(render_hub(), encoding="utf-8")
    prep_dir = ROOT / "indicaciones-para-sesiones"
    prep_dir.mkdir(parents=True, exist_ok=True)
    (prep_dir / "index.html").write_text(render_prep_page(), encoding="utf-8")
    harch_dir = OUT / "dr-paul-harch"
    harch_dir.mkdir(parents=True, exist_ok=True)
    (harch_dir / "index.html").write_text(render_harch_page(), encoding="utf-8")
    for t in TREATMENTS:
        d = OUT / t["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(render_page(t), encoding="utf-8")
    print(f"Generated hub + prep page + Harch page + {len(TREATMENTS)} landing pages")


if __name__ == "__main__":
    main()
