# Company Report Branding

**Odoo 19.0** · Multicompany CI for PDF reports (letterhead, fonts, logo & footer, line notes) · Odoo.sh compatible

| | |
| --- | --- |
| **Technical name** | `company_report_branding` |
| **Version** | 19.0.1.3.0 |
| **License** | LGPL-3 |
| **Author** | MPI GmbH, Michael Plöckinger |
| **Website** | [https://www.mpi-erp.at](https://www.mpi-erp.at) |

Store assets live in `company_report_branding/static/description/` (`icon.png`, `banner.png`, `cover.png`, screenshots, `index.html`).

---

## English

### Short summary (apps.odoo.com / marketplace)

Give every company its own report branding: upload an A4 letterhead PDF, set heading and body fonts (Google Fonts or upload), design a custom HTML footer, choose whether Odoo’s standard logo and footer text appear, and print optional HTML above or below document lines. All settings are on the company form (multicompany-safe).

### Full description (store / long text)

**Company Report Branding** extends **Settings → Companies** with a **Report branding** tab (administrators only). It applies to standard external PDF layouts (quotations, deliveries, purchases, invoices, credit notes, vendor documents) that use Odoo’s `web.external_layout` family—so one module covers the usual business documents without forking each report. Branding can be switched on or off per document family.

**Letterhead:** Upload a PDF (typically your print A4 with logo and corporate design). The first page is rasterized to a background image (optional **PyMuPDF** in the repository root `requirements.txt`, recommended on **Odoo.sh**). Adjustable content margins (mm) keep body text clear of artwork.

**Fonts:** Configure **heading** and **body** independently: keep the Odoo layout default, use a **Google Font** (name), or **upload** a font file (e.g. WOFF2/TTF). Uploaded fonts are served via a secure token URL for reliable PDF rendering.

**Footer:** Choose **standard** (Odoo’s `report_footer`), **custom** (translatable HTML), or **none** (no footer text; layout-specific page lines may still appear depending on the theme).

**Logo:** Choose **standard** (`company.logo`), **hidden**, or **custom** (separate image for reports).

**Line notes:** Optional translatable HTML blocks printed **above** and **below** the main product table, separately for quotations, deliveries, purchase orders, invoices, credit notes, and vendor bills.

Translations: German UI strings are provided (`i18n/de.po`); English is the default in code.

*Note: Parts of this module were developed with assistance from AI tools; MPI GmbH remains responsible for review, testing, and compliance.*

#### Features (bullet list for the store)

- Per-company **letterhead PDF** with optional background and **margin** controls
- **Per-report switches** for sales, stock, purchase, invoices, credit notes, vendor documents, and other external PDFs
- **Two font channels** (heading + body): theme / Google Font / file upload
- **Footer modes:** standard Odoo, custom HTML, or empty text area
- **Logo modes:** standard company logo, hidden, or custom report logo
- **HTML notes** above/below line tables, per document type
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
3. Choose which reports receive branding, upload letterhead, enable **Use letterhead on reports** if desired, then set margins, fonts, logo, footer, and optional line notes.

#### Technical notes

- Depends on **`web`**, **`sale`**, **`stock`**, **`purchase`**, and **`account`**.
- **Google Fonts** require outbound HTTPS from the PDF worker to `fonts.googleapis.com` unless you rely on uploads only.
- Letterhead v1 uses a **raster background**; vector PDF underlay is not included.

---

## Deutsch

### Kurzbeschreibung (apps.odoo.com / Marktplatz)

Volles **Corporate Design** für PDF-Berichte pro Firma: Briefpapier-PDF hochladen, Überschrift- und Fließtext-Schrift wählen (Google Fonts oder Upload), **Fußzeile** als HTML gestalten, festlegen ob Odoo-**Logo** und **Standard-Fußzeile** angezeigt werden, und optionale HTML-Texte ober- und unterhalb der Positionstabelle drucken. Alles pro **Unternehmen** (mehrmandantenfähig).

### Vollständige Beschreibung (Store / Langtext)

**Company Report Branding** erweitert **Einstellungen → Unternehmen** um den Reiter **Report branding** (nur für Administratoren). Er wirkt auf die üblichen **externen** PDF-Layouts von Odoo (`web.external_layout` und Varianten)—typischerweise Angebote, Lieferscheine, Bestellungen, Rechnungen, Gutschriften, Lieferantenbelege—ohne jeden Bericht einzeln anzupassen. Die Anwendung lässt sich **pro Belegfamilie** ein- und ausschalten.

**Briefpapier:** Sie laden ein PDF (z. B. DIN-A4 mit Logo und Layout). Die **erste Seite** wird als Hintergrundbild für den Bericht verwendet (optional **PyMuPDF** über die **`requirements.txt`** im **Repository-Root**, empfohlen für **Odoo.sh**). **Inhaltsränder** in Millimetern verhindern, dass Text in Grafiken läuft.

**Schriften:** **Überschriften** und **Fließtext** getrennt: Odoo-Standard, **Google Font** (Schriftname) oder **Datei-Upload** (z. B. WOFF2/TTF). Hochgeladene Schriften werden über eine geschützte Token-URL ausgeliefert—stabiler für die PDF-Erzeugung.

**Fußzeile:** Modus **Standard** (Odoo-Feld `report_footer`), **Benutzerdefiniert** (HTML, übersetzbar) oder **Kein Fußzeilentext** (Seitenzeilen je nach Layout können weiterhin erscheinen).

**Logo:** **Standard** (`company.logo`), **Ausblenden** oder **Benutzerdefiniert** (eigenes Bild nur für Berichte).

**Texte an der Positionstabelle:** Optionale, übersetzbare HTML-Blöcke **oberhalb** und **unterhalb** der Haupttabelle, getrennt für Angebote, Lieferscheine, Bestellungen, Rechnungen, Gutschriften und Lieferantenbelege.

Übersetzungen: Deutsche UI-Texte über `i18n/de.po`; Englisch ist die Standardsprache im Code.

*Hinweis: Teile dieses Moduls wurden mit Unterstützung von KI-Werkzeugen erstellt; die Verantwortung für Prüfung, Test und Compliance liegt bei der MPI GmbH.*

#### Funktionen (Stichpunkte für den Store)

- **Briefpapier-PDF** pro Unternehmen mit optionalen **Rändern**
- **Schalter pro Berichtstyp** (Verkauf, Lager, Einkauf, Rechnung, Gutschrift, Lieferantenbelege, übrige PDFs)
- Zwei **Schrift-Kanäle** (Überschrift + Text): Theme / Google Font / Upload
- **Fußzeilen-Modi:** Odoo-Standard, eigenes HTML, ohne Textblock
- **Logo-Modi:** Standard-Logo, ausgeblendet, eigenes Berichts-Logo
- **HTML-Texte** über/unter der Positionstabelle, je Belegtyp
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
3. Berichtstypen wählen, Briefpapier hochladen, bei Bedarf **Use letterhead on reports** aktivieren, Ränder sowie Schrift/Logo/Fußzeile und optionale Tabellentexte einstellen.

#### Technische Hinweise

- Abhängigkeiten: **`web`**, **`sale`**, **`stock`**, **`purchase`**, **`account`**.
- **Google Fonts** benötigen ausgehendes HTTPS zum PDF-Worker hin zu `fonts.googleapis.com`, sofern keine reinen Upload-Schriften genutzt werden.
- Briefpapier v1: **Raster-Hintergrund**; kein vektorielles PDF-Merge.

---

## Anwenderdokumentation / eLearning

Schulungsunterlagen für allgemeine Benutzer (Deutsch, mit Screenshots und Videos):

- **Handbuch (PDF):** [`docs/user_guide/Company_Report_Branding_Benutzerhandbuch.pdf`](docs/user_guide/Company_Report_Branding_Benutzerhandbuch.pdf)
- **Übersicht:** [`docs/README.md`](docs/README.md)
- **Odoo-Kurs:** optionales Addon [`company_report_branding_elearning`](company_report_branding_elearning/README.md) (App eLearning)

---

## Support

Commercial services and ERP products: [https://www.mpi-erp.at](https://www.mpi-erp.at) · [office@mpi-erp.at](mailto:office@mpi-erp.at)
