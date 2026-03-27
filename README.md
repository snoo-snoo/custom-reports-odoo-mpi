# Company Report Branding

**Odoo 19.0** · Multicompany CI for PDF reports (letterhead, fonts, logo & footer modes) · Odoo.sh compatible

| | |
| --- | --- |
| **Technical name** | `company_report_branding` |
| **License** | LGPL-3 |
| **Author** | MPI GmbH, Michael Plöckinger |
| **Website** | [https://www.mpi-erp.at](https://www.mpi-erp.at) |

---

## English

### Short summary (apps.odoo.com / marketplace)

Give every company its own report branding: upload an A4 letterhead PDF, set heading and body fonts (Google Fonts or upload), design a custom HTML footer, and choose whether Odoo’s standard logo and footer text appear—or stay empty when your letterhead already includes them. All settings are on the company form (multicompany-safe).

### Full description (store / long text)

**Company Report Branding** extends **Settings → Companies** with a **Report branding** tab (administrators only). It applies to standard external PDF layouts (e.g. quotations, deliveries, purchases, invoices, credit notes) that use Odoo’s `web.external_layout` family—so one module covers the usual business documents without forking each report.

**Letterhead:** Upload a PDF (typically your print A4 with logo and corporate design). The first page is rasterized to a background image (optional **PyMuPDF** in the repository root `requirements.txt`, recommended on **Odoo.sh**). Adjustable content margins (mm) keep body text clear of artwork.

**Fonts:** Configure **heading** and **body** independently: keep the Odoo layout default, use a **Google Font** (name), or **upload** a font file (e.g. WOFF2/TTF). Uploaded fonts are served via a secure token URL for reliable PDF rendering.

**Footer:** Choose **standard** (Odoo’s `report_footer`), **custom** (translatable HTML), or **none** (no footer text; layout-specific page lines may still appear depending on the theme).

**Logo:** Choose **standard** (`company.logo`), **hidden**, or **custom** (separate image for reports).

Translations: German UI strings are provided (`i18n/de.po`); English is the default in code.

*Note: Parts of this module were developed with assistance from AI tools; MPI GmbH remains responsible for review, testing, and compliance.*

#### Features (bullet list for the store)

- Per-company **letterhead PDF** with optional background and **margin** controls  
- **Two font channels** (heading + body): theme / Google Font / file upload  
- **Footer modes:** standard Odoo, custom HTML, or empty text area  
- **Logo modes:** standard company logo, hidden, or custom report logo  
- Inherits all main Odoo 19 **external layout** variants (Light, Striped, Boxed, Bold, Folder, Wave, Bubble)  
- **Multicompany:** settings live on `res.company`  
- **Odoo.sh:** declare **PyMuPDF** in root `requirements.txt` for letterhead rasterization  

#### Installation

1. Add this repository to your Odoo.sh project (or copy the `company_report_branding` folder into your addons path).  
2. Ensure **root `requirements.txt`** is present so **PyMuPDF** installs (letterhead PNG generation).  
3. Update the Apps list and install **Company Report Branding**.

#### Configuration

1. Log in as a user in **Settings / Administration** (`base.group_system`).  
2. Open **Settings → Companies →** your company → tab **Report branding**.  
3. Upload letterhead, enable **Use letterhead on reports** if desired, set margins and font/logo/footer options.

#### Technical notes

- Depends on **`web`** only; works with standard QWeb PDF reports using external layouts.  
- **Google Fonts** require outbound HTTPS from the PDF worker to `fonts.googleapis.com` unless you rely on uploads only.  
- Letterhead v1 uses a **raster background**; vector PDF underlay is not included.

---

## Deutsch

### Kurzbeschreibung (apps.odoo.com / Marktplatz)

Volles **Corporate Design** für PDF-Berichte pro Firma: Briefpapier-PDF hochladen, Überschrift- und Fließtext-Schrift wählen (Google Fonts oder Upload), **Fußzeile** als HTML gestalten und festlegen, ob Odoo-**Logo** und **Standard-Fußzeile** angezeigt werden – oder ausgeblendet, wenn das Briefpapier das schon enthält. Alles pro **Unternehmen** (mehrmandantenfähig).

### Vollständige Beschreibung (Store / Langtext)

**Company Report Branding** erweitert **Einstellungen → Unternehmen** um den Reiter **Report branding** (nur für Administratoren). Er wirkt auf die üblichen **externen** PDF-Layouts von Odoo (`web.external_layout` und Varianten)—typischerweise Angebote, Lieferscheine, Bestellungen, Rechnungen, Gutschriften—ohne jeden Bericht einzeln anzupassen.

**Briefpapier:** Sie laden ein PDF (z. B. DIN-A4 mit Logo und Layout). Die **erste Seite** wird als Hintergrundbild für den Bericht verwendet (optional **PyMuPDF** über die **`requirements.txt`** im **Repository-Root**, empfohlen für **Odoo.sh**). **Inhaltsränder** in Millimetern verhindern, dass Text in Grafiken läuft.

**Schriften:** **Überschriften** und **Fließtext** getrennt: Odoo-Standard, **Google Font** (Schriftname) oder **Datei-Upload** (z. B. WOFF2/TTF). Hochgeladene Schriften werden über eine geschützte Token-URL ausgeliefert—stabiler für die PDF-Erzeugung.

**Fußzeile:** Modus **Standard** (Odoo-Feld `report_footer`), **Benutzerdefiniert** (HTML, übersetzbar) oder **Kein Fußzeilentext** (Seitenzeilen je nach Layout können weiterhin erscheinen).

**Logo:** **Standard** (`company.logo`), **Ausblenden** oder **Benutzerdefiniert** (eigenes Bild nur für Berichte).

Übersetzungen: Deutsche UI-Texte über `i18n/de.po`; Englisch ist die Standardsprache im Code.

*Hinweis: Teile dieses Moduls wurden mit Unterstützung von KI-Werkzeugen erstellt; die Verantwortung für Prüfung, Test und Compliance liegt bei der MPI GmbH.*

#### Funktionen (Stichpunkte für den Store)

- **Briefpapier-PDF** pro Unternehmen mit optionalen **Rändern**  
- Zwei **Schrift-Kanäle** (Überschrift + Text): Theme / Google Font / Upload  
- **Fußzeilen-Modi:** Odoo-Standard, eigenes HTML, ohne Textblock  
- **Logo-Modi:** Standard-Logo, ausgeblendet, eigenes Berichts-Logo  
- Unterstützt die gängigen Odoo-19-**Layout-Varianten** (Light, Striped, Boxed, Bold, Folder, Wave, Bubble)  
- **Mehrmandantenfähig** über `res.company`  
- **Odoo.sh:** **PyMuPDF** in der Root-`requirements.txt` für die Briefpapier-Vorschau  

#### Installation

1. Repository ins **Odoo.sh**-Projekt einbinden (oder Ordner `company_report_branding` in den Addon-Pfad legen).  
2. **`requirements.txt`** im **Root** bereitstellen, damit **PyMuPDF** installiert wird.  
3. App-Liste aktualisieren und **Company Report Branding** installieren.

#### Konfiguration

1. Als Benutzer mit **Einstellungen / Administration** anmelden.  
2. **Einstellungen → Unternehmen →** gewünschte Firma → Reiter **Report branding**.  
3. Briefpapier hochladen, bei Bedarf **Use letterhead on reports** aktivieren, Ränder sowie Schrift/Logo/Fußzeile einstellen.

#### Technische Hinweise

- Abhängigkeit nur von **`web`**; für Standard-QWeb-PDFs mit externem Layout.  
- **Google Fonts** benötigen ausgehendes HTTPS zum PDF-Worker hin zu `fonts.googleapis.com`, sofern keine reinen Upload-Schriften genutzt werden.  
- Briefpapier v1: **Raster-Hintergrund**; kein vektorielles PDF-Merge.

---

## Support

Commercial services and ERP projects: [https://www.mpi-erp.at](https://www.mpi-erp.at)
