# OXYGENGDL — Deploy y SEO completo

## Cloudflare Pages

1. https://dash.cloudflare.com → Workers & Pages → proyecto **Oxygengdl**
2. Repo: **yariancn/Oxygengdl**, branch **main**
3. Build command: *(vacío)* | Output: **/**
4. Custom domains: `oxygengdl.com` y `www.oxygengdl.com`

---

## Por qué el dominio aparece en Google pero no está en Search Console

Son cosas **independientes**:

| Concepto | Qué es |
|--------|--------|
| **Dominio registrado** | Lo compraste en Namecheap hace tiempo |
| **Sitio indexado en Google** | Google encontró páginas (Canva, Dashnex, landing de terceros) y las guardó en su índice **sin que nadie registrara nada** |
| **Search Console** | Herramienta gratuita del **dueño** para ver rendimiento, errores, solicitar indexación y enviar sitemap. **No es obligatoria** para aparecer en Google, pero **sí es obligatoria** si quieres controlar y acelerar la migración |

Hoy Google todavía muestra señales viejas:
- `oxygengdl.lp-digiclic.com` (dirección antigua Montenegro 2155)
- `oxygengdl.setmore.com` (misma dirección vieja)
- Posible caché del sitio Canva

El sitio nuevo en `https://oxygengdl.com/` es técnicamente correcto, pero Google aún no lo ha consolidado como fuente principal.

---

## Paso 1 — Google Search Console (hacer hoy)

### A. Crear la propiedad

1. Entra a https://search.google.com/search-console
2. Clic en **Agregar propiedad**
3. Elige **Prefijo de URL**: `https://oxygengdl.com`
4. Método de verificación recomendado: **Registro DNS** (porque el DNS ya está en Cloudflare)

### B. Verificar por DNS en Cloudflare

1. Search Console te dará un registro TXT, algo como:
   ```
   google-site-verification=XXXXXXXXXXXXXXXX
   ```
2. Cloudflare → dominio **oxygengdl.com** → **DNS** → **Add record**
   - Type: **TXT**
   - Name: `@` (o deja en blanco)
   - Content: el valor completo que te dio Google
   - TTL: Auto
3. Guardar y en Search Console clic en **Verificar**
4. Repite para `https://www.oxygengdl.com` o configura redirección www → raíz (ya en Pages)

### C. Enviar sitemap

1. Search Console → **Sitemaps**
2. Agregar solo: `sitemap.xml` (sin URL completa; GSC ya usa el dominio verificado)
3. Estado debe quedar **Correcto** con 1 página descubierta

#### Si dice "No se ha podido obtener"

El sitemap responde bien en el navegador, pero Googlebot puede estar bloqueado por Cloudflare:

1. **Cloudflare** → dominio `oxygengdl.com` → **Security** → **Events**
   - Filtrar por User-Agent `Googlebot`
   - Si aparece bloqueado (403, challenge, JS challenge) → ese es el problema
2. **Desactivar Bot Fight Mode** (si está activo):
   - Security → Settings → **Bot Fight Mode** → Off
   - O crear regla WAF: si User-Agent contiene `Googlebot` → **Skip** / Allow
3. En Search Console → Sitemaps → **eliminar** el sitemap fallido
4. Esperar 5 minutos tras el deploy y **volver a enviar** `sitemap.xml`
5. Probar en **Inspección de URLs**: pegar `https://oxygengdl.com/sitemap.xml` → **Probar URL publicada**

> Nota: el redirect de `www` a raíz usa `//oxygengdl.com/` (sin `https:`). En Cloudflare → Rules, conviene corregirlo a `https://oxygengdl.com/$1` para evitar problemas con crawlers.

### D. Solicitar indexación de la página principal

1. Search Console → **Inspección de URLs**
2. Pegar: `https://oxygengdl.com/`
3. Clic en **Solicitar indexación**

---

## Paso 2 — Google Business Profile (hacer hoy)

1. https://business.google.com → **CAMARA HIPERBARICA OXYGENGDL**
2. Actualizar **Sitio web** → `https://oxygengdl.com`
3. Confirmar dirección: **C. Gral. San Martín 420, Col. Americana, Obrera, 44150 Guadalajara, Jal.**
4. Confirmar teléfono: **33 2833 2686**
5. Confirmar horario: L-V 7:30–20:00, S 9:00–14:00
6. Subir fotos recientes (instalaciones, cámara, fachada)

---

## Paso 3 — Eliminar duplicados (esta semana)

| Sitio viejo | Acción |
|-------------|--------|
| Canva (`oxygengdl.com` viejo) | Ya redirigido a Cloudflare Pages ✓ |
| Dashnex `oxy.dashnexpages.net` | Cancelar o poner redirect 301 a `https://oxygengdl.com/` |
| `oxygengdl.lp-digiclic.com` | Actualizar dirección y enlace al sitio nuevo, o desactivar |
| `oxygengdl.setmore.com` | Actualizar dirección a San Martín 420; mantener solo para reservas si lo usan |

En Search Console, cuando esté verificado, revisa **Páginas** → URLs con duplicados o no indexadas.

---

## Paso 4 — Bing Webmaster Tools (opcional, 10 min)

1. https://www.bing.com/webmasters
2. Importar desde Google Search Console (más rápido) o verificar por DNS igual que Google
3. Enviar sitemap: `https://oxygengdl.com/sitemap.xml`

---

## Paso 5 — Monitoreo (primeras 4 semanas)

Revisar cada semana en Search Console:

- [ ] **Páginas** — `https://oxygengdl.com/` indexada
- [ ] **Rendimiento** — impresiones para "cámara hiperbárica guadalajara"
- [ ] **Experiencia** — sin errores de Core Web Vitals
- [ ] **Mejoras** — FAQ y datos estructurados sin errores

Comprobar en Google: `site:oxygengdl.com` — debe aparecer solo el sitio nuevo.

---

## Checklist técnico del sitio (ya hecho)

- [x] Dominio único con canonical `https://oxygengdl.com/`
- [x] `robots.txt` + `sitemap.xml`
- [x] Schema.org (clínica, servicio, FAQ, rating 4.8/84)
- [x] Meta description, Open Graph, geo
- [x] `llms.txt` para buscadores IA
- [x] Redirecciones URLs viejas Canva (`_redirects`)
- [x] HTTPS en Cloudflare
- [x] NAP consistente (nombre, dirección, teléfono, email)
- [ ] Search Console verificado ← **pendiente**
- [ ] Sitemap enviado en Search Console ← **pendiente**
- [ ] GBP con URL nueva ← **pendiente**
- [ ] Dashnex / landing viejas apagadas o redirigidas ← **pendiente**

---

## Tiempo estimado de autoridad

| Fase | Tiempo |
|------|--------|
| Verificación Search Console + sitemap | Mismo día |
| Primera indexación del sitio nuevo | 3–14 días |
| Reemplazar páginas viejas en resultados | 2–6 semanas |
| Posicionamiento estable "cámara hiperbárica guadalajara" | 1–3 meses |

La base técnica ya está. Lo que falta es **verificar propiedad**, **decirle a Google que migre** y **apagar los duplicados**.
