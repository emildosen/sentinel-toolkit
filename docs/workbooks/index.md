# Workbooks Gallery

Browse the collection of Microsoft Sentinel workbooks. Click any screenshot to enlarge.

<div class="workbook-gallery" markdown>

{% for workbook in get_workbooks() %}
<div class="workbook-card" markdown>

## {{ workbook.name }}

{% if workbook.has_screenshot %}
[![{{ workbook.name }}]({{ workbook.screenshot_path }}){ .workbook-thumbnail }]({{ workbook.screenshot_path }})
{% else %}
![Screenshot Coming Soon](../assets/placeholder.svg){ .workbook-thumbnail .placeholder }
{% endif %}

<div class="workbook-content" markdown>

{{ read_readme_content(workbook.readme_path) }}

</div>

[:material-download: View Template on GitHub](https://github.com/emildosen/sentinel-toolkit/blob/main/{{ workbook.folder_path }}/template.json){ .md-button }

---

</div>
{% endfor %}

</div>
