# KQL Queries

Ready-to-use Kusto Query Language queries organized by category.

{% set queries = get_queries() %}
{% set categories = queries | map(attribute='category') | unique | list %}

{% for category in categories %}
## {{ category }}

{% for query in queries if query.category == category %}
- [{{ query.name }}]({{ query.category_slug }}/{{ query.slug }}.md)
{% endfor %}

{% endfor %}
