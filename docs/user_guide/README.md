# Benutzerhandbuch und Schulungsmedien

Ordner für Anwenderdokumentation (ohne Programmierkenntnisse).

| Datei | Inhalt |
| --- | --- |
| `Company_Report_Branding_Benutzerhandbuch.pdf` | Vollständiges Handbuch mit Screenshots, A4, Deutsch |
| `handbuch.html` | Quelldatei des Handbuchs (WeasyPrint) |
| `screenshots/` | Original-Bildschirmfotos aus der Demo |
| `videos/` | Kurzvideos zum Herunterladen und für Odoo eLearning |

Die E-Learning-Lektionen, Quizfragen und der Kursaufbau liegen unter
[`../elearning/`](../elearning/README.md).

PDF neu erzeugen (WeasyPrint muss installiert sein):

```bash
cd docs/user_guide
python3 -c "from weasyprint import HTML; HTML('handbuch.html', base_url='.').write_pdf('Company_Report_Branding_Benutzerhandbuch.pdf')"
```
