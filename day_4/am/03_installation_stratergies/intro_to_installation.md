
# Installing Python Packages from Git Repositories

This guide explains how to install Python packages directly from GitLab or GitHub using `pip`.  
Supports versioned, branch-based, and commit-specific installations.

---

## Format Summary

```bash
pip install git+https://<provider>/<username>/<repo>.git@<branch>#egg=<package>
```

Only the repo URL is strictly required — the rest helps clarify intent.

---

## GitLab Install Examples

### 1. Install latest main branch

```bash
pip install git+https://gitlab.com/PTR/applied_scientific_python.git@main
```

### 2. Install specific tag or version (e.g., v1.2.0)

```bash
pip install git+https://gitlab.com/PTR/applied_scientific_python.git@v1.2.0
```

### 3. Install from a feature branch

```bash
pip install git+https://gitlab.com/PTR/applied_scientific_python.git@feature/cli-improvements
```

---

## GitHub Install Examples

### 1. Install from main (GitHub)

```bash
pip install git+https://github.com/yourusername/your-repo.git@main
```

### 2. Install from a tag or commit

```bash
pip install git+https://github.com/yourusername/your-repo.git@abc1234
```

### Private Repositories

Using a personal access token:

```bash
pip install git+https://<token>@gitlab.com/PTR/private-repo.git
```

Using SSH:

```bash
pip install git+ssh://git@gitlab.com/PTR/private-repo.git
```

---

## Editable Local Installs (Development Mode)

Used when you're working on the package source locally:

```bash
pip install -e .
```

This creates a symlink instead of copying your code into site-packages.

> Requires a `setup.py` in the root of your project.

---

## Expectations & Use Cases

| Situation                         | Best Practice                               |
|----------------------------------|---------------------------------------------|
| CI installs from Git repo        | Use pinned commit hash or tag (not main)    |
| Dev installs (local editable)    | Use `pip install -e .`                      |
| Public tools                     | Use PyPI or GitHub tags                     |
| Private team projects            | Use GitLab with tokens or SSH               |
| Reproducibility / Version locks  | Pin `@commit` or `@version`                 |

---

## Bonus: Use in requirements.txt

```text
git+https://gitlab.com/PTR/applied_scientific_python.git@v1.2.0#egg=applied_scientific_python
```

---

## References

- [pip VCS support](https://pip.pypa.io/en/stable/topics/vcs-support/)
- [GitLab Personal Access Tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
- [Python Packaging Guide](https://packaging.python.org/tutorials/packaging-projects/)
