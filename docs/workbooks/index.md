# Workbooks Gallery

Browse the collection of Microsoft Sentinel workbooks.

<div class="workbook-gallery" markdown>

{% for workbook in get_workbooks() %}
<div class="workbook-card" markdown>

### [{{ workbook.name }}]({{ workbook.folder }}.md)

{% if workbook.has_screenshot %}
[![{{ workbook.name }}]({{ workbook.screenshot_path }}){ .workbook-thumbnail }]({{ workbook.folder }}.md)
{% else %}
[![{{ workbook.name }}](../assets/placeholder.svg){ .workbook-thumbnail .placeholder }]({{ workbook.folder }}.md)
{% endif %}

</div>
{% endfor %}

</div>
