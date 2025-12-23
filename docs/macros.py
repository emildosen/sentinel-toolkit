"""
MkDocs Macros Plugin hooks for dynamic content generation.
"""

from pathlib import Path


def define_env(env):
    """Define variables, macros, and filters for MkDocs Macros plugin."""

    docs_dir = Path(env.project_dir)
    repo_root = docs_dir.parent

    @env.macro
    def get_workbooks():
        """
        Scan /workbooks directory and return list of workbook metadata.
        """
        workbooks_dir = repo_root / "workbooks"
        workbooks = []

        if not workbooks_dir.exists():
            return workbooks

        for item in sorted(workbooks_dir.iterdir()):
            if item.is_dir():
                readme_path = item / "README.md"
                screenshot_path = item / "screenshot.png"
                template_path = item / "template.json"

                if readme_path.exists():
                    workbooks.append({
                        "name": item.name.replace("-", " ").title(),
                        "folder": item.name,
                        "folder_path": str(item.relative_to(repo_root)),
                        "has_screenshot": screenshot_path.exists(),
                        "screenshot_path": f"../assets/{item.name}.png" if screenshot_path.exists() else None,
                        "has_template": template_path.exists(),
                    })

        return workbooks

    @env.macro
    def get_queries():
        """
        Scan /queries directory recursively and return list of KQL files.
        """
        queries_dir = repo_root / "queries"
        queries = []

        if not queries_dir.exists():
            return queries

        for kql_file in sorted(queries_dir.rglob("*.kql")):
            category = kql_file.parent.name if kql_file.parent != queries_dir else "General"

            queries.append({
                "name": kql_file.stem.replace("-", " ").replace("_", " ").title(),
                "slug": kql_file.stem,
                "category": category.replace("-", " ").replace("_", " ").title(),
                "category_slug": category,
                "file_path": str(kql_file),
                "relative_path": str(kql_file.relative_to(repo_root)),
            })

        return queries

    @env.macro
    def read_file(path):
        """Read and return contents of a file."""
        file_path = repo_root / path
        if file_path.exists():
            return file_path.read_text()
        return f"<!-- File not found: {path} -->"

    @env.macro
    def read_workbook_readme(folder_name):
        """Read a workbook README from docs/workbooks/{name}.md."""
        readme_path = docs_dir / "workbooks" / f"{folder_name}.md"
        if readme_path.exists():
            content = readme_path.read_text()
            # Fix screenshot path
            content = content.replace(
                "](screenshot.png)",
                f"](../assets/{folder_name}.png)"
            )
            return content
        return "*Documentation not found*"
