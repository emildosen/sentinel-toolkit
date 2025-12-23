# KQL Queries

Ready-to-use Kusto Query Language queries organized by category.

{% set queries = get_queries() %}
{% set categories = queries | map(attribute='category') | unique | list %}

{% for category in categories %}
## {{ category }}

{% for query in queries if query.category == category %}
### {{ query.name }}

```kql
{{ read_file(query.relative_path) }}
```

[:material-github: View on GitHub](https://github.com/emildosen/sentinel-toolkit/blob/main/{{ query.relative_path }}){ .md-button }

---

{% endfor %}
{% endfor %}
